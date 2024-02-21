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

# Filter rows based on the nested JSON structure
#filtered_rows = [row for row in rows if json.loads(row[1])['item']['address']['suburb'] == 'Laranjeiras']


# Print the results
for row in rows:
    print(row)

# Close the connection
conn.close()
