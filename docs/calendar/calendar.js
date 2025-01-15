async function initCalendar() {
    const events = await loadEventsFromICal();
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
            timeGridWeek: { pointer: true },
        },
        eventClick: function(info) {
            popUpEvent(info.event);
        },
        dayMaxEvents: true,
        nowIndicator: true,
        eventStartEditable: false,
        hiddenDays: [0, 6],
    });

    window.ec = ec;
}

// Parse events from iCal file
async function loadEventsFromICal() {
    try {
        const response = await fetch('https://raw.githubusercontent.com/digital-work-lab/handbook/main/docs/calendar/digital_work_cal.ical');
        if (!response.ok) {
            throw new Error("Network response was not ok: " + response.statusText);
        }
        const iCalText = await response.text();
        const jcalData = ICAL.parse(iCalText);
        const vcalendar = new ICAL.Component(jcalData);
        const vevents = vcalendar.getAllSubcomponents('vevent');

        return vevents.map(vevent => {
            const event = new ICAL.Event(vevent);
            return {
                start: event.startDate.toJSDate(),
                end: event.endDate.toJSDate(),
                title: event.summary,
                description: event.description,
                location: event.location,
            };
        });
    } catch (error) {
        console.error("Error fetching or parsing iCal file:", error);
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

function popUpEvent(event) {
    const startTime = event.start.toLocaleString();
    const endTime = event.end ? event.end.toLocaleString() : 'undefined';

    // modal
    const modal = document.createElement('div');
    modal.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        z-index: 1000;
        width: 400px;
    `;

    // overlay
    const overlay = document.createElement('div');
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0,0,0,0.5);
        z-index: 999;
    `;

    modal.innerHTML = `
        <div>
            <h3>${event.title}</h3>
            <p>start: ${startTime}</p>
            <p>end: ${endTime}</p>
            <div style="text-align: center; margin-top: 15px;">
                <button onclick="this.closest('div').parentElement.parentElement.remove();document.querySelector('[data-modal-overlay]').remove()">Close</button>
            </div>
        </div>
    `;

    overlay.setAttribute('data-modal-overlay', '');
    document.body.appendChild(overlay);
    document.body.appendChild(modal);
}

document.addEventListener('DOMContentLoaded', () => {
    initCalendar();
});