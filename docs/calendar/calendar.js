async function initCalendar() {
    const events = await loadEvents();
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
        events: events,
        views: {
            timeGridWeek: {pointer: true},
        },
        dayMaxEvents: true,
        nowIndicator: true,
        selectable: true,
        editable: true,
        //eventSources: [{url: "calendar/events.json"}]
    });
    
    window.ec = ec;
}

// parse events.yaml
async function loadEvents() {
    try {
        const response = await fetch('calendar/events.yaml');
        if (!response.ok) {
            throw new Error("Network response was not ok: " + response.statusText);
        }
        const yamlText = await response.text();
        const events = jsyaml.load(yamlText);
        
        if (!Array.isArray(events)) {
            throw new Error("Parsed YAML is not an array");
        }

        return events.map(event => ({
            start: event.start,
            end: event.end,
            title: event.title,
            color: event.color
        }));
    } catch (error) {
        console.error("Error fetching or parsing YAML:", error);
        return [];
    }
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

document.addEventListener('DOMContentLoaded', () => {
    initCalendar();
});