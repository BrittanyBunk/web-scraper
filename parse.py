from bs4 import BeautifulSoup
import csv


a=0

def parse_page(filepath):
    global a
    pages = []
    with open(filepath, "r") as f:
        soup = BeautifulSoup(f, "lxml")
    book_list = soup.find("ol", {"class": "search-results apachesolr_search-results"})
    for li_elm in book_list.find_all("li", {"class": "search-result"}):
        # print(li_elm)
        title = li_elm.find("a").text
        try:
            author = li_elm.find_all("div")[1].find("p").find("a").text
        except AttributeError as e:
            a+=1
            continue
        isbn_13 = li_elm.find("a").attrs["href"].split("/")[-1]
        image_url = (
            li_elm.find("div", {"class": "abaproduct-image"}).find("img").attrs["src"]
        )
        pages.append(
            {
                "title": title,
                "author": author,
                "isbn_13": isbn_13,
                "image_url": image_url,
            }
        )

    return pages

rows=[]

with open("scrape.csv","w") as fw:
    writer = csv.DictWriter(fw,['title','author','isbn_13','image_url'])
    writer.writeheader()
    for i in range(0, 672):
        filepath = f'html-pages/page_{i}.html'
        print(f"{i}/672")
        writer.writerows(parse_page(filepath))
        

print(a)