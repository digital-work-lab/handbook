const ec = new EventCalendar(document.getElementById('ec'), {
    view: 'dayGridMonth',
    headerToolbar: {
        start: 'today,prev,next',
        center: 'title',
        end: 'dayGridMonth,timeGridWeek,listWeek'
    },
    buttonText: {
        close: 'Close', dayGridMonth: 'Month', listDay: 'list', listMonth: 'list', listWeek: 'Schedule', listYear: 'list', resourceTimeGridDay: 'resources', resourceTimeGridWeek: 'resources', resourceTimelineDay: 'timeline', resourceTimelineMonth: 'timeline', resourceTimelineWeek: 'timeline', timeGridDay: 'day', timeGridWeek: 'Week', today: 'Today'
    },
    scrollTime: '09:00:00',
    events: loadEvents(),
    views: {
        timeGridWeek: {pointer: true},
    },
    dayMaxEvents: true,
    nowIndicator: true,
    selectable: true,
    editable: true,
    eventAllUpdated: alert("hello")
});

function loadEvents() {
    let days = [];
    for (let i = 0; i < 7; ++i) {
        let day = new Date();
        let diff = i - day.getDay();
        day.setDate(day.getDate() + diff);
        days[i] = day.getFullYear() + "-" + _pad(day.getMonth()+1) + "-" + _pad(day.getDate());
    }

    return [
        {start: days[0] + " 00:00", end: days[0] + " 09:00", display: "background"},
        {start: days[1] + " 12:00", end: days[1] + " 14:00", display: "background"},
        {start: days[2] + " 17:00", end: days[2] + " 24:00", display: "background"},
        {start: days[0] + " 10:00", end: days[0] + " 14:00", title: "The calendar can display background and regular events", color: "#FE6B64"},
        {start: days[1] + " 16:00", end: days[2] + " 08:00", title: "An event may span to another day", color: "#B29DD9"},
        {start: days[2] + " 09:00", end: days[2] + " 13:00", title: "Events can be assigned to resources and the calendar has the resources view built-in", color: "#779ECB"},
        {start: days[3] + " 14:00", end: days[3] + " 20:00", title: "", color: "#FE6B64"},
        {start: days[3] + " 15:00", end: days[3] + " 18:00", title: "Overlapping events are positioned properly", color: "#779ECB"},
        {start: days[5] + " 10:00", end: days[5] + " 16:00", title: {html: "You have complete control over the <i><b>display</b></i> of events…"}, color: "#779ECB"},
        {start: days[5] + " 14:00", end: days[5] + " 19:00", title: "…and you can drag and drop the events!", color: "#FE6B64"},
        {start: days[5] + " 18:00", end: days[5] + " 21:00", title: "", color: "#B29DD9"},
        {start: days[1], end: days[3], resourceId: 1, title: "All-day events can be displayed at the top", color: "#B29DD9", allDay: true}
    ];
}

function _pad(num) {
    let norm = Math.floor(Math.abs(num));
    return (norm < 10 ? '0' : '') + norm;
}