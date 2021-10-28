import sqlite3

# Creating/Connecting the db
db_connection = sqlite3.connect('../Data/Database/job_database.db')

# Opening a cursor
db_cursor = db_connection.cursor()

# Create table product_info to store the collected product data
db_cursor.execute("""CREATE TABLE product_info(
                    product_name text,
                    rating real,
                    no_of_rating text,
                    price text,
                    color_available text,
                    size_available text,
                    brand text,
                    description text,
                    img_src text,
                    date date,
                    time time,
                    link text,
                    type text)""")