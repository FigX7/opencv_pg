import os
import pytest
import numpy

import cv2
from modules.camera_vlc import CameraVLC

_OUT_PATH = './modules_tests/assets/test_camera/test_capture.jpg'


@pytest.fixture
def camera(request):
    """Create tester object"""
    return CameraVLC(_OUT_PATH)


def test_capture(camera):
    video_capture = cv2.VideoCapture(os.getenv('RTSP_URL'))
    success, frame = video_capture.read()

    assert isinstance(frame, numpy.ndarray)
