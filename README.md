# PyGameWidgets

A straightforward widget toolkit for [Pygame](https://www.pygame.org).

## Getting Started

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

![Multiple Image Buttons](https://image.ibb.co/mAQYMR/Image_Buttons.png)

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

![Text Field](https://image.ibb.co/hX4A1R/Text_Input.png)

PyGameWidgets uses a grid-based layout manager that allows the development of visual complexity through nesting. There's only one container object ([Panel](https://github.com/EricsonWillians/PyGameWidgets/blob/master/widgets.py#L92)), and all widgets fit inside given a grid configuration:

```
panel = widgets.Panel(core.Grid((3, 7), (WINDOW_WIDTH, WINDOW_HEIGHT)), None, None, (0, 0))
panel.set_color((55, 55, 55, 255))
button = widgets.ToggleButton(panel, (1, 5)) # Here <<
```

The sequence `(1, 5)` means: Second column, sixth row (Starting from zero).  The parent container in this example has a size of 3 columns and 7 rows (`(3, 7)`). Be careful to not confuse yourself with the grid positions, starting always from 0 and defining the size always from 1. 

It's possible to nest panel containers as in this example:

```
panel = widgets.Panel(core.Grid((3, 7), (WINDOW_WIDTH, WINDOW_HEIGHT)), None, None, (0, 0))
panel.set_color((55, 55, 55, 255))
midpanel = widgets.Panel(core.Grid((1, 1), (panel.get_cell_width(), panel.get_cell_height())), panel, (1, 1), None)
midpanel.set_color((0, 0, 0, 255))
midpanel.set_span((0, 6))
button = widgets.TextButton(midpanel, (0, 0), core.Text("Button " + str(0), 32))
button.set_color((0, 100, 0, 255))
button.set_border((255, 0, 0, 255), 16)
```

![Panel Span and Nesting](https://image.ibb.co/k40xFm/Span_and_nesting.png)

As you may have noticed in this example, it's also possible to span components. The first panel has a grid size of `(3, 7)`, and then the second panel has a size of `(1, 1)`, but it's positioned in `(1, 1)` of the first panel (Second column, second row). The span of the second panel (`(0, 6)`) fills the remaining rows. The purpose of this example is to show how nesting and span can be combined to create greater visual complexity.

And here's a multiline string TextLabel example with the Arial font:

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
```

![Multiline TextLabel](https://image.ibb.co/f2ywyG/Text_Label.png)

The core module provides an array of standard colors that can be used in any component for border, background and font colors:

```
AQUA = (0, 255, 255, 255)
BLACK = (0, 0, 0, 255)
BLUE = (0, 0, 255, 255)
CORNFLOWER_BLUE = (100, 149, 237, 255)
FUCHSIA =  (255, 0, 255, 255)
GRAY = (128, 128, 128, 255)
GREEN = (0, 128, 0, 255)
LIME = (0, 255, 0, 255)
MAROON = (128, 0, 0, 255)
NAVY_BLUE = (0, 0, 128, 255)
OLIVE = (128, 128, 0, 255)
PURPLE = (128, 0, 128, 255)
RED =  (255, 0, 0, 255)
SILVER = (192, 192, 192, 255)
TEAL = (0, 128, 128, 255)
WHITE =  (255, 255, 255, 255)
YELLOW =  (255, 255, 0, 255)
```

It's important to remember that all color sequences must be in RGBA format. Alpha transparency is available by default in all pygame surfaces.

Check out each example and be sure to follow the repository for new components.

## Current Widgets

* RectWidget
* Panel
* TextLabel
* RectButton
* TextButton
* TextField
* ToggleButton
* OptionChooser

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
