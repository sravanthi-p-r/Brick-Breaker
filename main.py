import pygame
import sys
import random

from settings import *
from paddle import Paddle
from ball import Ball
from level import create_level
from particle import Particle
from powerup import PowerUp

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 24)

def draw_ui(score, lives, level):
    txt = font.render(f"Score: {score}  Lives: {lives}  Level: {level}", True, WHITE)
    screen.blit(txt, (20, 20))

def main():
    paddle = Paddle()
    balls = [Ball()]
    bricks = create_level(1)
    particles = []
    powerups = []

    score = 0
    lives = 3
    level = 1

    running = True

    while running:
        clock.tick(FPS)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        paddle.move(keys)

        # BALL UPDATE
        for ball in balls[:]:
            ball.move()

            # Paddle collision
            if ball.rect().colliderect(paddle.rect()):
                ball.dy *= -1

            # Brick collision
            for brick in bricks[:]:
                if ball.rect().colliderect(brick.rect):

                    brick.hit()
                    ball.dy *= -1

                    score += 10

                    # particles
                    for _ in range(12):
                        particles.append(Particle(ball.x, ball.y, RED))

                    # powerup chance
                    if random.random() < 0.2:
                        powerups.append(PowerUp(brick.rect.centerx, brick.rect.centery))

                    if brick.is_dead():
                        bricks.remove(brick)

                    break

            if ball.y > HEIGHT:
                balls.remove(ball)

        if not balls:
            lives -= 1
            balls.append(Ball())

        if lives <= 0:
            print("Game Over")
            running = False

        # POWERUPS
        for p in powerups[:]:
            p.update()

            if p.rect().colliderect(paddle.rect()):
                if p.type == "expand":
                    paddle.width += 40

                elif p.type == "multiball":
                    balls.append(Ball())

                elif p.type == "slow":
                    for b in balls:
                        b.dx *= 0.7
                        b.dy *= 0.7

                powerups.remove(p)

            elif p.y > HEIGHT:
                powerups.remove(p)

        # PARTICLES
        for p in particles[:]:
            p.update()
            if p.life <= 0:
                particles.remove(p)

        # NEXT LEVEL
        if not bricks:
            level += 1
            bricks = create_level(level)
            balls = [Ball()]

        # DRAW
        paddle.draw(screen)

        for ball in balls:
            ball.draw(screen, WHITE)

        for brick in bricks:
            brick.draw(screen)

        for p in particles:
            p.draw(screen)

        for p in powerups:
            p.draw(screen)

        draw_ui(score, lives, level)

        pygame.display.flip()

if __name__ == "__main__":
    main()
