import pygame
from pygame.math import Vector2
import random

BLUE = (0, 0, 255)

class leaf:
    def __init__(self):
        self.x = random.randrange(0, 700)
        self.y = random.randrange(0, 700)
        self.vy = 0
        self.vx = 0

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), 15)
    
    def move(self, cx, cy):
        pass
