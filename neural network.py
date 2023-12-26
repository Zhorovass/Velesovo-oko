import socket
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import urllib.parse
import socket
import requests

hostname = socket.gethostname()
ip_addresses = socket.getaddrinfo(hostname, None)

np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 300, 300, 3), dtype=np.float32)

#response = requests.get(f"http://{ip_address}/photo.jpg")
#image = Image.open(BytesIO(response.content))
#current_time = time.strftime("%H%M%S", time.localtime())
#image.save(f"using_image{current_time}.jpg")

# Replace this with the path to your image
image = Image.open('C:\Users\Admin\OneDrive\Рабочий стол\дорога\класс_д1').convert("RGB")

# resizing the image to be at least 224x224 and then cropping from the center
size = (300, 300)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Predicts the model
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Print prediction and confidence score
print("Class:", class_name[2:], end="")
print("Confidence Score:", confidence_score)

if class_name == 'Class_p1' or class_name == 'Class_p2' or class_name == 'Class_p3':
    response = urequests.get('https://10.23.41.66:8000/back01')

else:
    response = urequests.get('https://10.23.41.66:8000/forward01')

