import pygame
from pygame import Surface
from typing import List
import os


# https://www.geeksforgeeks.org/pygame-control-sprites/
class Character(pygame.sprite.Sprite):
    def __init__(self, surfaceHeight: int, images_folder: str, x: int, height: int):
        super().__init__()
        self.x = x
        self.y = 0
        self.yvelocity = 0
        self.surfaceHeight = surfaceHeight
        self.images: List[Surface] = []
        self.clock = pygame.time.Clock()
        self.time_counter = 0

        self.load_images(images_folder, height)
        self.image = self.images[0]  # The current image to be displayed
        self.rect = self.image.get_rect()  # The rectangle that encloses the image

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
            self.rect = self.image.get_rect()  # Update the rectangle
            self.time_counter = 0

    def draw(self, display):
        display.blit(
            self.image,
            (self.x, self.surfaceHeight - self.y - self.image.get_height()),
        )


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.index = 0

    def draw(self, display):
        display.blit(self.image, (self.index, 0))
        display.blit(self.image, (self.rect.width + self.index, 0))
        if self.index == -self.rect.width:
            display.blit(self.image, (self.rect.width + self.index, 0))
            self.index = 0
        self.index -= 1
