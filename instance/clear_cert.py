import sqlite3

# Connect to the database
conn = sqlite3.connect('blockchain.db')
cursor = conn.cursor()

# Delete all data from the 'certificate' table
cursor.execute("DELETE FROM certificate;")

# Commit changes and close connection
conn.commit()
conn.close()

print("All data in 'certificate' table cleared!")
