import pygame
import random

from .obstacle import Obstacle
from .nezuko import Nezuko

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width = screen.get_width()
height = screen.get_height()
GROUND_HEIGHT = height - 100
BLACK = 0, 0, 0
WHITE = 255, 255, 255
MINGAP = 200
VELOCITY = 300
MAXGAP = 600
OBSTACLESIZE = 50
OBSTACLENUM = 4

nezuko = Nezuko(GROUND_HEIGHT)


def main():
    score = 0
    xPos = 0
    yPos = 0
    lastFrame = pygame.time.get_ticks()
    obstacles = []
    lastObstacle = width

    for i in range(OBSTACLENUM):
        lastObstacle += (
            MINGAP + (MAXGAP - MINGAP) * random.random()
        )  # Make distance between rocks random
        obstacles.append(Obstacle(lastObstacle, OBSTACLESIZE, GROUND_HEIGHT))

    while True:
        t = pygame.time.get_ticks()
        deltaTime = (t - lastFrame) / 1000.0
        lastFrame = t
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                nezuko.jump()

        screen.fill(BLACK)

        nezuko.update(deltaTime)
        nezuko.draw(screen)

        for obs in obstacles:
            obs.update(deltaTime, VELOCITY)
            obs.draw(screen)
            if obs.checkOver():
                score += 1
                lastObstacle += MINGAP + (MAXGAP - MINGAP) * random.random()
                obs.x = lastObstacle

        lastObstacle -= VELOCITY * deltaTime

        pygame.draw.rect(
            screen, WHITE, [0, GROUND_HEIGHT, width, height - GROUND_HEIGHT]
        )

        pygame.display.update()

        xPos += 1
        yPos += 1


if __name__ == "__main__":
    main()
