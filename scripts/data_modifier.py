##data_modifier.py

import sqlite3
import traceback
from flask import Flask

app = Flask(__name__)

def see_highest_ranking_data():
    try:


        # Connect to the database
        conn = sqlite3.connect('instance/Users.sqlite3')
        cursor = conn.cursor()

        # Specify the city you want to filter by
        #city_to_filter = "Brooklyn"

        # Execute SQL query to select all rows from the Users table
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()

        conn.close()

        # Print only the rows where the rating is greater than 85. This works only for tuples
        filtered_rows = [row for row in rows if row[-1] > 85] 

        return filtered_rows

    except Exception as e:
        print("Exception during sqlite db manipulation:", e)
        print(traceback.format_exc())
        return[]
