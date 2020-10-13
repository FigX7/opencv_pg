from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

from dotenv import load_dotenv
load_dotenv()

from modules import azure_manager

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


# Call API with URL

list_guns = azure_manager.list_blobs('handguns')

'''
Tag an Image - remote
This example returns a tag (key word) for each thing in the image.
'''
threat_words = ['gun', 'weapon', 'rifle', 'firearm']
threats = []
# Call API with remote image
for item in list_guns:
    print(f'===== Tag an image - remote ===== {item}')
    tags_result_remote = computervision_client.tag_image(
        azure_manager.get_blob_url('handguns', item))

    # Print results with confidence score
    print("Tags in the remote image: ")
    if (len(tags_result_remote.tags) == 0):
        print("No tags detected.")
    else:
        for tag in tags_result_remote.tags:
            print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))

            if tag.name in threat_words:
                threats.append(f'{item}')
                break
