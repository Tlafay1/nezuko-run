import pygame


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
