import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

name = []
artist = []
price = []

my_url = 'https://bestofbharat.com/product-tag/vintage/'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

#gets the product section
content = page_soup.findAll("ul", {"class": "products columns-3"})
containers = content[0].findAll("li", {})


for container in containers:
    ##get the name of the product
    name.append(container.h2.text)

    ##get the name of the artist
    p_title = container.findAll("p", {"class": "customtitle yes"})
    if len(p_title) == 0:
        artist.append("Not Specified")
    else:
        title = p_title[0]
        nm_art = title.findAll("a", {})[-1]
        artist.append(nm_art.text)

    ##get the price
    price.append(container.bdi.text)


for i in range(len(name)):
    print("name: ", name[i])
    print("artist: ", artist[i])
    print("prices starting from: ", price[i])
    print()
