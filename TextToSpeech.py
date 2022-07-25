import html
import io
import os
from TextRecognizer import TextRecognizer
from google.api_core.exceptions import AlreadyExists

class TextToSpeech():

    key = "/Users/macair/Downloads/delta-guild-354701-7d01beb6d1f3.json"

    def __init__(self, text, outfile):
        self.text = text
        self.outfile = outfile

    def text_to_speech(self):
        from google.cloud import texttospeech
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.key
    
        escaped_lines = html.escape(self.text)

        # Convert plaintext to SSML in order to wait two seconds
        #   between each line in synthetic speech
        ssml = "<speak>{}</speak>".format(
            escaped_lines.replace("\n", '\n<break time="1gits"/>')
        )

        # Instantiates a client
        client = texttospeech.TextToSpeechClient()

        # Sets the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(ssml=ssml)

        # Builds the voice request, selects the language code ("en-US") and
        # the SSML voice gender ("MALE")
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE
        )

        # Selects the type of audio file to return
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        # Performs the text-to-speech request on the text input with the selected
        # voice parameters and audio file type

        request = texttospeech.SynthesizeSpeechRequest(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        response = client.synthesize_speech(request=request)

        with open(self.outfile, "w+b") as out:
            out.write(response.audio_content)
            print("Audio content written to file " + self.outfile)


                                     
