import csv
import re
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
# def timeToMinutes(time):
#     time = time.strip()
#     time = re.sub(r'(\d+)\s+(hr\.|min\.)', r'\1\2', time)
#     parts = time.split()
#     minutes = 0
#     for part in parts:
#         if 'hr.' in part:
#             hours = part.replace('hr.', '')
#             if hours.isdigit():
#                 minutes += int(hours) * 60
#         elif 'min.' in part:
#             minutes_str = part.replace('min.', '')
#             if minutes_str.isdigit(): 
#                 minutes += int(minutes_str)
#     print(minutes)
#     return minutes

# with open('./csv/kdrama.csv', 'r', encoding="utf-8") as csvfile:
#     kdramaDB = csv.DictReader(csvfile)
#     converted_data = []
#     fieldnames = kdramaDB.fieldnames
#     for row in kdramaDB:
#         minutes = timeToMinutes(row['Duration'])
#         row['Duration'] = minutes
#         converted_data.append(row)
        
# with open('./csv/kdrama.csv', 'w', encoding="utf-8") as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(converted_data)


engine = create_engine('mysql+mysqlconnector://root:Shuri3546#@localhost:3306/kdramaDB')
query = 'SELECT * FROM kdramadata'

df = pd.read_sql(query, con=engine)

# df['genre'] = df['genre'].str.split(', ')

# df = df.explode('genre')

# df['genre'].str.strip()

# new = pd.Series([])
# new = df['genre'].str.strip()
# df['genre'] = new

# average_ratings = df.groupby('genre')['rating'].mean().sort_values(ascending=False)
# print(average_ratings)


# engine.dispose()
# Podział wartości w kolumnie 'genre' na listy
df['genre'] = df['genre'].str.split(', ')

# Eksplozja danych na podstawie kolumny 'genre'
df = df.explode('genre')

# Usunięcie nadmiarowych białych znaków z wartości w kolumnie 'genre'
df['genre'] = df['genre'].str.strip()

# Obliczenie średniej oceny dla każdego gatunku
average_ratings = df.groupby('genre')['rating'].mean().sort_values(ascending=False)

# Wyświetlenie wyników
print(average_ratings)

# Zamknięcie połączenia z bazą danych
engine.dispose()