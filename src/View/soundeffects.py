import pygame
import os


class Sound:

    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self.file_folder = Sound.THIS_FOLDER

    def get_sound_effect(self, sound_effect):
        self.filename = "sounds/" + sound_effect + ".wav"
        self.sound_file = os.path.join(self.file_folder, self.filename)

        self.sound_effect = pygame.mixer.Sound(self.sound_file)
        return self.sound_effect.play()
