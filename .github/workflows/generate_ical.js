const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const { DateTime } = require('luxon'); // For timezone handling

function parseDateTime(dateTimeString) {
    // Parse "YYYY-MM-DD HH:MM" into Berlin timezone [YYYY, MM, DD, HH, MM]
    const dateTime = DateTime.fromFormat(dateTimeString, 'yyyy-MM-dd HH:mm', { zone: 'Europe/Berlin' });
    if (dateTime.isValid) {
        return [
            dateTime.year,
            dateTime.month,
            dateTime.day,
            dateTime.hour,
            dateTime.minute,
        ];
    } else {
        console.warn(`Invalid date-time format: ${dateTimeString}`);
        return null; // Return null for invalid date-time
    }
}

async function loadEvents() {
    const yamlText = fs.readFileSync('docs/calendar/events.yaml', 'utf8');
    const events = yaml.load(yamlText);

    if (!Array.isArray(events)) {
        throw new Error('Parsed YAML is not an array');
    }

    return events
        .map(event => {
            const start = parseDateTime(event.start);
            const end = parseDateTime(event.end);

            if (!start || !end) {
                console.warn(`Skipping event with invalid dates: ${JSON.stringify(event)}`);
                return null; // Skip invalid events
            }

            return {
                start,
                end,
                title: event.title,
                description: event.description || '',
                location: event.location || '',
                recurrence: event.recurrence || null, // Include recurrence if provided
            };
        })
        .filter(event => event !== null); // Filter out invalid events

}

function generateICal(events) {
    const vtimezone = `
BEGIN:VTIMEZONE
TZID:Europe/Berlin
BEGIN:STANDARD
DTSTART:20231029T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
END:STANDARD
BEGIN:DAYLIGHT
DTSTART:20240331T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
END:DAYLIGHT
END:VTIMEZONE`;

    const vevents = events
        .map(event => {
            const recurrenceRule = event.recurrence ? `RRULE:${event.recurrence}` : '';
            return `
BEGIN:VEVENT
UID:${Math.random().toString(36).substring(2, 15)}
SUMMARY:${event.title}
DTSTAMP:${DateTime.now().toUTC().toFormat("yyyyMMdd'T'HHmmss'Z'")}
DTSTART;TZID=Europe/Berlin:${DateTime.fromObject({
                year: event.start[0],
                month: event.start[1],
                day: event.start[2],
                hour: event.start[3],
                minute: event.start[4],
            }).toFormat("yyyyMMdd'T'HHmmss")}
DTEND;TZID=Europe/Berlin:${DateTime.fromObject({
                year: event.end[0],
                month: event.end[1],
                day: event.end[2],
                hour: event.end[3],
                minute: event.end[4],
            }).toFormat("yyyyMMdd'T'HHmmss")}
${recurrenceRule}
DESCRIPTION:${event.description}
LOCATION:${event.location}
END:VEVENT`;
        })
        .join("\n");

    return `BEGIN:VCALENDAR
VERSION:2.0
CALSCALE:GREGORIAN
PRODID:-//YourOrganization//YourProduct//EN
METHOD:PUBLISH
X-PUBLISHED-TTL:PT1H
${vtimezone}
${vevents}
END:VCALENDAR`;
}

(async () => {
    try {
        const events = await loadEvents();
        console.log('Loaded events:', events); // Log loaded events for debugging
        const icalContent = generateICal(events);

        const outputPath = path.join('docs/calendar/digital_work_cal.ical');
        fs.writeFileSync(outputPath, icalContent, 'utf8');
        console.log('iCal file generated and saved to:', outputPath);
    } catch (error) {
        console.error('Error during iCal generation:', error);
        process.exit(1); // Exit with error
    }
})();
