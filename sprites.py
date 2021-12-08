import pygame
import constants

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def update(self):
        pass


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/playerShip1_red.png").convert()
        self.image.set_colorkey(constants.BLACK)

    def update(self):
        self.x = self.x + 1
        if self.x > constants.SIZE[0]:
            self.x = 0

class Enemy(Sprite):
    def __init__(self):
        super().__init__()


