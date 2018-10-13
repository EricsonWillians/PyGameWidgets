import sys
sys.path.append("..")
import pygame
import core
import widgets

# Multiple buttons example.

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 728

pygame.init()
pygame.font.init
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
running = True

if __name__ == "__main__":
	panel = widgets.Panel(core.Grid((3, 7), (WINDOW_WIDTH, WINDOW_HEIGHT)), None, None, (0, 0))
	panel.set_color((55, 55, 55, 255))
	buttons = [widgets.TextButton(panel, (1, n), core.Text("Button " + str(n), 32)) for n in range(7)]
	[x.set_color((0, 100, 0, 255)) for x in buttons]

	def redraw():
		pygame.display.flip()
		screen.fill((0, 0, 0))
		panel.draw(screen)
		[x.draw(screen) for x in buttons]

while (running):
	clock.tick(FPS)
	redraw()
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			sys.exit()
		[x.on_click(e, lambda: x.set_text(core.Text("Pressed."))) for x in buttons]
		[x.on_release(e, lambda: x.set_text(core.Text("Released."))) for x in buttons]

	
