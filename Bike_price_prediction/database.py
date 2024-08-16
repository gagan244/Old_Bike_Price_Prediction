import sqlite3

# Establish a connection to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('bikedata.db')

# Define the SQL query to create the table
query_to_create_table = """
CREATE TABLE IF NOT EXISTS BikeDetails (
    owner INT,
    brand TEXT,
    kms_driven INT,
    power INT,
    age INT,
    predicted_price INT
);
"""

# Create a cursor object to interact with the database
cur = conn.cursor()

# Execute the SQL query to create the table
cur.execute(query_to_create_table)

# Commit the transaction (not strictly necessary for table creation, but good practice)
conn.commit()

# Print a success message
print("Your database and table are created")

# Close the cursor and connection
cur.close()
conn.close()
