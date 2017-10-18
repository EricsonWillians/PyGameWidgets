import sys
sys.path.append("..")
import pygame
from PyCliche import core
from PyCliche import widgets

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 728

pygame.init()
pygame.font.init
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
running = True

if __name__ == "__main__":	

	panel = widgets.Panel(core.Grid((4, 4), (128, 128)), None, None, (0, 0))
	panel.set_color((55, 55, 55, 255))
	button = widgets.TextButton(panel, (3, 3), core.Text("Click me!", 16))
	button.set_color((0, 100, 0, 150))

	def redraw():
		pygame.display.flip()
		screen.fill((0, 0, 0))
		panel.draw(screen)
		button.draw(screen)

while (running):
	clock.tick(FPS)
	redraw()
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			sys.exit()
		button.on_click(e, lambda: button.set_color([255, 0, 0, 255]))

	
