from typing import List

import pygame
import random

from .obstacle import Obstacle
from .characters.nezuko import Nezuko
from .characters.zenitsu import Zenitsu
from . import Background

pygame.init()

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
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

obstacle_list = pygame.sprite.Group()

# nezuko_running_sound = pygame.mixer.Sound("sounds/nezuko-running.mp3")
nezuko_running_sound = None
# pygame.mixer.music.load("sounds/music.mp3")
# pygame.mixer.music.set_volume(0.01)
# pygame.mixer.music.play(-1)
# nezuko_running_sound.set_volume(0.1)


def main():
    game_over: bool = False
    last_frame = pygame.time.get_ticks()
    obstacles: List[Obstacle] = []
    last_obstacle: int = width

    for _ in range(OBSTACLENUM):
        last_obstacle += int(
            MINGAP + (MAXGAP - MINGAP) * random.random()
        )  # Make distance between obstacles random

        obstacle = Obstacle(last_obstacle, OBSTACLESIZE, GROUND_HEIGHT, "imgs/inosuke")

        obstacles.append(obstacle)
        obstacle_list.add(obstacle)

    while True:
        t = pygame.time.get_ticks()
        delta_time = (t - last_frame) / 1000.0
        last_frame = t
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
        obstacle_list.draw(screen)

        if not game_over:
            nezuko.update(delta_time, nezuko_running_sound)
            nezuko.checkCollideObstacle(obstacles=obstacles)
            zenitsu.update()
            for obs in obstacles:
                obs.update(delta_time, VELOCITY)

        # if nezuko.checkOver(zenitsu):
        #     game_over = True

        if game_over:
            font = pygame.font.SysFont("arial", 40)
            text_surface = font.render("Game over !", True, WHITE)
            text_rect = text_surface.get_rect(center=(width // 2, height // 2))
            screen.blit(text_surface, text_rect)

        last_obstacle -= int(VELOCITY * delta_time)

        pygame.display.update()


if __name__ == "__main__":
    main()
