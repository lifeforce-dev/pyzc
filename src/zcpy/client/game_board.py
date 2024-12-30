from zcpy.common.settings import DebugColors

class Grid:
	def __init__(self, rows, cols, cell_size, top_left):
		self.rows = rows
		self.cols = cols
		self.cell_size = cell_size
		self.top_left = top_left
		self.grid = [[1 if (r + c) % 2 == 0 else 0 for c in range(cols)] for r in range(rows)]

	def draw(self, renderer, mouse_pos):
		for row in range(self.rows):
			for col in range(self.cols):
				x = self.top_left[0] + col * self.cell_size
				y = self.top_left[1] + row * self.cell_size
				color = DebugColors.WHITE if self.grid[row][col] == 1 else DebugColors.DARK_GREY
				renderer.draw_rect((x, y, self.cell_size, self.cell_size), color, border=2)