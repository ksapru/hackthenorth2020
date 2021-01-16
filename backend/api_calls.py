# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud import vision
from google.cloud import storage
from google.cloud import language_v1
import io

def implicit():

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

def detect_faces(path):
    """Detects faces in an image."""

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))
        print('sorrow: {}'.format(likelihood_name[face.sorrow_likelihood]))

        #scale of 1 to 5
        score = (int(face.joy_likelihood))
        print(score)

        """vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))"""

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return(score)
# TODO: modify to handle any sound file passed through
def speech_to_text(gcs_uri):

    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    #gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"

    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)
    text_all = ""
    for result in response.results:
        text_all += result.alternatives[0].transcript
        print("Transcript: {}".format(result.alternatives[0].transcript))
    print(text_all)
    #text_response = (response.results.alternatives[0].transcript)
    #print(text_response)
    return(text_all)

def text_sentiment(text):

    # Instantiates a client
    client = language_v1.LanguageServiceClient()

    # The text to analyze
    #text = u"Today was a very bad day"
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

    print("Text: {}".format(text))
    score = round(sentiment.score,3)
    mag = round(sentiment.magnitude,3)
    print("Sentiment: {}, {}".format(score, mag))
    return(score)

if __name__ == '__main__':
    path = "pictures/happyperson.jpg"
    sound_path = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
    #detect_faces(path)
    text = speech_to_text(sound_path)
    text_sentiment(text)