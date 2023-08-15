# remove images with 0 bytes

IMAGES_DIR = "images"

import os
from PIL import Image

files = filter(
    lambda x: not x.startswith(".") and x.endswith(".png"),
    sorted(os.listdir(IMAGES_DIR)),
)

for i, file in enumerate(files):
    file_path = f"{IMAGES_DIR}/{file}"

    try:
        img = Image.open(file_path)
        img.verify()
    except Exception as e:
        os.remove(file_path)
        print(file_path)
