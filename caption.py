# auto-caption images

IMAGES_DIR = "images"
PREPEND_TEXT = ""
APPEND_TEXT = ""
CAPTION_S_R = [ # search/replace
    ("", ""),
]

MAX_WORKERS = 3

import os
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from concurrent.futures import ThreadPoolExecutor


processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


def blip_captioning(raw_image):
    inputs = processor(raw_image, return_tensors="pt", max_length=100)
    out = model.generate(**inputs, max_new_tokens=100)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption


def caption(file):
    raw_image = Image.open(os.path.join(IMAGES_DIR, file)).convert("RGB")

    caption = blip_captioning(raw_image)

    caption = PREPEND_TEXT + caption + APPEND_TEXT

    for sr in CAPTION_S_R:
        caption = caption.replace(*sr)

    print(file, "->", caption)

    name, ext = os.path.splitext(file)
    with open(f"{IMAGES_DIR}/{name}.txt", "w") as f:
        f.write(caption)


files = filter(
    lambda x: not x.startswith(".") and x.endswith(".png"),
    sorted(os.listdir(IMAGES_DIR)),
)


for i, file in enumerate(files):
    caption(file)


# with ThreadPoolExecutor(MAX_WORKERS) as executor:
#     for i, file in enumerate(files):
#         print(i, file)
#         executor.submit(caption, file)
