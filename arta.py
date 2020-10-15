import datetime
import os
import sys

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from dotenv import load_dotenv
import keyboard
from PIL import Image
from modules import azure_manager
from modules import camera_vlc


load_dotenv()


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


'''
Detect Objects - remote
This example detects different kinds of objects with bounding boxes in a remote image.
'''
print("===== Detect Objects - remote =====")

'''
Tag an Image - remote
This example returns a tag (key word) for each thing in the image.
'''
camera = camera_vlc.CameraVLC()
time_start = datetime.datetime.now()

while True:
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
    d = timer - start

    keyboard.add_hotkey('enter', lambda: camera.capture(
        os.getenv('RTSP_URL'),
        f'./data/frames/frame_{d.seconds}_{d.microseconds}.jpg'
    ))

print("===== Tag an image - remote =====")
