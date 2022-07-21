import sys, os, io

class ObjectLocalization:
<<<<<<< HEAD
    key = "/Users/macair/Downloads/delta-guild-354701-7d01beb6d1f3.json"
    def __init__(self, path):
        self.path = path

    def localize_objects(self):
        from google.cloud import vision
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.key

        client = vision.ImageAnnotatorClient()

        imageLabels = []
        with open(self.path, 'rb') as image_file:
=======
    def __init__(self):
        self.imageLabels = []

    def localize_objects(self, path):
        from google.cloud import vision
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/macair/Downloads/delta-guild-354701-7d01beb6d1f3.json"

        client = vision.ImageAnnotatorClient()

        with open(path, 'rb') as image_file:
>>>>>>> cloud-vision-ocr
            content = image_file.read()
        image = vision.Image(content=content)

        objects = client.object_localization(
            image=image).localized_object_annotations

<<<<<<< HEAD
        for object_ in objects:
            imageLabels.append('{}'.format(object_.name))
            # print('\n{} (confidence: {})'.format(object_.name, object_.score))
            # print('Normalized bounding polygon vertices: ')
            # for vertex in object_.bounding_poly.normalized_vertices:
            #     print(' - ({}, {})'.format(vertex.x, vertex.y))
            
        return imageLabels
=======
        #print('Number of objects found: {}'.format(len(objects)))
        for object_ in objects:
            self.imageLabels.append('{}'.format(object_.name))
            # print('\n{} (confidence: {})'.format(object_.name, object_.score))
            # print('Normalized bounding polygon vertices: ')
            # for vertex in object_.bounding_poly.normalized_vertices:
            #     print(' - ({}, {})'.format(vertex.x, vertex.y))
>>>>>>> cloud-vision-ocr
