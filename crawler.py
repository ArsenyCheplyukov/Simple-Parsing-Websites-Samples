import requests
import bs4

f = open("Wikipedia_data.txt", "w",  encoding='utf-8')
response = requests.get("https://en.wikipedia.org/wiki/Macrolepiota_albuminosa")

if response is not None:
    page = bs4.BeautifulSoup(response.text, 'html.parser')
    
    title = page.select("#firstHeading")[0].text
    paragraphs = page.select("p")
    
    print(title)
    intro = '\n'.join([ para.text for para in paragraphs[0:10]])
    print (intro)
    
    f.write(title + "\n")
    f.write(intro + "\n")

f.close()  # Close the file
