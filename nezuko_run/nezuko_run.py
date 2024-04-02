from typing import List

import pygame
import random

from .obstacle import Obstacle
from .characters.nezuko import Nezuko
from .characters.zenitsu import Zenitsu
from . import Background

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width: int = screen.get_width()
height: int = screen.get_height()
GROUND_HEIGHT = height - 100
BLACK = 0, 0, 0
WHITE = 255, 255, 255
MINGAP = 200
VELOCITY = 300
MAXGAP = 600
OBSTACLESIZE = 200
OBSTACLENUM = 4
CHARACTER_SIZE = 200

nezuko = Nezuko(GROUND_HEIGHT, "imgs/nezuko", 200, CHARACTER_SIZE)
zenitsu = Zenitsu(GROUND_HEIGHT, "imgs/zenitsu", 50, CHARACTER_SIZE)
background = Background("imgs/background.jpg", [0, 0], width, height)

character_list = pygame.sprite.Group()
character_list.add(nezuko)
character_list.add(zenitsu)

# nezuko_running_sound = pygame.mixer.Sound("sounds/nezuko-running.mp3")
nezuko_running_sound = None
pygame.mixer.music.load("sounds/music.mp3")
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(-1)
# nezuko_running_sound.set_volume(0.1)


def main():
    score = 0
    xPos = 0
    yPos = 0
    game_over: bool = False
    lastFrame = pygame.time.get_ticks()
    obstacles: List[Obstacle] = []
    lastObstacle: int = width

    for i in range(OBSTACLENUM):
        lastObstacle += int(
            MINGAP + (MAXGAP - MINGAP) * random.random()
        )  # Make distance between rocks random
        obstacles.append(
            Obstacle(lastObstacle, OBSTACLESIZE, GROUND_HEIGHT, "imgs/inosuke")
        )

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

        background.draw(screen)
        character_list.draw(screen)

        if not game_over:
            nezuko.update(deltaTime, nezuko_running_sound)
            nezuko.checkCollideObstacle([obs.images[0].get_rect() for obs in obstacles])
            zenitsu.update()

        if nezuko.checkOver(zenitsu):
            game_over = True

        for obs in obstacles:
            if not game_over:
                obs.update(deltaTime, VELOCITY)
            obs.draw(screen)

        if game_over:
            font = pygame.font.SysFont("arial", 40)
            text_surface = font.render("Game over !", True, WHITE)
            text_rect = text_surface.get_rect(center=(width // 2, height // 2))
            screen.blit(text_surface, text_rect)

        lastObstacle -= int(VELOCITY * deltaTime)

        pygame.display.update()

        xPos += 1
        yPos += 1


if __name__ == "__main__":
    main()
