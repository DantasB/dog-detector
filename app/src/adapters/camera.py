import cv2


class Camera:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)

    def read_frame(self):
        ret, frame = self.cam.read()
        rgb_frame = self.__beautify_frame(frame)
        return ret, rgb_frame

    def __beautify_frame(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def release(self):
        self.cam.release()


def show_frame(frame):
    cv2.imshow("YOLO V8 Detection", frame)


def wait_for_key():
    return cv2.waitKey(1)


def destroy_all():
    return cv2.destroyAllWindows()
