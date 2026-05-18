import pygame
import random
import math
from settings import WIDTH, HEIGHT, BALL_SPEED

class Ball:
    def __init__(self):
        self.radius = 10
        self.reset()

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

        angle = random.uniform(-1, 1)
        self.dx = BALL_SPEED * angle
        self.dy = -BALL_SPEED

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Wall bounce
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.dx *= -1

        if self.y <= self.radius:
            self.dy *= -1

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)

    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                            self.radius * 2, self.radius * 2)
