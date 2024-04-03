from typing import List, Self

import pygame
from pygame import Surface
import os

colour = 0, 0, 255


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x: int, height: int, surface_height: int, images_folder: str):
        super().__init__()
        self.__surface_height = surface_height
        self.__images: List[Surface] = []
        self.__clock = pygame.time.Clock()
        self.__time_counter = 0

        self.__load_images(images_folder, height)

        # Properties required by pygame.sprite.Sprite
        self.__image = self.__images[0]
        self.__rect = self.__image.get_rect()

        self.x = x
        self.y = self.__image.get_height()

    @property
    def x(self) -> int:
        return self.__rect.x

    @x.setter
    def x(self, x) -> None:
        self.__rect.x = x

    @property
    def y(self) -> int:
        return self.__surface_height - self.__rect.y

    @y.setter
    def y(self, y) -> None:
        self.__rect.y = self.__surface_height - y

    @property
    def image(self) -> Surface:
        return self.__image

    @image.setter
    def image(self, image: Surface) -> None:
        self.__image = image

    @property
    def rect(self) -> pygame.Rect:
        return self.__rect

    @rect.setter
    def rect(self, rect: pygame.Rect) -> None:
        self.__rect = rect

    # def draw(self, display):
    #     display.blit(
    #         self.images[0],
    #         (self.x, self.surface_height - self.y - self.images[0].get_height()),
    #     )

    def __load_images(self, images_folder: str, height: int) -> None:
        for file in os.listdir(images_folder):
            file = os.path.join(images_folder, file)
            image: Surface = pygame.image.load(file).convert_alpha()
            image = pygame.transform.scale(
                image, (image.get_width() * height // image.get_height(), height)
            )
            image = pygame.transform.flip(image, True, False)
            self.__images.append(image)

    def update(self, delta_time, velocity) -> Self:
        self.__time_counter += self.__clock.tick()
        if self.__time_counter > 100:
            self.__images.append(self.__images.pop(0))
            self.__image = self.__images[0]  # Update the current image
            self.__time_counter = 0
        self.x -= velocity * delta_time
        return self
