const ec = new EventCalendar(document.getElementById('ec'), {
    view: 'dayGridMonth',
    customButtons: {
        exportBtn: {
            text: 'export',
            click: function() {
                generateICal();
            }
        }
    },
    headerToolbar: {
        start: 'today,prev,next',
        center: 'title',
        end: 'dayGridMonth,timeGridWeek,listWeek exportBtn'
    },
    buttonText: {
        close: 'Close', dayGridMonth: 'Month', listDay: 'list', listMonth: 'list', listWeek: 'Schedule', listYear: 'list', resourceTimeGridDay: 'resources', resourceTimeGridWeek: 'resources', resourceTimelineDay: 'timeline', resourceTimelineMonth: 'timeline', resourceTimelineWeek: 'timeline', timeGridDay: 'day', timeGridWeek: 'Week', today: 'Today'
    },
    scrollTime: '09:00:00',
    //events: loadEvents(),
    views: {
        timeGridWeek: {pointer: true},
    },
    dayMaxEvents: true,
    nowIndicator: true,
    selectable: true,
    editable: true,
    //eventClick: eventClickM,
    eventSources: [{url: "calendar/events.json"}]
});

function eventClickM(info) {
    const eventId = info.event.id;
    alert(eventId);
    alert(info.event.start);
}

function loadEvents() {
    let days = [];
    for (let i = 0; i < 7; ++i) {
        let day = new Date();
        let diff = i - day.getDay();
        day.setDate(day.getDate() + diff);
        days[i] = day.getFullYear() + "-" + _pad(day.getMonth()+1) + "-" + _pad(day.getDate());
    }
    //return [
    //    {start: days[0] + " 00:00", end: days[0] + " 09:00", title: "background"},
    //    {start: days[1] + " 12:00", end: days[1] + " 14:00", title: "background"},
    //    {start: days[2] + " 17:00", end: days[2] + " 24:00", title: "background"}
    //];

    res =  [
            {start: days[0] + " 00:00", end: days[0] + " 09:00", title: "background"},
            {start: days[1] + " 12:00", end: days[1] + " 14:00", title: "background"},
            {start: days[2] + " 17:00", end: days[2] + " 24:00", title: "background"}
        ];
    
    return fetch('calendar/events.yaml')
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok: " + response.statusText);
            }
            return response.text();
        })
        .then(yamlText => {
            console.log("Fetched YAML text:", yamlText); // 调试输出
            const events = jsyaml.load(yamlText); // 使用 jsyaml 库解析 YAML
            
            if (!Array.isArray(events)) {
                throw new Error("Parsed YAML is not an array");
            }
            let eventList = []; // 新增事件列表
            events.forEach(event => {
                eventList.push({
                    start: event.start,
                    end: event.end,
                    title: event.title
                });
            });
            alert(eventList);
            return eventList; // 返回事件列表
        })
        .catch(error => {
            console.error("Error fetching or parsing YAML:", error); // 错误处理
        });
}

function _pad(num) {
    let norm = Math.floor(Math.abs(num));
    return (norm < 10 ? '0' : '') + norm;
}

function generateICal() {
    const events = ec.getEvents();
    
    var cal = ics();

    events.forEach(event => {
        cal.addEvent(event.title || " ", event.description || " ", event.location || " ", event.start, event.end);
    });

    const blob = new Blob([cal.toString()], { type: 'text/calendar' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'calendar.ics';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}