# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud import vision
from google.cloud import storage
from google.cloud import language_v1
from google.cloud import videointelligence_v1p3beta1 as videointelligence
#from google.cloud import videointelligence

import io

def implicit():

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

# This method uploads files to cloud storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

def get_video(path):
    """Transcribe speech from a video stored on GCS."""

    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.SPEECH_TRANSCRIPTION]

    config = videointelligence.SpeechTranscriptionConfig(
        language_code="en-US", enable_automatic_punctuation=True
    )
    video_context = videointelligence.VideoContext(speech_transcription_config=config)

    operation = video_client.annotate_video(
        request={
            "features": features,
            "input_uri": path,
            "video_context": video_context,
        }
    )

    print("\nProcessing video for speech transcription.")

    result = operation.result(timeout=600)

    # There is only one annotation_result since only
    # one video is processed.
    annotation_results = result.annotation_results[0]

    final_text = ""
    for speech_transcription in annotation_results.speech_transcriptions:

        # The number of alternatives for each transcription is limited by
        # SpeechTranscriptionConfig.max_alternatives.
        # Each alternative is a different possible transcription
        # and has its own confidence score.
        final_text = speech_transcription.alternatives[0].transcript
        print(final_text)
        """
        for alternative in speech_transcription.alternatives:
            print("Alternative level information:")

            print("Transcript: {}".format(alternative.transcript))
            print("Confidence: {}\n".format(alternative.confidence))

            print("Word level information:")
            for word_info in alternative.words:
                word = word_info.word
                start_time = word_info.start_time
                end_time = word_info.end_time
                print(
                    "\t{}s - {}s: {}".format(
                        start_time.seconds + start_time.microseconds * 1e-6,
                        end_time.seconds + end_time.microseconds * 1e-6,
                        word,
                    )
                )
                """
    return(final_text)

def detect_faces2(gcs_uri="gs://prac_interview/testvideo.mp4"):
    """Detects faces in a video."""

    client = videointelligence.VideoIntelligenceServiceClient()

    # Configure the request
    config = videointelligence.FaceDetectionConfig(
        include_bounding_boxes=True, include_attributes=True
    )
    context = videointelligence.VideoContext(face_detection_config=config)

    # Start the asynchronous request
    operation = client.annotate_video(
        request={
            "features": [videointelligence.Feature.FACE_DETECTION],
            "input_uri": gcs_uri,
            "video_context": context,
        }
    )

    print("\nProcessing video for face detection annotations.")
    result = operation.result(timeout=300)

    print("\nFinished processing.\n")

    # Retrieve the first result, because a single video was processed.
    annotation_result = result.annotation_results[0]

    for annotation in annotation_result.face_detection_annotations:
        print("Face detected:")
        for track in annotation.tracks:
            print(
                "Segment: {}s to {}s".format(
                    track.segment.start_time_offset.seconds
                    + track.segment.start_time_offset.microseconds / 1e6,
                    track.segment.end_time_offset.seconds
                    + track.segment.end_time_offset.microseconds / 1e6,
                )
            )

            # Each segment includes timestamped faces that include
            # characteristics of the face detected.
            # Grab the first timestamped face
            timestamped_object = track.timestamped_objects[0]
            """box = timestamped_object.normalized_bounding_box
            print("Bounding box:")
            print("\tleft  : {}".format(box.left))
            print("\ttop   : {}".format(box.top))
            print("\tright : {}".format(box.right))
            print("\tbottom: {}".format(box.bottom))"""

            # Attributes include glasses, headwear, smiling, direction of gaze
            print("Attributes:")
            for attribute in timestamped_object.attributes:
                print(
                    "\t{}:{} {}".format(
                        attribute.name, attribute.value, attribute.confidence
                    )
                )

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
    """path = "pictures/happyperson.jpg"
    sound_path = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
    #detect_faces(path)
    text = speech_to_text(sound_path)
    text_sentiment(text)"""

    bucket_name = "prac_interview"
    source_file_name = "pictures/testvideo.mp4"
    destination_blob_name = "testvideo.mp4"
    # This uploads file to cloud storage
    #upload_blob(bucket_name,source_file_name,destination_blob_name)
    video_path = "gs://prac_interview/testvideo.mp4"
    get_video(video_path)
    detect_faces2()