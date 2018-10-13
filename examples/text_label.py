import sys
sys.path.append("..")
import pygame
import core
import widgets

# Text label example.

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 728

pygame.init()
pygame.font.init
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
running = True

if __name__ == "__main__":	
    panel = widgets.Panel(core.Grid((3, 20), (WINDOW_WIDTH, WINDOW_HEIGHT)), None, None, (0, 0))
    panel.set_color((155, 155, 155, 255))
    text = widgets.TextLabel(panel, (1, 5), core.Text("Hello World!", 32, core.RED))

    def redraw():
        pygame.display.flip()
        screen.fill((0, 0, 0))
        panel.draw(screen)
        text.draw(screen)

while (running):
    clock.tick(FPS)
    redraw()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
