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

    def draw(self,window):
        window.fill(constants.BLUE)
        self.player.draw(window)

    def update(self):
        self.player.update()


