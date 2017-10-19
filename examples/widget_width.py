import sys
sys.path.append("..")
import pygame
from PyCliche import core
from PyCliche import widgets

# Widget width example.

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 728

pygame.init()
pygame.font.init
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
running = True

if __name__ == "__main__":	
	panel = widgets.Panel(core.Grid((3, 7), (int(WINDOW_WIDTH / 3), int(WINDOW_HEIGHT / 1))), None, None, (0, 0))
	panel.set_color((155, 155, 155, 255))
	midpanel = widgets.Panel(core.Grid((1, 7), (panel.grid.cell_size[0], int(WINDOW_HEIGHT / 7))), panel, (1, 0), None)
	panel.set_color((55, 55, 55, 255))
	buttons = [widgets.TextButton(midpanel, (0, n), core.Text("Button " + str(n), 32)) for n in range(7)]
	[x.set_color((0, 100, 0, 150)) for x in buttons]
	[x.set_width(16) for x in buttons]

	def redraw():
		pygame.display.flip()
		screen.fill((0, 0, 0))
		panel.draw(screen)
		midpanel.draw(screen)
		[x.draw(screen) for x in buttons]

while (running):
	clock.tick(FPS)
	redraw()
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			sys.exit()
		[x.on_click(e, lambda: x.set_text("Pressed.")) for x in buttons]
		[x.on_release(e, lambda: x.set_text("Released")) for x in buttons]