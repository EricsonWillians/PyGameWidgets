import sys
sys.path.append("..")
import pygame
import core
import widgets

# Widget span example.

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
    midpanel = widgets.Panel(core.Grid((1, 1), (panel.get_cell_width(), panel.get_cell_height())), panel, (1, 0), None)
    midpanel.set_color((0, 0, 0, 255))
    button = widgets.TextButton(midpanel, (0, 0), core.Text("Button " + str(0), 32))
    button.set_color((0, 100, 0, 255))
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
        button.on_click(e, lambda: button.set_text(core.Text("Pressed.")))
        button.on_release(e, lambda: button.set_text(core.Text("Released.")))
