from io import BytesIO

import requests
from PIL import Image
import time


def save_image_from_ip(ip_address):
    response = requests.get(f"http://{ip_address}/photo.jpg")
    image = Image.open(BytesIO(response.content))
    current_time = time.strftime("%H%M%S", time.localtime())
    image.save(f"saved_image{current_time}.jpg")
    print("Изображение сохранено!")


ip_address = "192.168.128.8:8080/"
save_image_from_ip(ip_address)
