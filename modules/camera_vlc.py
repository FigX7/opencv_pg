# import the opencv library
import sys
import cv2
from pynput.keyboard import Listener


class CameraVLC():

    def __init__(self, rtsp_path, out_path):
        self.rtsp_path = rtsp_path
        self.out_path = out_path

    def on_press(self, key):
        if hasattr(key, 'char'):
            if key.char == 'q':
                self.capture

    def capture(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()
            # define a video capture object
            vid = cv2.VideoCapture(self.rtsp_path)

            # Capture the video frame
            # by frame
            print('------------ starting video ---------------')
            while(True):
                success, frame = vid.read()
            if cv2.waitKey(1) & 0xFF == ord('c'):
                # Display the resulting frame
                if success:
                    cv2.imwrite(
                        self.out_path,
                        frame)
                    cv2.imshow("TEST", frame)
                    print(type(frame))
                    return frame
