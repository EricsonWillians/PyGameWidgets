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
    panel = widgets.Panel(core.Grid((3, 10), (WINDOW_WIDTH, WINDOW_HEIGHT)), None, None, (0, 0))
    panel.set_color((155, 155, 155, 255))
    text = widgets.TextLabel(panel, (1, 2), core.Text(
        """
        Lorem ipsum dolor sit amet, 
        consectetur adipiscing elit,
        sed do eiusmod tempor incididunt
        ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis
        nostrud exercitation ullamco laboris
        nisi ut aliquip ex ea commodo consequat.
            Duis aute irure dolor in
            reprehenderit in voluptate velit
            esse cillum dolore eu fugiat
            nulla pariatur. Excepteur sint
            occaecat cupidatat non proident,
            sunt in culpa qui officia deserunt
            mollit anim id est laborum.""", 13, core.BLACK)
    )
    text.set_color(core.WHITE) # This is the color of the widget, not to be confused with the color of its text.
    text.set_span((0, 5))
    text.set_border(core.BLACK, 8)
    text.set_margin(10) # Altering the margin because of the border.

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
