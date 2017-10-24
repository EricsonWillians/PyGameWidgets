# PyGameWidgets

A straightforward widget toolkit for [Pygame](https://www.pygame.org).

## Getting Started

Import the `core` and `widgets` modules. Use relative imports (As in this example) if necessary.
```
import sys
sys.path.append("..")
import pygame
from PyGame-Widgets import core
from PyGame-Widgets import widgets
```

Here's a working example rendering multiple image buttons that change their text value for "pressed" and "released":

```
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
    panel.set_color((100, 100, 100, 255))
    buttons = [widgets.TextButton(panel, (1, n), core.Text("Button " + str(n), 32)) for n in range(7)]
    [x.set_image("gfx/bg1.bmp") for x in buttons]

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
```

![Multiple Image Buttons](https://ibb.co/bXiL1R)

And here's an example of a TextField object:

```
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
	text_input = widgets.TextField(panel, (1, 5))
	text_input.set_border(core.WHITE, 3)

	def redraw():
		pygame.display.flip()
		screen.fill((0, 0, 0))
		panel.draw(screen)
		text_input.draw(screen)

while (running):
	clock.tick(FPS)
	redraw()
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			sys.exit()
		text_input.register(e)
```

![Text Field](https://ibb.co/eBS8o6)

### Prerequisites

Pygame and Python3 are the only prerequisites. 

`pip install pygame`

### Installing

In the folder of your project, type `git init` and then clone the repository:

`git clone https://github.com/EricsonWillians/PyGame-Widgets`

## Running 

Replace the `example_name` by the name of the example that you want to see.

`python examples/example_name.py`

## Authors

* **Ericson Willians** - [EricsonWillians](https://github.com/EricsonWillians)

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details.
