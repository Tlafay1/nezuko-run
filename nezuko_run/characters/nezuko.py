from typing import Self
import pygame
from pygame.sprite import collide_rect

from ..characters import Character
from ..obstacle import Obstacle

nezu = 255, 255, 255


class Nezuko(Character):
    GRAVITY = -10
    JUMP_FORCE = 1000

    def jump(self) -> Self:
        if self.y == self.image.get_height():
            self.yvelocity = self.JUMP_FORCE
        return self

    def update(self, delta_time, sound: pygame.mixer.Sound | None) -> Self:
        self.yvelocity += self.GRAVITY

        if self.y + self.yvelocity * delta_time >= self.image.get_height():
            self.y += self.yvelocity * delta_time
        else:
            self.y = self.image.get_height()

        if sound:
            sound.play()

        super().update()
        return self

    def checkCollideObstacle(self, obstacles: list[Obstacle]) -> bool:
        for obstacle in obstacles:
            if collide_rect(self, obstacle):  # type: ignore
                self.x -= 20
                return True
        return False

    def checkOver(self, zenitsu: Character) -> bool:
        # nezuko_rect = self.images[0].get_rect()
        # nezuko_rect.topleft = (self.x, self.surfaceHeight - self.y - nezuko_rect.height)
        # zenitsu_rect = zenitsu.images[0].get_rect()
        # zenitsu_rect.topleft = (zenitsu.x, zenitsu.surfaceHeight - zenitsu.y - zenitsu_rect.height)
        # if collide_rect(self, zenitsu):
        #     return True
        return False
