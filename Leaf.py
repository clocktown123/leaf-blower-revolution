import pygame
from pygame.math import Vector2
import random
import math

BLUE = (0, 0, 255)

class leaf:
    def __init__(self, xpos, ypos):
        self.x = random.randrange(0, 700)
        self.y = random.randrange(0, 700)
        self.vy = 0
        self.vx = 0
        self.radius = 15

    def draw(self, screen):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.radius)
    
    #def move(self):

    def collision(self, mousePos, px, py):

        self.x += self.vx
        self.y += self.vy

        if (self.radius+70 > math.sqrt((px - self.x)**2 + (py - self.y)**2)):
            print("collision")
            self.vx, self.vy = 1, 1
            self.vx = -self.vx*1
            self.vy = -self.vy*1
        else:
            self.vx = 0
            self.vy = 0


