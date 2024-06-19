# tests/adapters/test_camera.py
import pytest
from app.src.adapters.camera import Camera, show_frame, wait_for_key


@pytest.fixture
def mock_cv2(mocker):
    return mocker.patch("app.src.adapters.camera.cv2")


def test_read_frame(mock_cv2):
    mock_camera_instance = mock_cv2.VideoCapture.return_value
    mock_camera_instance.read.return_value = (True, "frame")

    camera = Camera()
    ret, frame = camera.read_frame()

    mock_camera_instance.read.assert_called_once()
    assert ret
    assert frame == "frame"


def test_show_frame(mock_cv2):
    frame = "test_frame"
    show_frame(frame)
    mock_cv2.imshow.assert_called_once_with("YOLO V8 Detection", frame)


def test_wait_for_key(mock_cv2):
    wait_for_key()
    mock_cv2.waitKey.assert_called_once_with(1)
