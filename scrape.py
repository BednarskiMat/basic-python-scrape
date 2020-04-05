import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

headers = {"Accept-Language": "en-US, en;q=0.5"}
url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"
results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, "html.parser")

#print(soup.prettify())


# initialize empty list for data storage
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []
movie_div = soup.find_all('div', class_= 'lister-item mode-advanced')


#for loop
for container in movie_div:
    name = container.h3.a.text
    titles.append(name)

    year = container.h3.find('span', class_='lister-item-year').text
    years.append(year)

    runtime = container.p.find('span', class_='runtime').text if container.p.find('span', class_='runtime').text else '-'
    time.append(runtime)

    imdb = float(container.strong.text)
    imdb_ratings.append(imdb)

    m_score = container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-'
    metascores.append(m_score)

    # there are two NV containers, grab both of them as they hold both the votes and the grosses
    nv = container.find_all('span', attrs={'name': 'nv'})

    # filter nv for votes
    vote = nv[0].text
    votes.append(vote)

    # filter nv for gross
    grosses = nv[1].text if len(nv) > 1 else '-'
    us_gross.append(grosses)

#for i in range(len(titles)):
  #  print(f"Title: {titles[i]}, Year: {years[i]}, Time:{time[i]}, Rating: {imdb_ratings[i]}, Earnings: {us_gross[i]}")

movies = pd.DataFrame({
    'movie': titles,
    'year': years,
    'timeMin': time,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes,
    'us_grossMillions': us_gross,
})
print(movies)
movies.to_csv('movies.csv')


