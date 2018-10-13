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
    text = widgets.TextLabel(None, None, core.Text("Hello World!", 32, core.RED))
    text.pos = [
        200,
        300
    ]
    button = widgets.RectButton(None, None)
    button.pos = [
        500,
        400,
    ]
    button.dimensions = [
        128,
        128
    ]
    button.set_color(core.GREEN)
    def redraw():
        pygame.display.flip()
        screen.fill(core.BLACK)
        text.draw(screen)
        button.draw(screen)

while (running):
    clock.tick(FPS)
    redraw()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        # If you don't specify a text object in set_text, it'll generate a default one.
        button.on_click(e, lambda: text.set_text("It works!"))
