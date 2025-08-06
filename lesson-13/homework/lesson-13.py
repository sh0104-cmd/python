from datetime import datetime
from dateutil.relativedelta import relativedelta

birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
today = datetime.today()

age = relativedelta(today, birthdate)
print(f"You are {age.years} years, {age.months} months, and {age.days} days old.")

birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
today = datetime.today()

next_birthday = birthdate.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_remaining = (next_birthday - today).days
print(f"Days until next birthday: {days_remaining}")

current_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
duration_hours = int(input("Meeting duration hours: "))
duration_minutes = int(input("Meeting duration minutes: "))

current_time = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
meeting_end = current_time + relativedelta(hours=duration_hours, minutes=duration_minutes)

print(f"Meeting will end at: {meeting_end.strftime('%Y-%m-%d %H:%M')}")

from pytz import timezone, all_timezones

date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
source_tz = input("Enter your current timezone (e.g., US/Eastern): ")
target_tz = input("Enter target timezone (e.g., Asia/Tokyo): ")

dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
src_zone = timezone(source_tz)
tgt_zone = timezone(target_tz)

src_dt = src_zone.localize(dt)
converted_dt = src_dt.astimezone(tgt_zone)

print(f"In {target_tz}, it will be: {converted_dt.strftime('%Y-%m-%d %H:%M')}")

import time

target_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
target_dt = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    if now >= target_dt:
        print("Countdown complete!")
        break
    remaining = target_dt - now
    print(f"Time remaining: {remaining}", end='\r')
    time.sleep(1)

import re

email = input("Enter an email address: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")

phone = input("Enter a 10-digit phone number: ")
digits = ''.join(filter(str.isdigit, phone))

if len(digits) == 10:
    formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    print(f"Formatted Phone Number: {formatted}")
else:
    print("Invalid phone number length.")

import re

password = input("Enter a password: ")

length = len(password) >= 8
uppercase = re.search(r'[A-Z]', password)
lowercase = re.search(r'[a-z]', password)
digit = re.search(r'\d', password)

if all([length, uppercase, lowercase, digit]):
    print("Password is strong.")
else:
    print("Weak password. Requirements:")
    if not length: print("- At least 8 characters")
    if not uppercase: print("- At least one uppercase letter")
    if not lowercase: print("- At least one lowercase letter")
    if not digit: print("- At least one digit")

text = input("Enter some text: ")
word = input("Enter the word to search: ")

positions = []
start = 0

while True:
    idx = text.lower().find(word.lower(), start)
    if idx == -1:
        break
    positions.append(idx)
    start = idx + 1

if positions:
    print(f"'{word}' found at positions: {positions}")
else:
    print(f"'{word}' not found.")

import re

text = input("Enter a text with dates (e.g. 'We met on 2023-12-01 or 01/12/2023.'): ")
date_patterns = [
    r'\b\d{4}-\d{2}-\d{2}\b',  # YYYY-MM-DD
    r'\b\d{2}/\d{2}/\d{4}\b',  # DD/MM/YYYY or MM/DD/YYYY
]

dates = []
for pattern in date_patterns:
    matches = re.findall(pattern, text)
    dates.extend(matches)

if dates:
    print("Dates found:", dates)
else:
    print("No dates found.")
