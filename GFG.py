import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

##stores the relevat questions
q = []
link = []

my_url = 'https://www.geeksforgeeks.org/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

#gets each list
containers = page_soup.findAll("ol", {})

for container in containers:
    all_li = container.findAll("li", {})
    for nm in all_li:
        q.append(nm.a.text.strip())
        link.append(nm.a['href'])

ind = q.index('Difficulty-wise ordered Coding questions for Interview and Competitive Programming')
q = q[: ind][:]

print(len(q))
for i in range(len(q)):
    print(q[i])
    print(link[i])
    print('\n\n')
    
