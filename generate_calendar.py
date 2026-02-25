import requests
from icalendar import Calendar, Event
from datetime import datetime
import os

USERNAME = os.environ["UNTIS_USERNAME"]
PASSWORD = os.environ["UNTIS_PASSWORD"]
SCHOOL = os.environ["UNTIS_SCHOOL"]
SERVER = os.environ["UNTIS_SERVER"]

session = requests.Session()

# Login
login_url = f"https://{SERVER}/WebUntis/j_spring_security_check"
session.post(login_url, data={
    "school": SCHOOL,
    "j_username": USERNAME,
    "j_password": PASSWORD
})

# Example timetable fetch (simplified placeholder)
timetable_url = f"https://{SERVER}/WebUntis/api/public/timetable/weekly/data"
response = session.get(timetable_url)

calendar = Calendar()

event = Event()
event.add('summary', 'Untis Sync Active')
event.add('dtstart', datetime.now())
event.add('dtend', datetime.now())
calendar.add_component(event)

with open("calendar.ics", "wb") as f:
    f.write(calendar.to_ical())
