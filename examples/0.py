import sys
sys.path.append("..")
import pygame
import core	

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

	r = core.Ellipse((255, 255, 255), (0, 0), (100, 100))
	r.center((WINDOW_WIDTH, WINDOW_HEIGHT))
	f = core.SysFont((255, 255, 255), (0, 0), (100, 100), "monospace", False, True)

	def redraw():
		pygame.display.flip()
		screen.fill((0, 0, 0))
		f.draw_text(screen, "Whatever")
		r.draw(screen)

while (running):
	clock.tick(FPS)
	redraw()
	handle_events()

	
