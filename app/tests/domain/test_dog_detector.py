import pytest
from app.src.domain.dog_detector import DogDetector

def test_dog_was_detected():
    detector = DogDetector()
    with pytest.raises(NotImplementedError):
        detector.dog_was_detected(None)
