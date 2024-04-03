import pygame
from pygame import Surface


import os
from typing import List


class Character(pygame.sprite.Sprite):
    def __init__(self, surface_height: int, images_folder: str, x: int, height: int):
        super().__init__()
        self.yvelocity = 0
        self.surface_height = surface_height
        self.images: List[Surface] = []
        self.clock = pygame.time.Clock()
        self.time_counter = 0

        self.load_images(images_folder, height)
        self.image = self.images[0]  # The current image to be displayed
        self.rect = self.image.get_rect()  # The rectangle that encloses the image

        self.x = x
        self.y = self.image.get_height()

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, x):
        self.rect.x = x

    @property
    def y(self):
        return self.surface_height - self.rect.y

    @y.setter
    def y(self, y):
        self.rect.y = self.surface_height - y

    def load_images(self, images_folder: str, height: int):
        for file in os.listdir(images_folder):
            file = os.path.join(images_folder, file)
            image: Surface = pygame.image.load(file).convert_alpha()
            image = pygame.transform.scale(
                image, (image.get_width() * height // image.get_height(), height)
            )
            image = pygame.transform.flip(image, True, False)
            self.images.append(image)

    def update(self):
        self.time_counter += self.clock.tick()
        if self.time_counter > 100:
            self.images.append(self.images.pop(0))
            self.image = self.images[0]  # Update the current image
            self.time_counter = 0
