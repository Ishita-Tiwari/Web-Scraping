import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import cv2
import numpy as np

my_url = 'https://www.scoopwhoop.com/Khaled-Hosseini-Quotes/'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

#gets the quote section
containers = page_soup.findAll("div", {"class": "article-body"})


#this page has all the quotes in image format
all_img = containers[0].findAll("img", {})

for imgs in all_img:
    each_quote = imgs["src"]
    print(each_quote)

    #displaying all the images with the help of opencv.
    #use: extracting text from image and analysing
    url_response = uReq(each_quote)
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)
    img = cv2.resize(img, (400, 500))
    cv2.imshow('URL Image', img)
    cv2.waitKey()

cv2. destroyAllWindows()
