#!/usr/bin/env Python3

# Web scraping script for fun

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a")
        for link in links:
            print(link.get("href"))
    else:
        print("Failed to retrieve the web page.")

def main():
    url = input("Enter the URL of the website you want to scrape: ")
    scrape_website(url)

if __name__ == "__main__":
    main()