import pygame

nezu = 255, 255, 255
NEZUHEIGHT = 40
NEZUWIDTH = 20


class Nezuko:
    def __init__(self, surfaceHeight):
        self.x = 60
        self.y = 0
        self.yvelocity = 0
        self.height = NEZUHEIGHT
        self.width = NEZUWIDTH
        self.surfaceHeight = surfaceHeight

    def jump(
        self,
    ):  # When adding classes into function, the first parameter must be the parameter
        if (
            self.y == 0
        ):  # Only allow jumping if the dinosaur is on the ground to prevent mid air jumps.
            self.yvelocity = 300

    def update(self, deltaTime):  # Updates the y position of the dinosaur each second
        self.yvelocity += -500 * deltaTime  # Gravity
        self.y += self.yvelocity * deltaTime
        if self.y < 0:  # if the dinosaur sinks into the ground, make velocity and y = 0
            self.y = 0
            self.yvelocity = 0

    def draw(self, display):
        pygame.draw.rect(
            display,
            nezu,
            [
                self.x,
                self.surfaceHeight - self.y - self.height,
                self.width,
                self.height,
            ],
        )
