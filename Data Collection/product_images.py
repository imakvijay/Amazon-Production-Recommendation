import requests
import sqlite3
from os import listdir

# DB connection for loading data
db_connection = sqlite3.connect('Data/Database/job_database.db')
db_cursor = db_connection.cursor()

# Links to be collected
query = f"""SELECT img_src FROM product_info"""
db_cursor.execute(query)
links_list = db_cursor.fetchall()

# Images already collected
collected_images = listdir('Data/Images')

for link in links_list:
    # Extract the name of the image
    name = link[0].split('/')[-1]
    # Check if image already exists
    if name in collected_images:
        continue
    else:
        path = f'Data/Images/{name}'
        img_data = requests.get(link[0]).content
        with open(path, 'wb') as file:
            file.write(img_data)


