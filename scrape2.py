#solo application from tutorial used in helper.py

import requests
from requests import get
from bs4 import BeautifulSoup




def scrape():
    headers = {"Accept-Language": "en-US, en;q=0.5"}
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")

    prices = []
    descriptions = []

    product_div = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')

    for item in product_div:
        price = item.h4.text
        prices.append(price)

        description = item.find("p", class_='description').text
        descriptions.append(description)

    return prices, descriptions


