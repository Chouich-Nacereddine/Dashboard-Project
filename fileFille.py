import pandas as pd
import random
from datetime import datetime, timedelta 
import os

def generate_habit_data(start_date, days):
    data = []
    current_date = start_date
    for _ in range(days):
        row = {
            'Date': current_date.date(),
            'Instagram (mins)': random.randint(20, 100),
            'YouTube (mins)': random.randint(20, 100),
            'Video Games (mins)': random.randint(0, 120),  
            'Studies (mins)': random.randint(30, 240), 
            'Sports (mins)': random.randint(0, 120),
            'Family (mins)': random.randint(30, 180),
            'Worship (mins)': random.randint(30, 180),
            
        }
        data.append(row)
        current_date += timedelta(days=1)
    return data

start_date = datetime(2023, 1, 1) 
days = 365  
data = generate_habit_data(start_date, days)


df = pd.DataFrame(data)
os.chdir(r"C:\Users\nchouich\OneDrive - Capgemini\Bureau\Dashboard-Project")
df.to_excel('Data.xlsx', index=False) 