# clean images

IMAGES_DIR = "images"

import os

try:
    files = os.listdir(IMAGES_DIR)
    for file in files:
        file_path = os.path.join(IMAGES_DIR, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
except Exception as e:
    print(e)
