import pygame
import constants
import sprites

class Screen():
    def __init__(self):
        pass

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, window):
        pass

class Game_screen(Screen):
    def __init__(self):
        super().__init__()
        self.player = sprites.Player()
        self.enemies = pygame.sprite.Group()
        for i in range(10):
            enemy = sprites.Enemy()
            self.enemies.add(enemy)
        self.player.reset()

    def draw(self,window):
        window.fill(constants.BLUE)
        self.player.draw(window)
        self.enemies.draw(window)

    def update(self):
        self.player.update()
        self.enemies.update()
        pygame.sprite.spritecollide(self.player,self.enemies,True)


