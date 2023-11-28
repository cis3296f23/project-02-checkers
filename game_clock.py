# file will contain elements of in an game clock that will be used to determine turns

import pygame 

class Timer:
    def __init__(self, initial_time):
        self.time = initial_time
        self.start_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.start_time) // 1000
        self.time -= elapsed_time
        self.start_time = current_time

    def get_time_string(self):
        minutes = self.time // 60
        seconds = self.time % 60
        return f"{minutes:02d}:{seconds:02d}"

    def is_time_up(self):
        return self.time <= 0