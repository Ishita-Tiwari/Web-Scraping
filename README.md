# Web Scraping

Welcome to yet another repository. Here you can find a few sample code snippets if you wish to get started with scraping websites. If you do not clearly understand the use of web scraping, check out this [blog](https://www.captaindata.co/blog/11-reasons-why-use-web-scraping). Once you get a hang of it and understand the basics, you will be able to scrape pretty much any website you wish to. 

<table margin="none">
  <tr>
    <td>
      <img src="https://user-images.githubusercontent.com/51106967/99793940-67ded680-2b4f-11eb-8ca2-c534b1605cd8.gif" alt="gif" width="5000px">
    </td>
    <td>
      This is essentially what happens when we scrape a website. We get the raw HTML of that page. This is our scattered data and we extract what is useful to us from here. We put the newly found information together in order to perform other tasks. In this repository, we are doing the same with the following websites: <br><br>
      <a href="https://www.imdb.com/list/ls000021660/?st_dt=&mode=detail&page=1" target="_blank"><img src = "https://user-images.githubusercontent.com/51106967/99798997-f6efec80-2b57-11eb-9886-c03396956b6a.jpeg" width="90px"></a>
      <a href="https://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century" target="_blank"><img src="https://user-images.githubusercontent.com/51106967/99821859-8a391a00-2b78-11eb-8b45-a235c9cf76bc.png" width="115px" margin-left="50px"></a>
      <a href="https://www.scoopwhoop.com/Khaled-Hosseini-Quotes/" target="_blank"><img src="https://user-images.githubusercontent.com/51106967/99881271-bb7c1d80-2c3e-11eb-8a8e-279eb7db29bd.png" width="55px" margin-left="50px"></a>
    </td>
  </tr>
</table>



##### Note: Before getting started with this, make sure to refer the robots.txt file. Each website defines its policies related to crawling in this text file.


### Goodreads
Here is the execution of [Goodreads.py](https://github.com/Ishita-Tiwari/Web-Scraping/blob/main/Goodreads.py). It takes a couple of seconds to display the data which is essentially because it has to download the entire content first.


<p align="center">
  <img src="https://user-images.githubusercontent.com/51106967/99874048-98d01180-2c0a-11eb-893d-3c52f79a3229.gif" alt="sr">
</p>


<br>

### ScoopWhoop
This page displays content in the form of images. We extract the image url from the HTML and display the image with the help of opencv. These images can be further processed in order to use the written text present in the image. This is the output of [Scoopwhoop.py](https://github.com/Ishita-Tiwari/Web-Scraping/blob/main/Scoopwhoop.py)

<p align="center">
  <img src="https://user-images.githubusercontent.com/51106967/99881379-760c2000-2c3f-11eb-8df7-7094ad9221ec.gif" alt="sr">
</p>
