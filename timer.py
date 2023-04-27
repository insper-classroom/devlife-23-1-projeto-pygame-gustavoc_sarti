import pygame
import time

class Timer:
    
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.start = 6000
        self.clock.tick(100)

    def time(self):
        self.start -= 1
        if self.start <= 0:
            return False
        return True
        
