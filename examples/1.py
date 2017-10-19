import sys
sys.path.append("..")
import pygame
from PyCliche import core
from PyCliche import widgets

# Button span example.

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
    button = widgets.TextButton(midpanel, (0, 0), core.Text("Button " + str(0), 32))
    button.set_color((0, 100, 0, 150))
    button.set_span((0, 3))

    def redraw():
        pygame.display.flip()
        screen.fill((0, 0, 0))
        panel.draw(screen)
        midpanel.draw(screen)
        button.draw(screen)

while (running):
    clock.tick(FPS)
    redraw()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        button.on_click(e, lambda: button.set_text("Pressed."))
        button.on_release(e, lambda: button.set_text("Released"))