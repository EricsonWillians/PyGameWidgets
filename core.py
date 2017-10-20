import pygame
import math

FILLED = 0
DEFAULT_WIDTH = 16

class Shape(pygame.Surface):
	
	def __init__(self, pos, dimensions):
		pygame.Surface.__init__(self, dimensions, pygame.SRCALPHA, 32)
		self.pos = pos
		self.dimensions = dimensions
		self.x = pos[0]
		self.y = pos[1]
		self.w = dimensions[0]
		self.h = dimensions[1]
		
	def center(self, window_dimensions):
		self.x = (window_dimensions[0] / 2) - (self.w / 2)
		self.y = (window_dimensions[1] / 2) - (self.h / 2)
		
class Rectangle(Shape):
	
	def __init__(self, color, pos, dimensions, width=FILLED):
		Shape.__init__(self, pos, dimensions)
		self.color = color
		self.width = width
		self.R = pygame.Rect(self.pos[0], self.pos[1], self.dimensions[0], self.dimensions[1])

	def set_pygame_rect(R):
		self.R = R
		
	def draw(self, surface):
		pygame.draw.rect(self, self.color, pygame.Rect(0, 0, self.w, self.h), self.width)
		surface.blit(self, (self.x, self.y))
		
class Ellipse(Shape):
	
	def __init__(self, color, pos, dimensions, width=FILLED):
		Shape.__init__(self, pos, dimensions)
		self.color = color
		self.width = width
		
	def draw(self, surface):
		pygame.draw.ellipse(self, self.color, pygame.Rect(0, 0, self.w, self.h), self.width)
		surface.blit(self, (self.x, self.y))
		
class SysFont(Shape):
	
	def __init__(self, color, pos, dimensions, font_name="monospace", bold=False, italic=False):
		Shape.__init__(self, pos, dimensions)
		self.color = color
		self.font_name = font_name
		self.bold = bold
		self.italic = italic
		self.font = pygame.font.SysFont(font_name, 32, bold, italic)

	def draw_text(self, surface, text):
		surface.blit(self.font.render(text, 1, self.color, (self.w, self.h)), (self.x, self.y))

class Text:
	
	def __init__(self, value, size=32, color=[255, 255, 255, 255], font_name="monospace", bold=False, italic=False):
		self.value = value
		self.color = color
		self.size = size
		self.font_name = font_name
		self.bold = bold
		self.italic = italic
		self.font = pygame.font.SysFont(self.font_name, self.size, self.bold, self.italic)

class Grid:

	def __init__(self, grid_size, reference_size):
		self.grid_size = grid_size
		self.cell_size = [
			int(reference_size[0] / self.grid_size[0]),
			int(reference_size[1] / self.grid_size[1])
		]