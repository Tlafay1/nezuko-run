# obstacle.py

from typing import List
from .characters.nezuko import Nezuko

import pygame
from pygame import Surface
import os

colour = 0, 0, 255


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x: int, height: int, surfaceHeight: int, images_folder: str):
        super().__init__()
        self.x = x
        self.y = 0
        self.height = height
        self.surfaceHeight = surfaceHeight
        self.images: List[Surface] = []
        self.clock = pygame.time.Clock()
        self.time_counter = 0

        self.load_images(images_folder, height)
        self.image = self.images[0]  # The current image to be displayed
        self.rect = self.image.get_rect()  # The rectangle that encloses the image

    def draw(self, display):
        display.blit(
            self.images[0],
            (self.x, self.surfaceHeight - self.y - self.images[0].get_height()),
        )

    def load_images(self, images_folder: str, height: int):
        for file in os.listdir(images_folder):
            file = os.path.join(images_folder, file)
            image: Surface = pygame.image.load(file).convert_alpha()
            image = pygame.transform.scale(
                image, (image.get_width() * height // image.get_height(), height)
            )
            image = pygame.transform.flip(image, True, False)
            self.images.append(image)

    def update(self, deltaTime, velocity):
        self.time_counter += self.clock.tick()
        if self.time_counter > 100:
            self.images.append(self.images.pop(0))
            self.image = self.images[0]  # Update the current image
            self.time_counter = 0
        self.x -= velocity * deltaTime

    def checkOver(self, nezuko: Nezuko):
        nezuko_rect = nezuko.image.get_rect()
        nezuko_rect.topleft = (nezuko.rect.x, nezuko.surfaceHeight - nezuko.rect.y - nezuko_rect.height)
        obstacle_rect = self.image.get_rect()
        obstacle_rect.topleft = (self.x, self.surfaceHeight - self.y - obstacle_rect.height)
        if nezuko_rect.colliderect(obstacle_rect):
            return True
        return False
