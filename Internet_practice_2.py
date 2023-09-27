import requests, bs4
response = requests.get('https://learncodeonline.in')
soup = bs4.BeautifulSoup(response.text, 'lxml')
title = soup.select('title')
print("Title is : " + title[0].getText() + "\n")