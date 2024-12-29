import random
from zcpy.common.settings import DebugColors

class MenuBox:
	def __init__(self, size, top_left, red_box_size):
		self.size = size  # Logical size (width, height)
		self.top_left = top_left  # Logical position
		self.red_box_size = red_box_size
		self.red_box_active = True
		self.red_box_numbers = [random.randint(0, 5) for _ in range(4)]

	def draw(self, renderer):
		# Draw the menu box border
		renderer.draw_rect((*self.top_left, *self.size), DebugColors.WHITE, border=2)

		# Draw the red box
		if self.red_box_active:
			red_box_pos = renderer.center((self.red_box_size, self.red_box_size))
			renderer.draw_rect((*red_box_pos, self.red_box_size, self.red_box_size), DebugColors.RED)
