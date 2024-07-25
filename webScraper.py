import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.bbc.com/news"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

articles = soup.find_all("div", class_="app")

headlines = soup.find_all("h2")

for headline in headlines:
    print(headline.text, "\n", end="\r")
    time.sleep(1)
