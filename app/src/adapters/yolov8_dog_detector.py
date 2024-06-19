import datetime
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
from ..domain.dog_detector import DogDetector


class YOLOv8DogDetector(DogDetector):
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.DOGLABEL = "dog"
        self.DOGCODE = 16

    def dog_was_detected(self, frame) -> bool:
        detected = False
        results = self.model(
            frame,
            verbose=False,
            task="detect",
            iou=0.2,
            conf=0.3,
            classes=[self.DOGCODE],
            show_boxes=True,
        )
        for r in results:
            annotator = Annotator(frame)
            boxes = r.boxes
            for box in boxes:
                b = box.xyxy[0]
                c = box.cls
                if self.model.names[int(c)] == self.DOGLABEL:
                    print(f"[INFO - {datetime.datetime.now()}] Bit detected!")
                    annotator.box_label(b, "Bit")
                    detected = True
        frame = annotator.result()
        return detected
