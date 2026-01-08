import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.background_music = None
        self.sound_effects = {}

    def load_background_music(self, file_path):
        self.background_music = file_path

    def play_background_music(self, loops=-1):
        if self.background_music:
            pygame.mixer.music.load(self.background_music)
            pygame.mixer.music.play(loops)

    def stop_background_music(self):
        pygame.mixer.music.stop()

    def load_sound_effect(self, name, file_path):
        self.sound_effects[name] = pygame.mixer.Sound(file_path)

    def play_sound_effect(self, name):
        if name in self.sound_effects:
            self.sound_effects[name].play()

    def stop_sound_effect(self, name):
        if name in self.sound_effects:
            self.sound_effects[name].stop()