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


# Function to load collected data to the DB
def load_links(product_links, product_type):
    status = 'Not collected'

    # Loop through the list and load them into DB
    for url_product in product_links:
        dt_now = datetime.now()
        date_nw = dt_now.strftime("%m/%d/%Y")
        time_nw = dt_now.strftime("%H:%M:%S")
        query = f"INSERT INTO transaction_links (link, type, status, date, time)\
                    VALUES ('{url_product}','{product_type}', '{status}', '{date_nw}', '{time_nw}')"
        db_cursor.execute(query)

    db_connection.commit()


with open('product_types_links.txt') as file:
    link_type_list = file.read().splitlines()

for link_type in link_type_list:
    link = link_type.split(', ')[0]
    product_type = link_type.split(', ')[1]

    # Load amazon first page
    driver.get(link)

    # Extract total number of result pages
    page_str = driver.find_element_by_xpath('(//ul[@class="a-pagination"]//li[@class="a-disabled"])[last()]').text
    total_page = int(page_str)

    page = 1
    # Loop through pages and collect the links
    while page <= total_page:
        product_links = []
        link_xpath = '//div[@data-component-type="s-search-result"]//a[@class="a-link-normal a-text-normal"]'
        products = driver.find_elements_by_xpath(link_xpath)
        for product in products:
            product_links.append(product.get_attribute('href'))

        # Load the collected data of each page to DB
        load_links(product_links, product_type)
        print(f'{page} page of {product_type}')
        # Check whether current page is last page or not
        if page != total_page and page < 21:
            # click the next page button
            driver.find_element_by_xpath('//li[@class="a-last"]').click()
            page += 1
            time.sleep(5)
        else:
            break


driver.close()


