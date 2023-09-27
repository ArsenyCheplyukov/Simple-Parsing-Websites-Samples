# RETURNS SOME SHIT

from bs4 import BeautifulSoup as soup
import requests

wikipedia = requests.get('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States')
page_soup = soup(wikipedia.text, 'html.parser')

# Print the title of the page
title = page_soup.title.text
print('Title:', title)

# Print the first paragraph
first_paragraph = page_soup.p.text
print('First Paragraph:', first_paragraph)

# Print all the links in the page
links = page_soup.find_all('a')
print('Links:')
for link in links:
    print(link.get('href'))

# Print all the presidents from the table
table = page_soup.find('table', {'class': 'wikitable'})
presidents = table.find_all('th', {'scope': 'row'})
print('List of Presidents:')
for president in presidents:
    print(president.text)
