import pytest
from unittest.mock import MagicMock
from app.src.services.detection_service import DetectionService

def test_process_frame(mocker):
    mock_dog_detector = MagicMock()
    mock_bot = MagicMock()

    service = DetectionService(mock_dog_detector, mock_bot)

    frame = "test_frame"
    mock_dog_detector.dog_was_detected.return_value = True

    service.process_frame(frame)

    mock_dog_detector.dog_was_detected.assert_called_once_with(frame)
    mock_bot.send_image.assert_called_once_with(frame)
