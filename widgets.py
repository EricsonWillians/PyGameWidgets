import pygame
from PygameUser import core

class Panel(core.Shape):
	
	def __init__(self, pos, grid, rgba):
		print(grid.columns * grid.cell_size[0])
		self.cell_size = grid.cell_size
		self.w = grid.columns * grid.cell_size[0]
		self.h = grid.rows * grid.cell_size[1]
		self.x_positions = [x for x in range(0, self.w, grid.cell_size[0])]
		self.y_positions = [x for x in range(0, self.h, grid.cell_size[1])]
		core.Shape.__init__(self, pos, (self.w, self.h))
		self.pos = pos
		self.grid = grid
		self.rgba = rgba
		self.widgets = {}
		self.rect = core.Rectangle(self.rgba, self.pos, self.dimensions)
		
	def add(self, widget):
		self.widgets[(widget.row, widget.column): widget]
		
	def draw(self, surface):
		self.rect.draw(surface)
		

class Widget:
	
	def __init__(self, parent):
		self.parent = parent
		self.rect = None

	def draw(self, surface):
		self.rect.draw(surface)
		
class Button(Widget, core.Shape):
	
	def __init__(self, text, command, parent, position_in_grid):
		Widget.__init__(self, parent)
		self.text = text
		self.command = command
		self.x = self.parent.x_positions[position_in_grid[0]]
		self.y = self.parent.y_positions[position_in_grid[1]]
		self.w = self.parent.cell_size[0]
		self.h = self.parent.cell_size[1]
		self.color = (0, 0, 0, 0)
		self.rect = core.Rectangle(self.color, (self.x, self.y), (self.w, self.h))
		
	def set_color(self, rgba):
		self.color = rgba
		self.rect = core.Rectangle(self.color, (self.x, self.y), (self.w, self.h))
		
	