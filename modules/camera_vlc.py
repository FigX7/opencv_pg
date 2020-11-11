# import the opencv library
import sys
import cv2
from pynput.keyboard import Listener


class CameraVLC():

    def __init__(self, out_path):
        self.out_path = out_path

    def capture(self, frame):

        # Capture the video frame
        # by frame
        print('------------ starting video ---------------')
        try:
            cv2.imwrite(
                f'{self.out_path}',
                frame)
            print('Video captured')
            
        except Exception as e:
            print(str(e))
            pass
