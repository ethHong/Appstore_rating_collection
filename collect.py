from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# from fake_useragent import UserAgent
import time
import platform
import json

if platform.system() == "Windows":
    driverpath = os.getcwd() + "/chromedriver.exe"
else:
    driverpath = os.getcwd() + "/chromedriver"

options = webdriver.ChromeOptions()
"""def mock_user_agent():
    ua = UserAgent()

    working = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15"
    working_tail = "(" + working.split("(")[-1]
    random_head = ua.random.split("(")[0] + "(" + ua.random.split("(")[1]
    return random_head + working_tail

userAgent = mock_user_agent()
options.add_argument(f"user-agent={userAgent}")"""


options.add_argument("headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

"""def scroll():
    SCROLL_PAUSE_TIME = 2
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height"""


def scroll(how_long=100):
    SCROLL_PAUSE_TIME = 2
    # Get scroll height
    starttime = time.time()
    proceed = 0
    last_height = driver.execute_script("return document.body.scrollHeight")
    while proceed < how_long:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        endtime = time.time()
        proceed = endtime - starttime


with open("links.txt", "r") as f:
    links = [i.strip() for i in f.readlines()]


driver = driver = webdriver.Chrome(driverpath, chrome_options=options)


def get_rating(url, seconds=100):
    driver.get(url)
    driver.implicitly_wait(5)
    scroll(seconds)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    reviews = soup.find_all("div", {"class": "we-customer-review lockup"})
    collection = {}
    for i in range(0, len(reviews)):
        collection[i] = {}
        l = reviews[i]
        collection[i]["title"] = l.find(
            "h3",
            {"class": "we-truncate we-truncate--single-line we-customer-review__title"},
        ).text.strip()
        collection[i]["contents"] = l.find("div", {"class": "we-clamp"}).text
        collection[i]["rating"] = l.find(
            "figure",
            {
                "class": "we-star-rating we-customer-review__rating we-star-rating--large"
            },
        )["aria-label"]
        collection[i]["time"] = l.find("time")["datetime"]

    return collection


filename = input("Enter filename: ")
result = {}
for url in links:
    print("Collecting from {}...".format(url))
    temp = get_rating(url, seconds=100)
    result[url] = temp

with open(filename + ".json", "w") as f:
    json.dump(result, f, ensure_ascii=False, indent="\t")
