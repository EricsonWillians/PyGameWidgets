import pygame
from PygameUser import core

class Panel(core.Shape):
	
	def __init__(self, pos, grid, rgba):
		core.Shape.__init__(self, pos, (grid.columns * grid.cell_size[0], grid.rows * grid.cell_size[1]))
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
	
	def __init__(self, parent, grid_cfg):
		self.parent = parent
		self.grid_pos = grid_cfg

class Button(Widget, Shape):
	
	def __init__(self, text, command, parent, grid_cfg):
		Widget.__init__(self, parent, grid_cfg)
		# This needs to be better studied...
		# pygame.Surface.__init__(self, dimensions, pygame.SRCALPHA, 32)
		self.text = text
		self.command = command
		self.rect = core.Rectangle((0, 255, 0, 100))