import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.bbc.com/news"

response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.text, "lxml")
#print(soup)
