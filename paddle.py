import pygame
from settings import WIDTH, HEIGHT, PADDLE_SPEED, BLUE

class Paddle:
    def __init__(self):
        self.width = 140
        self.height = 18
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 60

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT]:
            self.x += PADDLE_SPEED

        self.x = max(0, min(WIDTH - self.width, self.x))

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE,
                         (self.x, self.y, self.width, self.height),
                         border_radius=8)

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
