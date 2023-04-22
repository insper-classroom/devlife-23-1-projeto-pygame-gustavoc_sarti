import pygame
from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Player:
    direction = None
    speed = 0 
    bounds = None

    def __init__(self, bounds):
        self.bounds = bounds
        self.retangulo = self.image.get_rect()
    
    def draw(self, window):
        window.blit(self.image, self.retangulo)