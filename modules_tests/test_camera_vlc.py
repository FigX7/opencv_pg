import pytest
import numpy
from modules.camera_vlc import CameraVLC


@pytest.fixture
def camera(request):
    """Create tester object"""
    return CameraVLC()


def test_capture(camera):
    path = 'rtsp://Figs:JesusCC@192.168.0.215/live'
    output = './modules_tests/assets/test_camera/test_capture.jpg'
    img = camera.capture(path, output)

    assert isinstance(img, numpy.ndarray)
