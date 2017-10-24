# PyGame-Widgets

A straight-foward widget toolkit for [Pygame](https://www.pygame.org).

## Getting Started

´´´
import sys
sys.path.append("..")
import pygame
from PyGame-Widgets import core
from PyGame-Widgets import widgets

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
		[x.on_click(e, lambda: x.set_text("Pressed.")) for x in buttons]
		[x.on_release(e, lambda: x.set_text("Released")) for x in buttons]
´´´

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc


http://
