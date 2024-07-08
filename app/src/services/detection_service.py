import pydub
from pydub.playback import play

class DetectionService:
    def __init__(self, dog_detector, bot):
        self.dog_detector = dog_detector
        self.bot = bot

    def process_frame(self, frame):
        if self.dog_detector.dog_was_detected(frame):
            self.bot.send_image(frame)
            self.play_sound()

    def play_sound(self):
        song = pydub.AudioSegment.from_mp3("audios/bark.mp3")
        play(song)