# Bulk Image Download and Captioning

A collection of scripts for downloading images in bulk and captioning them. These scripts will be useful for generating dataset to train LoRAs for Stable Diffusion

## Installation

- Requires Python and NodeJS

```sh
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt

cd caption-editor
npm i
cd ..
```

## Available Scripts

`IMAGES_DIR` variable is used to specify the workspace directory where images and captions will be stored by default

### `download.py`

- Download images related to a particular search-term by changing the `KEYWORD` variable
- Use the `LIMIT` variable to specify the total number of images you wish to download
- [`simple_image_download`](https://pypi.org/project/simple-image-download/) is used to download the images
- Images downloaded are saved in increasing numeric order from 1 (i.e 1.png, 2.png, 3.png...)

### `prune.py`

- Some downloaded images can be invalid/corrupted. Use this script to remove those files

### `rename.py`

- To keep the ordering of the filenames, eun this script. It'll rename the files to the default increasing numeric order

### `clean.py`

- Cleans the workspace folder, in other words: removes everything present in `IMAGES_DIR`

### `caption.py`

- Caption all the files present in the workspace folder
- Captions are saved in text files with their names same as the image files. (Like 1.png will have captions in 1.txt)
- Captioning is done with BLIP Captioning
- Use `PREPEND_TEXT` and `APPEND_TEXT` to prepend and append static texts to every captions
- Use `CAPTION_S_R` to search and replace specific terms in the captions
  - `CAPTION_S_R` takes array of tuples
  - Tuples are in a format of `(search, replace)``

### Caption Editor

- A simple captions editor which is browser based
- To run the caption editor

```sh
cd caption-editor
node app.js
```

- Open http://localhost:3000 in your browser to use the UI
