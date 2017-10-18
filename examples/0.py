import sys
sys.path.append("..")
import pygame
from PyVenus import core
from PyVenus import widgets

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 728

pygame.init()
pygame.font.init
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
running = True

if __name__ == "__main__":	

	def handle_events():
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				sys.exit()

	panel = widgets.Panel(core.Grid((4, 4), (128, 128)), None, None, (0, 0))
	panel.set_color((255, 255, 255, 255))
	button = widgets.Button("Test", None, panel, (3, 3))
	button.set_color((0, 255, 0, 255))

	def redraw():
		pygame.display.flip()
		screen.fill((0, 0, 0))
		panel.draw(screen)
		button.draw(screen)

while (running):
	clock.tick(FPS)
	redraw()
	handle_events()

	
