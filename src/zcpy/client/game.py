import pygame
from zcpy.client.render import Renderer
from zcpy.common.settings import DebugColors
from zcpy.client.grid import Grid
from zcpy.client.menu import MenuBox

class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        pygame.display.set_caption("ZC Client")

        # Renderer
        self.renderer = Renderer(self.screen)

        # Game objects
        self.grid = Grid(4, 4, 50, (50, 50))
        self.menu_box = MenuBox((200, 100), (50, 400), 50)

        # State
        self.running = True


    def handle_events(self):
        """Handles events such as window resizing and quitting."""
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                self.running = False
            elif evt.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((evt.w, evt.h), pygame.RESIZABLE)
                self.renderer.calculate_scaling()


    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()

            # Render objects
            self.screen.fill(DebugColors.BLACK.value)
            mouse_pos = pygame.mouse.get_pos()
            self.grid.draw(self.renderer, mouse_pos)
            self.menu_box.draw(self.renderer)

            # Update display
            pygame.display.flip()

        quit()