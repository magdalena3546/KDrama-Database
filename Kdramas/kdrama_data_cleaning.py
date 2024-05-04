import csv
import re

def timeToMinutes(time):
    time = time.strip()
    time = re.sub(r'(\d+)\s+(hr\.|min\.)', r'\1\2', time)
    parts = time.split()
    minutes = 0
    for part in parts:
        if 'hr.' in part:
            hours = part.replace('hr.', '')
            if hours.isdigit():
                minutes += int(hours) * 60
        elif 'min.' in part:
            minutes_str = part.replace('min.', '')
            if minutes_str.isdigit(): 
                minutes += int(minutes_str)
    print(minutes)
    return minutes

with open('./csv/kdrama.csv', 'r', encoding="utf-8") as csvfile:
    kdramaDB = csv.DictReader(csvfile)
    converted_data = []
    fieldnames = kdramaDB.fieldnames
    for row in kdramaDB:
        minutes = timeToMinutes(row['Duration'])
        row['Duration'] = minutes
        converted_data.append(row)
        
with open('./csv/kdrama.csv', 'w', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(converted_data)