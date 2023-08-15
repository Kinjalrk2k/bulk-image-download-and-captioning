# rename all files in increasing numeric order

IMAGES_DIR = "images"

TMP_DIR = "images_tmp"

import os
import shutil

if not os.path.exists(TMP_DIR):
    os.makedirs(TMP_DIR)

files = filter(
    lambda x: not x.startswith(".") and x.endswith(".png"),
    sorted(os.listdir(IMAGES_DIR)),
)
for i, file in enumerate(files):
    name, ext = os.path.splitext(file)
    source = f"{IMAGES_DIR}/{file}"
    destination = f"{TMP_DIR}/{i+1}{ext}"
    shutil.copy2(source, destination)

shutil.rmtree(IMAGES_DIR)

os.rename(TMP_DIR, IMAGES_DIR)
