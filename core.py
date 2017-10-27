import pygame
import math
import os
import platform
import subprocess
import ctypes

# COLORS

AQUA = (0, 255, 255, 255)
BLACK = (0, 0, 0, 255)
BLUE = (0, 0, 255, 255)
CORNFLOWER_BLUE = (100, 149, 237, 255)
FUCHSIA =  (255, 0, 255, 255)
GRAY = (128, 128, 128, 255)
GREEN = (0, 128, 0, 255)
LIME = (0, 255, 0, 255)
MAROON = (128, 0, 0, 255)
NAVY_BLUE = (0, 0, 128, 255)
OLIVE = (128, 128, 0, 255)
PURPLE = (128, 0, 128, 255)
RED =  (255, 0, 0, 255)
SILVER = (192, 192, 192, 255)
TEAL = (0, 128, 128, 255)
WHITE =  (255, 255, 255, 255)
YELLOW =  (255, 255, 0, 255)
TRANSPARENT = (255, 255, 255, 0)

COLORS = [
	AQUA, 
	BLACK, 
	BLUE, 
	CORNFLOWER_BLUE, 
	FUCHSIA, 
	GRAY, 
	GREEN, 
	LIME, 
	MAROON, 
	NAVY_BLUE, 
	OLIVE, 
	PURPLE, 
	RED, 
	SILVER, 
	TEAL, 
	WHITE, 
	YELLOW
]

# THICKNESS

FILLED = 0
SOLID = 0
DEFAULT_WIDTH = 16

# TEXT

DEFAULT_FONT_SIZE = 18
DEFAULT_TEXT_SPACING = 3
def get_capslock_state():
	state = False
	if platform.system() == "Windows":
		hllDll = ctypes.WinDLL ("User32.dll")
		VK_CAPITAL = 0x14
		if hllDll.GetKeyState(VK_CAPITAL):
			state = True
		else:
			state = False
	else:
		if subprocess.check_output('xset q | grep LED', shell=True)[65] == 50 :
			state = False
		if subprocess.check_output('xset q | grep LED', shell=True)[65] == 51 :
			state = True
	return state

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

	def set_pygame_rect(self, R):
		self.R = R
	
	def set_alpha(self, value):
		self.color = (self.color[0], self.color[1], self.color[2], value)

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
	
	def __init__(self, value, size=32, color=WHITE, font_name="monospace", bold=False, italic=False):
		self.value = value
		self.size = size
		self.color = color
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