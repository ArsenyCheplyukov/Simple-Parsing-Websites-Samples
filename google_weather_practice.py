from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests

f = open("current_in_Mstislavl.txt", "w")

res = requests.get("https://www.worldweatheronline.com/mstislavl-weather/minsk/by.aspx")
res.raise_for_status()
page_soup = soup(res.text, "html.parser")

temperature = page_soup.findAll('span', {'class': 'display-4'})
staff = page_soup.findAll('dd', {'class': 'col-sm-7'})
names_of_staff = page_soup.findAll('dt', {'class' : 'col-sm-5'})

f.write("Current situation in Mstislavl is : " + "\n")
if len(temperature):
    print("Temperature is : " + temperature[0].getText() + "\n")
    f.write("Temperature : " + temperature[0].getText() + "\n")

for i in range(len(names_of_staff)):
    print(names_of_staff[i].getText())
    print(staff[i].getText())
    f.write(names_of_staff[i].getText() + " : " + staff[i].getText() + "\n")