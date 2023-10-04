from pathlib import Path
import tqdm
from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor
from loguru import logger


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


def create_dl_tasks():
    tasks = []
    for i in range(1, 672):
        url = f"https://www.greenlightbookstore.com/search/site/vegan?page={i}"
        filepath = f"html-pages/page_{i}.html"
        tasks.append([url, filepath, f"{i}/672"])
    return tasks


def main():
    tasks = create_dl_tasks()
    with ThreadPoolExecutor(10) as pool:
        pool.map(download,tasks)


main()
