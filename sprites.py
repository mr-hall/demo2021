import pygame
import constants
import random

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

    def reset(self):
        self.x = constants.SIZE[0]//2
        self.y = constants.SIZE[1]-100

class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/enemyGreen2.png").convert()
        self.image.set_colorkey(constants.BLACK)
        self.x = random.randint(0,constants.SIZE[0])
    #
    def update(self):
        self.y=self.y+1
