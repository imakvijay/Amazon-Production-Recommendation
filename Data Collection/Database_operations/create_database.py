import sqlite3

# Creating/Connecting the db
db_connection = sqlite3.connect('../Data/Database/job_database.db')

# Opening a cursor
db_cursor = db_connection.cursor()

# Create table transaction_links to start the scraping
db_cursor.execute("""CREATE TABLE transaction_links(
                    link text,
                    type text,
                    status text,
                    date date,
                    time time)
                    """)
