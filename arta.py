import datetime
import os
import sys

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import cv2
from dotenv import load_dotenv
import pafy
from pynput import keyboard
from modules import azure_manager
from modules import camera_vlc

load_dotenv()


_time_start = datetime.datetime.now()


def _calc_time_diff(time_start):

    start = datetime.timedelta(
        hours=time_start.hour,
        minutes=time_start.minute,
        seconds=time_start.second,
        microseconds=time_start.microsecond)
    timer = datetime.datetime.now()
    timer = datetime.timedelta(
        hours=timer.hour,
        minutes=timer.minute,
        seconds=timer.second,
        microseconds=timer.microsecond)

    return timer - start


# Add your Computer Vision subscription key to your environment variables.
subscription_key = os.getenv('COMPUTER_VISION_SUBSCRIPTION_KEY')
if not subscription_key:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()
# Add your Computer Vision endpoint to your environment variables.
endpoint = os.getenv('COMPUTER_VISION_ENDPOINT')
if not endpoint:
    print("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

computervision_client = ComputerVisionClient(
    endpoint,
    CognitiveServicesCredentials(subscription_key))

url = 'https://www.youtube.com/watch?v=KmWr_p20tCM'
vPafy = pafy.new(url)
play = vPafy.getbest()

# _vid = cv2.VideoCapture(play.url)

_vid = cv2.VideoCapture(os.getenv('RTSP_URL'))
while True:
    success, frame = _vid.read()
    if success:
        container = 'arta-rtsp-feed'
        file_name = f'{_calc_time_diff(_time_start).seconds}.jpg'
        path = './data/frames/'
        camera = camera_vlc.CameraVLC(f'{path}{file_name}')

        camera.capture(frame)
        az_manager = azure_manager.AzureManager()
        cv2.destroyAllWindows()
        az_manager.upload_image(
            file_name,
            path,
            container)

        # '''
        # Tag an Image - remote
        # This example returns a tag (key word) for each thing in the image.
        # '''
        # threat_words = ['gun', 'weapon', 'rifle', 'firearm']
        # threats = []
        # list_guns = az_manager.list_blobs_names(container)
        # # Call API with remote image
        # for item in list_guns:
        #     print(f'===== Tag an image - remote ===== {item}')
        #     tags_result_remote = computervision_client.tag_image(
        #         az_manager.get_blob_url(container, item))

        #     # Print results with confidence score
        #     print("Tags in the remote image: ")
        #     if (len(tags_result_remote.tags) == 0):
        #         print("No tags detected.")
        #     else:
        #         for tag in tags_result_remote.tags:
        #             print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))

        #             if tag.name in threat_words:
        #                 threats.append(f'{item}')
        #                 break
