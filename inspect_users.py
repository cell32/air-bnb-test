import sqlite3

from flask import json

# Connect to the database
conn = sqlite3.connect('instance/Users.sqlite3')
cursor = conn.cursor()

# Specify the city you want to filter by
#city_to_filter = "Brooklyn"

# Execute SQL query to select all rows from the Users table
cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()

# Print only the rows where the rating is greater than 85
for row in rows:
    rating = row[-1]  # Assuming the rating is the last item in each row
    if rating > 85:
        print(row)    

# Close the connection
conn.close()
