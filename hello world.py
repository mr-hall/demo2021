import pygame
import constants

class Main():
    def __init__(self):
        # initialise game
        pygame.init()
        self.running = True
        self.screen = pygame.display.set_mode(constants.SIZE)

    def handle_events(self):
        # check input
        events = pygame.event.get()
        for event in events:
            # if quit
            if event.type == pygame.QUIT:
                running = False


    def update(self):
        pass

    def draw(self):
        self.screen.fill(constants.BLUE)
        pygame.display.flip()

    def gameloop(self):
        # game loop
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    game = Main()
    game.gameloop()





