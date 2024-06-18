import pytest
from PIL import Image
import os
from app.src.adapters.yolov8_dog_detector import YOLOv8DogDetector
from ultralytics.engine.results import Results

@pytest.fixture
def yolov8_dog_detector(mocker):
    detector = YOLOv8DogDetector("models/yolov8n.pt")
    detector.model = mocker.MagicMock()
    return detector

def test_dog_was_detected(yolov8_dog_detector, mocker):
    # Load the image
    image_path = os.path.join(os.path.dirname(__file__), "..", "images", "test.jpg")
    frame = Image.open(image_path)

    # Create a mock Results object
    mock_results = mocker.create_autospec(Results, instance=True)
    mock_results.boxes = []
    mock_results.names = [yolov8_dog_detector.DOGLABEL]

    # Mock the return value of yolov8_dog_detector.model
    yolov8_dog_detector.model.return_value = [mock_results]

    # Call the method under test
    result = yolov8_dog_detector.dog_was_detected(frame)

    # Assert that the model was called with the correct arguments
    yolov8_dog_detector.model.assert_called_once_with(
        frame,
        verbose=False,
        task="detect",
        iou=0.2,
        conf=0.3,
        classes=[yolov8_dog_detector.DOGCODE],
        show_boxes=True,
    )

    # Assert the result
    assert not result
