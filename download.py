import csv
import json
from bs4 import BeautifulSoup
from pathlib import Path
from loguru import logger
import requests
from concurrent.futures import ThreadPoolExecutor

logger.add("main.log")


def download(t):
    url = t[0]
    path = Path(t[1])
    log_str = t[2]
    logger.info(f"Downloading {log_str}")

    if not path.exists():
        res = requests.get(url)
        if res.status_code == 200:
            path.write_bytes(res.content)
        else:
            logger.error(f"Status code {res.status_code} {log_str}")


def create_tasks():
    tasks = []
    with open("isbns.txt", "r") as f:
        isbns = f.readlines()
    total_isbns = len(isbns)

    for index, _isbn in enumerate(isbns, 1):
        isbn = _isbn.strip()

        url = f"https://www.greenlightbookstore.com/book/{isbn}"
        filepath = f"books/{isbn}.html"

        tasks.append([url, filepath, f"{index}/{total_isbns}", isbn])

    return tasks


def parse_book(t):
    url = t[0]
    path = Path(t[1])
    log_str = t[2]

    logger.info(f"Parsing {log_str}")

    with open(path) as f:
        soup = BeautifulSoup(f, "lxml")

    product_details_text = soup.find(
        "fieldset", {"id": "aba-product-details-fieldset"}
    ).text
    product_details = {}
    for line in product_details_text.splitlines():
        if ": " in line:
            key = line.split(":")[0]
            val = line.split(": ")[1]
            product_details[key] = val
    categories_elm = soup.find(
        "fieldset", {"class": "collapsible abaproduct-related-editions"}
    )
    categories = []
    if categories_elm is not None:
        for li_elm in categories_elm.find_all("li"):
            categories.append(li_elm.text)

    return categories, product_details


def main():
    with open("vegan_books.csv", "w") as fw:
        writer = csv.writer(fw)
        writer.writerow(
            [
                "ISBN-10",
                "Series",
                "Publication Date",
                "ISBN",
                "Large Print",
                "Publisher",
                "Pages",
                "Language",
            ]
        )
        tasks = create_tasks()
        # with ThreadPoolExecutor(10) as pool:
        #     pool.map(download,tasks)

        for t in tasks:
            categories, product_details = parse_book(t)
            out_row = {
                "ISBN-10": "",
                "Series": "",
                "Publication Date": "",
                "ISBN": "",
                "Large Print": "",
                "Publisher": "",
                "Pages": "",
                "Language": "",
                "categories":""
            }
            for k, v in product_details.items():
                out_row[k] = v
            out = list(out_row.values())
            out.extend(categories)
            writer.writerow(out)


# if __name__ == "__main__":
#     main()
