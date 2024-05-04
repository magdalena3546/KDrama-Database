import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from scipy.stats import f_oneway

load_dotenv()
engine = create_engine(os.getenv("DB_LINK"))
query = 'SELECT * FROM kdramadata'

df = pd.read_sql(query, con=engine)

df['genre'] = df['genre'].str.split(', ')

df = df.explode('genre')

df['genre'] = df['genre'].str.strip()

# Analyzing average ratings by genre to determine the most highly-rated genres.
average_ratings = df.groupby('genre')['rating'].mean().sort_values(ascending=False)

print(average_ratings)

# ANOVA 
grouped_data = [df[df['genre'] == genre]['rating'] for genre in df['genre'].unique()] 
f_statistic, p_value = f_oneway(*grouped_data)

print('f_statistic:', f_statistic)
print('p_value:', p_value)

engine.dispose()