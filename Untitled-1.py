
import sqlite3

# Connect to the database
connection = sqlite3.connect('your_database.db')
cursor = connection.cursor()

# Execute the SQL query
cursor.execute("SELECT first_name || ' ' || last_name AS FullName FROM employees")

# Fetch and print the results
results = cursor.fetchall()
for row in results:
	print(row)

# Close the connection
connection.close()
