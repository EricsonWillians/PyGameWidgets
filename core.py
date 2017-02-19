import pygame
import math

class Shape:
	
	def __init__(self, pos, dimensions):
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
	
	def __init__(self, color, pos, dimensions):
		Shape.__init__(self, pos, dimensions)
		self.color = color
		
	def draw(self, surface):
		pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
	
if __name__ == "__main__":	

	pass
