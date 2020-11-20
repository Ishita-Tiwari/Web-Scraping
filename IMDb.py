import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


name = []
genre = []
rating = []
duration = []

ini_url = 'https://www.imdb.com/list/ls000021660/?sort=list_order,asc&st_dt=&mode=detail&page='
for i in range(1, 4):
    my_url = ini_url + str(i)

    #opening up connection, grabbing the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    #gets each product
    containers = page_soup.findAll("div", {"class": "lister-item-content"})

    for container in containers:
        ##gets all the movie names
        name.append(container.h3.a.text)

        ##gets the genre
        spn_gnr = container.findAll("span", {"class": "genre"})
        
        if len(spn_gnr) == 0:
            genre.append([])
        else:
            genre.append(spn_gnr[0].text.strip().split(', '))

        ##gets the number of stars
        spn_rtng = container.findAll("span", {"class": "ipl-rating-star__rating"})
        if len(spn_rtng) == 0:
            rating.append('none')
        else:
            for rtng in spn_rtng:
                rating.append(rtng.text)
                break
##        print()


    ##gets the duration
    spn_dur = page_soup.findAll("span", {"class": "runtime"})
    for dur in spn_dur:
        duration.append(dur.text.strip())

for i in range(len(name)):
    print("name: ", name[i])
    print("genre: ", *genre[i])
    print("duration: ", duration[i])
    print("stars: ", rating[i])
    print()
