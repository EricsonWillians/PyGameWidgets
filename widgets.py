import pygame
from PygameUser import core

class Component:

	def __init__(self, pos, dimensions, parent):
		self.pos = pos
		self.dimensions = dimensions
		self.parent = parent

class RectWidget(Component, core.Shape):
	
	def __init__(self, pos, dimensions, parent=None):
		Component.__init__(self, pos, dimensions, parent)
		core.Shape.__init__(self, pos, self.dimensions)
		self.color = (0, 0, 0, 0)
		self.rect = None
		
	def draw(self, surface):
		self.rect.draw(surface)
		
	def set_color(self, rgba):
		self.color = rgba
		self.rect = core.Rectangle(self.color, self.pos, self.dimensions)

class Panel(RectWidget):
	
	def __init__(self, pos, grid=None, parent=None):
		self.cell_size = grid.cell_size
		self.dimensions = [grid.columns * grid.cell_size[0], grid.rows * grid.cell_size[1]] 
		self.x_positions = [x for x in range(0, self.dimensions[0], grid.cell_size[0])]
		self.y_positions = [x for x in range(0, self.dimensions[1], grid.cell_size[1])]
		RectWidget.__init__(self, pos, self.dimensions)
		self.widgets = {}
		self.rect = core.Rectangle(self.color, self.pos, self.dimensions)
		
	def add(self, widget):
		self.widgets[(widget.row, widget.column): widget]
		
	def draw(self, surface):
		self.rect.draw(surface)
		
class Button(RectWidget):
	
	def __init__(self, text, command, parent, position_in_grid):
		RectWidget.__init__(self, parent.pos, parent.dimensions, parent)
		self.text = text
		self.command = command
		self.pos = [
			self.parent.x_positions[position_in_grid[0]], 
			self.parent.y_positions[position_in_grid[1]]
		]
		self.dimensions = [self.parent.cell_size[0], self.parent.cell_size[1]]
		self.rect = core.Rectangle(self.color, self.pos, self.dimensions)