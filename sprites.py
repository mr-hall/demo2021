import pygame
import constants
import random

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 0, 0)

    def draw(self, window):
        window.blit(self.image, self.rect)

    def update(self):
        pass
    #


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/playerShip1_red.png").convert()
        self.image.set_colorkey(constants.BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect = self.rect.move(1, 0)

        if self.rect.x > constants.SIZE[0]:
            self.rect.x = 0

    def reset(self):
        self.rect.x = constants.SIZE[0]//2
        self.rect.y = constants.SIZE[1]-100

class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/enemyGreen2.png").convert()
        self.image.set_colorkey(constants.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,constants.SIZE[0])
    #
    def update(self):
        self.rect.y=self.rect.y+1
