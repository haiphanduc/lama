import io
import os
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Thread
import threading
import time
from PIL import Image
from fastapi import File
from litelama import LiteLama


def download_image(url):
    # response = requests.get(url)
    return Image.open(url).convert("RGB")


def read_image_from_upload_file(file):
    # response = requests.get(url)
    return Image.open(io.BytesIO(file.file.read())).convert("RGB")


img_url = "src/input/dog.png"
mask_url = "src/input/maskdog.png"

lama = LiteLama()
lama.load(use_safetensors=True, location="cpu")
lama.to("cpu:0")
init_image = download_image(img_url).resize((512, 512))
mask_image = download_image(mask_url).resize((512, 512))

stime = time.time()
# for i in range(100):
# print(lama.predict(init_image, mask_image))
lama.predict(init_image, mask_image).save("src/output/result.png")


@staticmethod
def removeObject(url: File, mask: File, url_name: str):
    lama = LiteLama()
    lama.load(use_safetensors=True, location="cpu")
    lama.to("cpu:0")
    init_image = read_image_from_upload_file(url).resize((512, 512))
    mask_image = read_image_from_upload_file(mask).resize((512, 512))
    result = "C:/Users/HaiPhan/Desktop/Newfolder/" + url_name
    lama.predict(init_image, mask_image).save(result)
    # with ThreadPoolExecutor() as executor:
    #     executor.map(delayed_detection(result))
    return result

def delayed_detection(url):
    time.sleep(1)
    os.remove(url)



