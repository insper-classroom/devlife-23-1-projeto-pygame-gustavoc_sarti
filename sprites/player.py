import pygame
from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    STOP = 4


class Player:
    direction = None
    speed = 0 
    bounds = None

    def __init__(self, bounds):
        self.bounds = bounds
        self.retangulo = self.image.get_rect()
    
    def draw(self, window):
        window.blit(self.image, self.retangulo)

    def move(self, direction):
        if self.direction == Direction.DOWN and self.retangulo.bottom > self.bounds.bottom:
            self.direction = direction
        elif self.direction == Direction.UP and self.retangulo.top < self.bounds.top:
            self.direction = direction
        elif self.direction == Direction.LEFT and self.retangulo.left > self.bounds.left:
            self.direction = direction
        elif self.direction == Direction.RIGHT and self.retangulo.right < self.bounds.right:
            self.direction = direction