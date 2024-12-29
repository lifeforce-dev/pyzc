import pygame
from zcpy.common.settings import DebugColors

class Renderer:
    def __init__(self, screen, base_width=800, base_height=600):
        self.screen = screen
        self.base_width = base_width
        self.base_height = base_height
        self.scaling_factor = 1.0
        self.calculate_scaling()


    def calculate_scaling(self):
        window_width, window_height = self.screen.get_size()
        scale_x = window_width / self.base_width
        scale_y = window_height / self.base_height
        self.scaling_factor = min(scale_x, scale_y)  # Maintain aspect ratio


    def scale(self, value):
        """Scales a logical size/position to the actual screen size."""
        return int(value * self.scaling_factor)


    def draw_rect(self, logical_rect, color, border=0):
        """Draws a rectangle, scaling it to the screen size."""
        scaled_rect = pygame.Rect(
            self.scale(logical_rect[0]),
            self.scale(logical_rect[1]),
            self.scale(logical_rect[2]),
            self.scale(logical_rect[3]),
        )
        pygame.draw.rect(self.screen, color.value, scaled_rect, self.scale(border))


    def draw_text(self, text, logical_position, font, color=DebugColors.WHITE):
        """Draws text at a logical position."""
        scaled_position = (self.scale(logical_position[0]), self.scale(logical_position[1]))
        self.screen.blit(font.render(text, True, color), scaled_position)


    def center(self, logical_size):
        """Calculates the top-left position to center an object."""
        screen_width, screen_height = self.screen.get_size()
        scaled_width, scaled_height = self.scale(logical_size[0]), self.scale(logical_size[1])
        return ((screen_width - scaled_width) // 2, (screen_height - scaled_height) // 2)
