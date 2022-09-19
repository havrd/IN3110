from bs4 import BeautifulSoup
import requests as req
import requesting_urls as ru
import re
import os


def extract_events(url):
    """
    Extract date, venue and discipline for competitions.
    Args:
        url(str): The url to extract events from.
    Returns:
        table_info( list of lists ): A nested list where the rows represent each race date, and the columns are [date, venue, discipline ].
    """

    disciplines = {
       "DH":"Downhill",
       "SL":"Slalom",
       "GS":"Giant Slalom",
       "SG":"Super Giant Slalom",
       "AC":"Alpine Combined",
       "PG":"Parallel Giant Slalom",
        }

    html = ru.get_html(url)
    soup = BeautifulSoup(html, "html.parser")

    calendar_header = soup.find(id="Calendar")
    calendar_table = calendar_header.find_all_next("table")[0]
    rows = calendar_table.find_all("tr")

    found_event = None
    found_venue = None
    found_discipline = None
    found_date = None
    events = []

    header = rows[0].find_all("th")

    event_index = 0
    date_index = 0
    venue_index = 0
    long_discipline_index = 0
    i = 0
    for cell in header:
        if cell.text == 'Event\n':
            event_index = i
        if cell.text == 'Date\n':
            date_index = i
        if cell.text == 'Venue\n':
            venue_index = i
        if cell.text == 'Type\n':
            long_discipline_index = i
        i += 1

    short_discipline_index = long_discipline_index-2

    full_row_length = 11
    short_row_length = full_row_length - 2

    for row in rows :
        cells = row.find_all("td")

        if len( cells ) not in {full_row_length, short_row_length}:
            continue

        # Hard - coding indexes works for now(you should find them using the Header !)
        event = cells[event_index]
        if re.match(r"\d{1,3}", event.text.strip()):
            found_event = event.text.strip()
        else:
            found_event = None

        date = cells[date_index]
        if re.match(r"\d{1,2} [a-zA-Z]+ \d{4}", date.text.strip()):
            found_date = date.text.strip()
        else:
            found_date = None

        if len( cells ) == full_row_length :
        # If event is cancelled, the index below might need to be shifted.
            venue_cell = cells [venue_index]
            found_venue = venue_cell.text.strip()
            discipline_index = long_discipline_index
        else :
        # repeated venue, discipline is in a different column
            discipline_index = short_discipline_index

        discipline = cells[discipline_index]
        discipline_regex = r"^([A-Z]{2})"
        discipline_match = re.search(discipline_regex, discipline.text.strip())

        if discipline_match :
            found_discipline = disciplines.get(discipline_match[0])
        else :
            found_discipline = None


        if found_venue and found_event and found_discipline and found_date:
            events.append(( found_event, found_date, found_venue ,found_discipline ))

    return events

def create_betting_slip(events, save_as):
    """
    Saves a markdown format betting slip to the location './datetime_filter/< save_as >.md'.
    Args :
        events (list): takes a list of 3- tuples containing date, venue and type for each event.
        save_as (string): filename to save the markdown betting slip as.
    """
    # ensure directory exists
    os.makedirs("datetime_filter", exist_ok=True )

    with open(f"./datetime_filter/{save_as}.md", "w") as out_file:
        out_file.write(f"#BETTING SLIP\n\nName :\n\n")
        out_file.write(" Event | Date | Venue | Discipline | Who wins?\n")
        out_file.write(" --- | --- | --- | --- | --- \n")
        for e in events:
            event, date, venue, type = e
            out_file.write(f"{event} | {date} | {venue} | {type} |\n")

url ="https://en.wikipedia.org/wiki/2021-22_FIS_Alpine_Ski_World_Cup"
events = extract_events(url)
create_betting_slip(events, "betting_slip_empty")
