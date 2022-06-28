import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/macair/Downloads/delta-guild-354701-7d01beb6d1f3.json"
# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('Downloads/photo-1553284965-83fd3e82fa5a.jpeg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)


