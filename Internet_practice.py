from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# URL to web scrape from
page_url = "http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=GTX&bop=And&Page=1&PageSize=36&order=BESTMATCH"

# Open the connection and download the HTML page from the URL
uClient = urlopen(page_url)

# Parse HTML into a soup data structure
page_soup = soup(uClient, "html.parser")
uClient.close()

# Find each product from the store page
containers = page_soup.findAll("div", {"class": "item-container"})

# Name the output file to write to the local disk
out_filename = "graphics_cards.csv"

# Open the file and write headers
with open(out_filename, "w") as f:
    headers = "brand,product_name,shipping\n"
    f.write(headers)

    # Loop over each product and grab attributes
    for container in containers:
        make_rating_sp = container.div.select("a")
        brand = make_rating_sp[0].img["title"].title()
        product_name = container.div.select("a")[2].text
        shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

        # Print the dataset
        print("Brand:", brand)
        print("Product Name:", product_name)
        print("Shipping:", shipping)

        # Write the dataset to the file
        f.write(f"{brand}, {product_name.replace(',', '|')}, {shipping}\n")

print("Scraping complete. Data saved to", out_filename)
