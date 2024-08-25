import requests
from bs4 import BeautifulSoup
import time


def fetch_and_display_headlines(url="https://www.bbc.com/news", delay=2):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")

        headlines = soup.find_all("h2")

        for headline in headlines:
            print(headline.text.strip(), "\n", end="\r")
            time.sleep(delay)
            
            

        return headlines

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    return []


def save_headlines(headlines):

    file_name = "webscraper.txt"

    with open(file_name, "a") as file:
        for headline in headlines:
            file.write(headline.text.strip() + "\n")


def main():

    headlines = fetch_and_display_headlines()
    save_headlines(headlines)


if __name__ == "__main__":

    main()
