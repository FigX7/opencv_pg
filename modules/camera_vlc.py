# import the opencv library
import cv2


class CameraVLC():

    def capture(self, rtsp_path, out_path):
        # define a video capture object
        vid = cv2.VideoCapture(rtsp_path)

        # Capture the video frame
        # by frame
        success, frame = vid.read()

        # Display the resulting frame
        if success:
            cv2.imwrite(
                out_path,
                frame)
            cv2.imshow("TEST", frame)
            print(type(frame))
        return frame
