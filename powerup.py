import pygame
import random
from settings import GREEN, YELLOW, PURPLE

class PowerUp:
    TYPES = ["expand", "multiball", "slow"]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.type = random.choice(self.TYPES)

    def update(self):
        self.y += 4

    def draw(self, screen):
        color = GREEN
        if self.type == "multiball":
            color = YELLOW
        elif self.type == "slow":
            color = PURPLE

        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)

    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius,
                            self.radius * 2, self.radius * 2)
