import threading
from src.services.detection_service import DetectionService
from src.adapters.yolov8_dog_detector import YOLOv8DogDetector
from src.adapters.telegram_bot import TelegramBot
from src.adapters.camera import Camera, show_frame, wait_for_key, destroy_all

if __name__ == "__main__":
    dog_detector = YOLOv8DogDetector("models/yolov8n.pt")
    bot = TelegramBot()
    detection_service = DetectionService(dog_detector, bot)
    camera = Camera()
    LIMITER = 30
    frame_counter = 0

    try:
        while True:
            ret, frame = camera.read_frame()
            frame_counter += 1

            if frame_counter % LIMITER == 0:
                threading.Thread(
                    target=detection_service.process_frame, args=(frame,)
                ).start()

            show_frame(frame)

            if wait_for_key() & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        destroy_all()
