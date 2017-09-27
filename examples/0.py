import sys
sys.path.append("..")
import pygame
from PygameUser import core
from PygameUser import widgets

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

	panel = widgets.Panel((0, 0), 3, 3, (128, 64))

	def redraw():
		pygame.display.flip()
		screen.fill((0, 0, 0))
		panel.draw(screen)

while (running):
	clock.tick(FPS)
	redraw()
	handle_events()

	
