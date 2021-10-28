# Import required libraries
from selenium import webdriver
import time
from datetime import datetime
import sqlite3

# Initializing web driver
driver = webdriver.Chrome('chromedriver.exe')

# DB connection for loading data
db_connection = sqlite3.connect('Data/Database/job_database.db')
db_cursor = db_connection.cursor()

types_list = ['Hoodie/Sweatshirt', 'Jeans', 'Pants', 'Shorts', 'Sleepwear', 'Socks',
              'Suits/Blazers', 'Sweater', 'Leather Jacket', 'Raincoat']

for product_type in types_list:

    print(f'Collecting {product_type} type products')
    query = f"""SELECT count(*) FROM transaction_links
                        WHERE status ='Collected' AND type='{product_type}'"""
    db_cursor.execute(query)
    # Counter for storing number of links extracted
    extracted_count = db_cursor.fetchall()[0][0]

    # Collect only 100 products for each type
    if extracted_count >= 100:
        continue

    query = f"""SELECT link FROM transaction_links
                        WHERE status ='Not collected' AND type='{product_type}'"""
    # Extracting the links that are not collected from DB
    db_cursor.execute(query)
    links_list = db_cursor.fetchall()

    for link in links_list:
        driver.get(link[0])
        time.sleep(5)
        try:
            if extracted_count >= 100:
                print('Collected 100 records')
                break

            product_name = driver.find_element_by_xpath('//span[@id="productTitle"]').text
            rating = driver.find_element_by_xpath('//span[@data-hook="rating-out-of-text"]').text
            no_of_rating = driver.find_element_by_xpath('//span[@class="a-size-base a-color-secondary"]').text
            price = driver.find_element_by_xpath('//span[contains(@class,"a-size-medium")]').text
            # Available sizes
            size_available = ''
            sizes = driver.find_elements_by_xpath('//select[@name="dropdown_selected_size_name"]//option')
            for size in sizes:
                size_available += size.text
                size_available += ', '

            # Available colors
            color_available = ''
            colors = driver.find_elements_by_xpath('//li[contains(@id,"color_name")]//img')
            for color in colors:
                color_available += color.get_attribute('alt')
                color_available += ', '

            brand = driver.find_element_by_xpath('//div[@class="a-section a-spacing-none"]').text
            description = driver.find_element_by_xpath('//ul[@class="a-unordered-list a-vertical a-spacing-mini"]').text
            img_src = driver.find_element_by_xpath('//span[@data-action="main-image-click"]//img').get_attribute('src')
            url = link[0]

            # Time_Now
            dt_now = datetime.now()
            date_now = dt_now.strftime("%m/%d/%Y")
            time_now = dt_now.strftime("%H:%M:%S")

            query = f"""INSERT INTO product_info 
                        VALUES('{product_name}','{rating}','{no_of_rating}','{price}','{color_available}',
                        '{size_available}','{brand}','{description}', '{img_src}','{date_now}','{time_now}',
                        '{url}', '{product_type}')"""

            db_cursor.execute(query)
            db_connection.commit()
            extracted_count += 1

            query = f"""UPDATE transaction_links
                    SET status ='Collected'
                    where link = '{url}'"""

            db_cursor.execute(query)
            db_connection.commit()

        except:
            url = link[0]
            query = f"""UPDATE transaction_links
                                SET status ='Error thrown'
                                where link = '{url}'"""

            db_cursor.execute(query)
            db_connection.commit()

driver.close()