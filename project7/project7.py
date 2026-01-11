import requests
from bs4 import BeautifulSoup
bs4 = BeautifulSoup

base_url ="https://xkcd.com"
url = "https://xkcd.com/1"

while "#" not in url:

    #part 1 request and soupify
    #requests the web page

    response = requests.get(url)


    #print(response.content)

    #parse the page to make it easy to use
    soup = bs4(response.content, "html.parser")
    # print(soup)

    #part 2 find the url of the image
    img_element = soup.select("#comic img")[0]
    img_src =  img_element["src"]
    img_src = "http:" + str(img_src)

    img_name = img_src.split("/")[-1]

    #get the name of the file

    #part 3 download the comic
    #use the with open function to save the fie
    response = requests.get(img_src)
    with open("comics/" + img_name,"wb") as file:
        file.write(response.content)
        
    #part 4 find the next one
    next_a = (soup.select(".comicNav a[rel=next]"))[0]
    next_href = next_a["href"]
    url = base_url + next_href 
    print(url)