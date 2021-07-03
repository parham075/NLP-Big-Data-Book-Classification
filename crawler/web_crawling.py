import csv
import os
from csv import DictWriter
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
import selenium_helper as parse_helper
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()  # take environment variables from .env.

GOODREADS_USERNAME = os.getenv('GOODREADS_USERNAME')
GOODREADS_PASSWORD = os.getenv('GOODREADS_PASSWORD')

fieledNames = ['Title', 'Description', 'Category']


def csv_file_creator():
    with open('Data.csv', 'a', encoding='UTF8', newline='') as f:
        fieled_Name = ['Title', 'Description', 'Category']
        thewriter = csv.DictWriter(f, fieldnames=fieled_Name)
        thewriter.writeheader()
        f.close()


def Crawl_from_goodreads():
    url = 'https://www.goodreads.com/user/sign_in'

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % "1920,1080")
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)

    driver.get(url)
    driver.find_element_by_name("user[email]").send_keys(GOODREADS_USERNAME)
    driver.find_element_by_name("user[password]").send_keys(GOODREADS_PASSWORD)
    driver.find_element_by_name("next").click()
    print("loged in successfully")
    sleep(1)
    # driver.get("https://www.goodreads.com/search?page=%251&q=geners&qid=1zuFtmrnpl&search%5Bsource%5D=goodreads&search_type=books&tab=books")
    driver.get('https://www.goodreads.com/book/show/4033373-international-mathematical-congresses?random=true')
    category_str = ''
    list_category = []
    for page in range(1, 30000):
        description = ''
        category = ''
        title = ''
        if parse_helper.check_exists_by_id(driver, "description"):
            description = driver.find_element_by_id('description').text

        if parse_helper.check_exists_by_id(driver, "bookTitle"):
            title = driver.find_element_by_id("bookTitle").text

        if parse_helper.check_exists_by_class_name(driver, "elementList "):
            category = driver.find_element_by_class_name("elementList ").text
            category_str = str(category)
            list_category = category_str.split('\n')
            category = list_category[0]
            list_category = category.split(" >")
            category_str = str(list_category[0])

            if page % 50 == 0:
                print("page:", page, "th is crwaled sucessfully.")

        with open('Data.csv', 'a', newline='', encoding='utf-8') as f:
            Dict_writer = DictWriter(f, fieldnames=fieledNames)
            Dict_writer.writerow({'Title': title,
                                  'Description': description,
                                  'Category': category_str})
            f.close()
        driver.find_element_by_link_text("View another random book »").click()

    driver.close()


if __name__ == "__main__":
    csv_file_creator()
    Crawl_from_goodreads()
