import io
import os

class TextRecognizer: 
    def __init__(self):
        self.key = "/Users/macair/Downloads/delta-guild-354701-7d01beb6d1f3.json"

    def detect_text(self, path):
        """Detects text in the file."""
        from google.cloud import vision
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.key

        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        labels = []
        positions = []

        response = client.text_detection(image=image)
        texts = response.text_annotations
        sentence = response.full_text_annotation.text

        print('Texts:')
        for text in texts:
            #self.labels.append('\n"{}"'.format(text.description))
            labels.append('{}'.format(text.description))

            vertices = (['({},{})'.format(vertex.x, vertex.y)
                         for vertex in text.bounding_poly.vertices])

            #print('bounds: {}'.format(','.join(vertices)))
            positions.append('bounds: {}'.format(','.join(vertices)))
    
        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))

        return labels, sentence, positions

