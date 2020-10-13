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


'''
Detect Objects - remote
This example detects different kinds of objects with bounding boxes in a remote image.
'''
print("===== Detect Objects - remote =====")
# Call API with URL

list_guns = azure_manager.list_blobs('handguns')

detect_objects_results_remote = computervision_client.detect_objects(
    azure_manager.get_blob_url('handguns', list_guns[0]))

# Print detected objects results with bounding boxes
print("Detecting objects in remote image:")
if len(detect_objects_results_remote.objects) == 0:
    print("No objects detected.")
else:
    for object in detect_objects_results_remote.objects:
        print("object at location {}, {}, {}, {}".format(
            object.rectangle.x, object.rectangle.x + object.rectangle.w,
            object.rectangle.y, object.rectangle.y + object.rectangle.h))


print("===== Categorize an image - remote =====")
# Select the visual feature(s) you want.
remote_image_features = ["categories"]
for index in range(0, 10):
    categorize_results_remote = computervision_client.analyze_image(
        .get_blob_url('handguns', list_guns[index]),
        remote_image_features)

    # Print results with confidence score
    print("Categories from remote image: ")
    if (len(categorize_results_remote.categories) == 0):
        print("No categories detected.")
    else:
        for category in categorize_results_remote.categories:
            print("'{}' with confidence {:.2f}%".format(
                category.name,
                category.score * 100))

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
