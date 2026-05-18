import pygame
from settings import RED, ORANGE, YELLOW, GREEN, PURPLE, WHITE

COLORS = [RED, ORANGE, YELLOW, GREEN, PURPLE]

class Brick:
    def __init__(self, x, y, strength=1):
        self.rect = pygame.Rect(x, y, 90, 35)
        self.strength = strength

    def hit(self):
        self.strength -= 1

    def is_dead(self):
        return self.strength <= 0

    def draw(self, screen):
        color = COLORS[max(0, self.strength - 1)]
        pygame.draw.rect(screen, color, self.rect, border_radius=6)
        pygame.draw.rect(screen, WHITE, self.rect, 2, border_radius=6)
