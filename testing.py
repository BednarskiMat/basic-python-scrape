from scrape2 import scrape

info = scrape()
(prices, descriptions) = info


for i in range(len(descriptions)):
    print(f"Description: {descriptions[i]}, Price: {prices[i]}")

