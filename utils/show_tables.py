import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')
c = conn.cursor()

# Query the sqlite_master table to get all tables
c.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all the results
tables = c.fetchall()

# Print all table names
for table in tables:
    print(table[0])

# Close the connection
conn.close()

