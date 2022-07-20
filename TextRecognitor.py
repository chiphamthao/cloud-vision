import io
import os

<<<<<<< Updated upstream:TextRecognitor.py
class TextRecognitor: 
    def __init__(self):
        #super().__init__()
        #self.initUI()
        self.labels = []
        
    def detect_text(self, path):
=======
class TextRecognizer: 
    key = "/Users/macair/Downloads/delta-guild-354701-7d01beb6d1f3.json"
    
    def __init__(self, path):
        self.path = path

    def detect_text(self):
>>>>>>> Stashed changes:TextRecognizer.py
        """Detects text in the file."""
        from google.cloud import vision
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.key

        client = vision.ImageAnnotatorClient()

        with io.open(self.path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        labels = []
        positions = []

        response = client.text_detection(image=image)
        texts = response.text_annotations
<<<<<<< Updated upstream:TextRecognitor.py
=======
        sentence = response.full_text_annotation.text

>>>>>>> Stashed changes:TextRecognizer.py
        print('Texts:')

        for text in texts:
<<<<<<< Updated upstream:TextRecognitor.py
            self.labels.append('\n"{}"'.format(text.description))
=======
            labels.append('{}'.format(text.description))
>>>>>>> Stashed changes:TextRecognizer.py

            # vertices = (['({},{})'.format(vertex.x, vertex.y)
            #             for vertex in text.bounding_poly.vertices])

<<<<<<< Updated upstream:TextRecognitor.py
            # print('bounds: {}'.format(','.join(vertices)))
=======
            #print('bounds: {}'.format(','.join(vertices)))
            positions.append('bounds: {}'.format(','.join(vertices)))
>>>>>>> Stashed changes:TextRecognizer.py
    
        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
        
        return labels, sentence, positions

<<<<<<< Updated upstream:TextRecognitor.py
    # def detect_text_uri(self, uri):
    #     """Detects text in the file located in Google Cloud Storage or on the Web.
    #     """
    #     from google.cloud import vision
    #     client = vision.ImageAnnotatorClient()
    #     image = vision.Image()
    #     image.source.image_uri = uri

    #     response = client.text_detection(image=image)
    #     texts = response.text_annotations
    #     print('Texts:')

    #     for text in texts:
    #         print('\n"{}"'.format(text.description))

    #         vertices = (['({},{})'.format(vertex.x, vertex.y)
    #                     for vertex in text.bounding_poly.vertices])

    #         print('bounds: {}'.format(','.join(vertices)))

    #     if response.error.message:
    #         raise Exception(
    #             '{}\nFor more info on error messages, check: '
    #             'https://cloud.google.com/apis/design/errors'.format(
    #                 response.error.message))
=======
    
>>>>>>> Stashed changes:TextRecognizer.py
