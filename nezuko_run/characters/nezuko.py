import pygame
from pygame import Surface, Rect
from pygame.sprite import Sprite, collide_rect

from nezuko_run import Character

nezu = 255, 255, 255


class Nezuko(Character):
    GRAVITY = -10
    JUMP_FORCE = 1000

    def jump(self):
        if self.y == self.image.get_height():
            self.yvelocity = self.JUMP_FORCE

    def update(self, delta_time, sound: pygame.mixer.Sound | None):
        self.yvelocity += self.GRAVITY

        if self.y + self.yvelocity * delta_time >= self.image.get_height():
            self.y += self.yvelocity * delta_time
        else:
            self.y = self.image.get_height()

        if sound:
            sound.play()

        super().update()

    def checkCollideObstacle(self, obstacles: list[Rect]):
        for obstacle in obstacles:
            print("Self rect: ", self.rect.x, self.rect.y, self.rect.width, self.rect.height)
            print("Obstacle rect: ", obstacle.rect.x, obstacle.rect.y, obstacle.rect.width, obstacle.rect.height)
            if collide_rect(self, obstacle):
                print("Collided")
                self.x -= 20
                return True
        return False

    def checkOver(self, zenitsu: Character):
        # nezuko_rect = self.images[0].get_rect()
        # nezuko_rect.topleft = (self.x, self.surfaceHeight - self.y - nezuko_rect.height)
        # zenitsu_rect = zenitsu.images[0].get_rect()
        # zenitsu_rect.topleft = (zenitsu.x, zenitsu.surfaceHeight - zenitsu.y - zenitsu_rect.height)
        # if collide_rect(self, zenitsu):
        #     return True
        return False
