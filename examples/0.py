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

	panel = widgets.Panel(core.Grid(4, 4, (int(WINDOW_WIDTH / 4), int(WINDOW_HEIGHT / 4))), None, None, (0, 0))
	panel.set_color((255, 255, 255, 255))
	subpanel = widgets.Panel(core.Grid(4, 4, (int(WINDOW_WIDTH / 8), int(WINDOW_HEIGHT / 8))), panel, (2, 0), None)
	subpanel.set_color((200, 200, 200, 255))
	subsubpanel = widgets.Panel(core.Grid(4, 4, (int(WINDOW_WIDTH / 16), int(WINDOW_HEIGHT / 16))), subpanel, (1, 0), None)
	subsubpanel.set_color((155, 155, 155, 255))
	subsubsubpanel = widgets.Panel(core.Grid(4, 4, (int(WINDOW_WIDTH / 32), int(WINDOW_HEIGHT / 32))), subsubpanel, (1, 1), None)
	subsubsubpanel.set_color((55, 55, 55, 255))
	# button = widgets.Button("Test", None, subsubpanel, (0, 0))
	# button.set_color((0, 255, 0, 255))

	def redraw():
		pygame.display.flip()
		screen.fill((0, 0, 0))
		panel.draw(screen)
		subpanel.draw(screen)
		subsubpanel.draw(screen)
		subsubsubpanel.draw(screen)
		# button.draw(screen)

while (running):
	clock.tick(FPS)
	redraw()
	handle_events()

	
