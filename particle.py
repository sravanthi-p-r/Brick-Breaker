import pygame
import random
import math

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(2, 6)

        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed

        self.life = 30
        self.color = color

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.life -= 1

    def draw(self, screen):
        if self.life > 0:
            pygame.draw.circle(screen, self.color,
                               (int(self.x), int(self.y)), 3)
