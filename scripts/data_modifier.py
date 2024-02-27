##data_modifier.py

import sqlite3
import traceback
from flask import Flask
from collections import namedtuple #import if you want to set up tupple structure

app = Flask(__name__)

User = namedtuple('User', ['id', 'listing_url', 'name', 'country', 'city', 
                           'bedrooms', 'bathrooms', 'beds', 'accommodates', 'review_score'])

def see_highest_ranking_data(country):
    try:
        # Connect to the database
        conn = sqlite3.connect('instance/Users.sqlite3')
        cursor = conn.cursor()

        # Execute SQL query to select all rows from the Users table
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()

        conn.close()

        # Convert each row tuple into an instance of the User named tuple
        users = [User(*row) for row in rows] # needed if want to use tuple structure and not indexes to filter

        # To filter rows based on ranking and country. Retrieval based on indexes
        # filtered_rows = [row for row in rows if row[-1] > 85 and row[3] == country]

        # To filter rows based on ranking and country. Retrieval based on tuple schema and not indexes
        filtered_rows = [user for user in users if user.review_score > 85 and user.country == country] 

        return filtered_rows

    except Exception as e:
        print("Exception during sqlite db manipulation:", e)
        print(traceback.format_exc())
        return[]
