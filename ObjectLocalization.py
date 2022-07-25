import sys, os, io

class ObjectLocalization:
    def __init__(self):
        self.key = "/Users/macair/Downloads/delta-guild-354701-7d01beb6d1f3.json"


    def localize_objects(self, path):
        from google.cloud import vision
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.key

        client = vision.ImageAnnotatorClient()

        imageLabels = []
        with open(path, 'rb') as image_file:
            content = image_file.read()
        image = vision.Image(content=content)

        objects = client.object_localization(
            image=image).localized_object_annotations

        for object_ in objects:
            imageLabels.append('{}'.format(object_.name))
            
        return imageLabels
