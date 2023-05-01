import pygame

SCREEN_HEIGHT = 969
SCREEN_WIDTH = 1420

TIMER = 150

star = pygame.image.load('assets/images/props/star_vector.png')
null_star = pygame.image.load('assets/images/props/null_star.png')

STAR = pygame.transform.scale(star,(20,20))
NULL_STAR = pygame.transform.scale(null_star,(20,20))

WALL_GAP = 25


MAP1 = [
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X','X','X',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ','X','X','X','X','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ','X','D',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ','8','-','I','-','-','-','-','-','-','-','-','-','-','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X',' ',' ',' ',' ','L',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ','L',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S','-','-','-','-','-','-','8',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','2',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']
]


MAP2 = [
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ','2',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ','X',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ','X',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ','X',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ','X',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ','X',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','L',' ',' ',' ',' ',' ',' ','L',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ','X','X','X',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S','-','-','-','-','-','-','-','-','-','-','-','-','8',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ','X',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ','L',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ','X',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ','X',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ','X',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ','1',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ','8','-','-','-','-','-','-','-','-','-','-','-','-','-','-','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ','I',' ',' ','X','X','X',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ','D',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ','I',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['S',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ','I',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ','S'],
    ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']
]
    
MAP3 = []
    
