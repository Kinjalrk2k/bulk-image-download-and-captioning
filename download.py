# bulk download images

IMAGES_DIR = "images"
KEYWORD = "simple system design flowcharts"
LIMIT = 10

MAX_WORKERS = 3

from simple_image_download import simple_image_download as simp
import os
import requests
from concurrent.futures import ThreadPoolExecutor

response = simp.simple_image_download
urls = response().urls(KEYWORD, LIMIT)

if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)


def download(i, url):
    try:
        print(i, "->", url)
        r = requests.get(url, allow_redirects=True)
        filename = f"{i+1}.png"
        open(os.path.join(IMAGES_DIR, filename), "wb").write(r.content)
    except Exception as e:
        print(e)


with ThreadPoolExecutor(MAX_WORKERS) as executor:
    for i, url in enumerate(urls):
        executor.submit(download, i, url)
