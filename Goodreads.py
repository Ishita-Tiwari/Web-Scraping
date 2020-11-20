import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

name = []
rating = []
num_rating = []

my_url = 'https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

#gets each product
containers = page_soup.findAll("tr", {"itemtype": "http://schema.org/Book"})

print(len(containers))

for container in containers:

    a_name = container.a["title"]
    name.append(a_name)

    spn_star = container.find("span", {"class": "minirating"}).text.strip().split()
    ind = 0
    star = spn_star[ind]

    ##the text in rating field may vary
    if star.replace('.', '').isnumeric() == False:
        for ele in range(len(spn_star)):
            if spn_star[ele].replace('.', '').isnumeric():
                ind = ele
                break
    ind2 = ind + 4
    num = spn_star[ind2]
    rating.append(star)
    num_rating.append(num)
    

##displaying the data extracted from this page
for i in range(len(name)):
    print("name: ", name[i])
    print("average rating: ", rating[i])
    print("number of ratings: ", num_rating[i])
    print()
