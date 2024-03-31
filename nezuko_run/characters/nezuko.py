import pygame
from pygame import Surface, Rect
from pygame.sprite import Sprite, collide_rect

from nezuko_run import Character

nezu = 255, 255, 255


class Nezuko(Character):

    def jump(self):
        if self.y == 0:
            self.yvelocity = 300

    def update(self, deltaTime, sound: pygame.mixer.Sound | None):
        self.yvelocity += -500 * deltaTime
        self.y += self.yvelocity * deltaTime
        if self.y < 0:
            self.y = 0
            self.yvelocity = 0
        if sound:
            sound.play()
        super().update()

    def draw(self, display):
        super().draw(display)

    def checkCollideObstacle(self, obstacles: list[Rect]):
        # nezuko_rect = self.images[0].get_rect()
        # nezuko_rect.topleft = (self.x, self.surfaceHeight - self.y - nezuko_rect.height)
        # for value in obstacles:
        #     obstacle_rect: Rect = value
        #     obstacle_rect.topleft = (obstacle_rect.x, self.surfaceHeight - self.y - obstacle_rect.height)
        #     # Don't change the position of the obstacle
        #     if nezuko_rect.colliderect(obstacle_rect):
        #         self.x -= 20
        #         return True
        return False

    def checkOver(self, zenitsu: Character):
        # nezuko_rect = self.images[0].get_rect()
        # nezuko_rect.topleft = (self.x, self.surfaceHeight - self.y - nezuko_rect.height)
        # zenitsu_rect = zenitsu.images[0].get_rect()
        # zenitsu_rect.topleft = (zenitsu.x, zenitsu.surfaceHeight - zenitsu.y - zenitsu_rect.height)
        # if collide_rect(self, zenitsu):
        #     return True
        return False
