const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const { DateTime } = require('luxon');
const { RRule } = require('rrule');

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
    try {
        const yamlText = fs.readFileSync('./docs/calendar/events.yaml', 'utf8'); // Read the YAML file
        const events = yaml.load(yamlText);

        if (!Array.isArray(events)) {
            throw new Error("Parsed YAML is not an array");
        }

        const expandedEvents = [];
        for (const event of events) {
            const startDate = new Date(event.start);
            const endDate = new Date(event.end);

            if (event.recurrence) {
                const rrule = new RRule({
                    ...RRule.parseString(event.recurrence),
                    dtstart: startDate,
                });

                rrule.all().forEach(date => {
                    const end = new Date(date.getTime() + (endDate - startDate));
                    expandedEvents.push({
                        start: date.toISOString(),
                        end: end.toISOString(),
                        title: event.title,
                        color: event.color,
                        location: event.location,
                        description: event.description,
                    });
                });
            } else {
                // Non-recurring event
                expandedEvents.push({
                    start: event.start,
                    end: event.end,
                    title: event.title,
                    color: event.color,
                    location: event.location,
                    description: event.description,
                });
            }
        }

        console.log("Expanded events:", expandedEvents);
        return expandedEvents;
    } catch (error) {
        console.error("Error fetching or parsing YAML:", error);
        return [];
    }
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

    function parseDate(input) {
        try {
            if (typeof input === 'string' && input.includes('T')) {
                return DateTime.fromISO(input);
            } else if (typeof input === 'string') {
                return DateTime.fromFormat(input, "yyyy-MM-dd HH:mm");
            } else {
                throw new Error("Invalid date format");
            }
        } catch (error) {
            console.error("Error parsing date:", input, error);
            return null;
        }
    }

    const vevents = events
        .map(event => {
            const dtstart = parseDate(event.start);
            const dtend = parseDate(event.end);

            if (!dtstart || !dtend) {
                console.error("Skipping event due to invalid dates:", event);
                return null;
            }

            return `
BEGIN:VEVENT
UID:${Math.random().toString(36).substring(2, 15)}
SUMMARY:${event.title}
DTSTAMP:${DateTime.now().toUTC().toFormat("yyyyMMdd'T'HHmmss'Z'")}
DTSTART;TZID=Europe/Berlin:${dtstart.toFormat("yyyyMMdd'T'HHmmss")}
DTEND;TZID=Europe/Berlin:${dtend.toFormat("yyyyMMdd'T'HHmmss")}
DESCRIPTION:${event.description || ''}
LOCATION:${event.location || ''}
END:VEVENT`;
        })
        .filter(Boolean) // Remove null values
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
