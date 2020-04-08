import pygame
import os
from PyGameWidgets import core

class Component:

	def __init__(self, pos, dimensions, parent):
		self.pos = pos
		self.dimensions = dimensions
		self.parent = parent
		self.parent_x_positions = [0]
		self.parent_y_positions = [0]

	def get_width(self):
		return self.dimensions[0]

	def get_height(self):
		return self.dimensions[1]
		
class Widget(Component):
	
	def __init__(self, pos, dimensions, parent=None):
		Component.__init__(self, pos, dimensions, parent)

class RectWidget(Widget):
	
	def __init__(self, pos, dimensions, parent=None):
		Component.__init__(self, pos, dimensions, parent)
		self.color = (0, 0, 0, 255) # Default color is black.
		self.width = core.FILLED # By default the rect widget is "solid".
		self.pos = pos
		self.dimensions = dimensions
		self.rect = None

	def set_color(self, rgba):
		self.color = rgba
		self.rect = core.Rectangle(self.color, self.pos, self.dimensions, self.width)

	def set_width(self, width):
		self.width = width
		self.rect = core.Rectangle(self.color, self.pos, self.dimensions, self.width)

	def set_solid(self, value):
		if value:
			self.set_width(0)
		else:
			self.set_width(core.DEFAULT_WIDTH)

	def set_span(self, span):
		self.span = [span[0]+1, span[1]+1]
		self.span_w = sum([self.dimensions[0] for w in range(self.span[0])])
		self.span_h = sum([self.dimensions[1] for h in range(self.span[1])])
		self.dimensions = [
			self.span_w,
			self.span_h
		]
		self.rect = core.Rectangle(self.color, self.pos, self.dimensions, self.width)
		if hasattr(self, "text"): self.set_text(self.text)

	def set_image(self, path):
		self.image = pygame.transform.scale(
			pygame.image.load(path), 
			(self.dimensions[0], self.dimensions[1])
		)

	def set_image_dimensions(self, d):
		if self.image:
			self.image = pygame.transform.scale(self.image, d)
			self.rect = core.Rectangle(self.color, self.pos, [self.image.get_width(), self.image.get_height()], self.width)

	def set_border(self, color, width=8):
		if width == 0: raise Exception("Border width cannot be 0, otherwise it will eclipse the underlying rect.")
		border_dimensions = [
			self.dimensions[0] + (width * 2),
			self.dimensions[1] + (width * 2)
		]
		border_pos = [
			self.pos[0] - width,
			self.pos[1] - width
		]
		self.border = core.Rectangle(color, self.pos, self.dimensions, width)

	def draw_image(self, surface):
		surface.blit(self.image, (self.pos[0], self.pos[1]))

	def draw(self, surface):
		self.rect.draw(surface)
		if hasattr(self, "image"): self.draw_image(surface)
		if hasattr(self, "border"): self.border.draw(surface)

def rpc(p, l=[]):
	if p.parent:
		rpc(p.parent)
	else:
		l.append(p)
	return l

class Panel(RectWidget):
	
	def __init__(self, grid=None, parent=None, position_in_grid=None, pos=None):
		if pos:
			self.pos = pos
		else:
			self.pos = (0, 0)
		self.grid = grid
		self.dimensions = (
			self.grid.grid_size[0] * self.grid.cell_size[0], 
			self.grid.grid_size[1] * self.grid.cell_size[1]
		)
		self.x_positions = [x for x in range(0, self.dimensions[0], self.grid.cell_size[0])]
		self.y_positions = [x for x in range(0, self.dimensions[1], self.grid.cell_size[1])]
		if (parent and position_in_grid):
			self.parent = parent
			self.position_in_grid = position_in_grid
			parents = rpc(parent)
			lastParent = parents[len(parents)-1]
			self.x_positions = [x for x in range(0, lastParent.dimensions[0], lastParent.grid.cell_size[0])]
			self.y_positions = [x for x in range(0, lastParent.dimensions[1], lastParent.grid.cell_size[1])]
			self.dimensions = [
				lastParent.grid.cell_size[0], 
				lastParent.grid.cell_size[1]
			]
			self.pos = (
				self.x_positions[self.position_in_grid[0]] + lastParent.pos[0],
				self.y_positions[self.position_in_grid[1]] + lastParent.pos[1]
			)
		else:
			self.position_in_grid = (0, 0)
		RectWidget.__init__(self, self.pos, self.dimensions)
		self.rect = core.Rectangle(self.color, self.pos, self.dimensions, self.width)

	def get_cell_width(self):
		return self.grid.cell_size[0]

	def get_cell_height(self):
		return self.grid.cell_size[1]

class PanelSpecific(RectWidget):
	
	def __init__(self, parent, position_in_grid):
		self.parent = parent
		if self.parent:
			self.position_in_grid = position_in_grid
			self.dimensions = [
				self.parent.grid.cell_size[0], 
				self.parent.grid.cell_size[1]
			]
			self.x_positions = [x for x in range(0, self.parent.dimensions[0], self.dimensions[0])]
			self.y_positions = [x for x in range(0, self.parent.dimensions[1], self.dimensions[1])]
			try:
				self.pos = [
					self.x_positions[self.position_in_grid[0]] + self.parent.pos[0],
					self.y_positions[self.position_in_grid[1]] + self.parent.pos[1]
				]
			except IndexError as e:
				raise Exception(
					"The parent component's grid does not have such position: {error}.".format(error=str(self.position_in_grid))
				)
		else:
			self.pos = (0, 0)
			self.dimensions = (0, 0)
		RectWidget.__init__(self, self.pos, self.dimensions, self.parent)
		self.rect = core.Rectangle(self.color, self.pos, self.dimensions)

class TextLabel(PanelSpecific):

	ALIGN_LEFT = 0
	ALIGN_CENTER = 1
	ALIGN_RIGHT = 2
	DEFAULT_MARGIN = 6

	def __init__(self, parent, position_in_grid, text, alignment=ALIGN_LEFT):
		PanelSpecific.__init__(self, parent, position_in_grid)
		self.text_rects = None
		self.set_alignment(alignment)
		self.set_text(text)
		self.set_margin(TextLabel.DEFAULT_MARGIN)
		
	
	def set_text(self, new_text):
		if isinstance(new_text, str):
			if '\n' in new_text:
				self.texts = [core.Text(s) for s in new_text.split('\n')]
				self.text_rects = [
					t.font.render(t.value, 1, core.WHITE) for t in self.texts
				]
			else:
				self.text = core.Text(new_text)
				self.text_rect = self.text.font.render(
					self.text.value, 
					1, 
					core.WHITE
				)
		else:
			if '\n' in new_text.value:
				self.texts = [
					core.Text(s.lstrip(' '), new_text.size, new_text.color, new_text.font_name, new_text.bold, new_text.italic) for s in new_text.value.split('\n')
				]
				self.text_rects = [
					t.font.render(t.value, 1, t.color) for t in self.texts
				]
			else:
				self.text = new_text
				self.text_rect = self.text.font.render(
					self.text.value, 
					1, 
					new_text.color
				)
		self.half_w = self.dimensions[0] / 2
		self.half_h = self.dimensions[1] / 2
		if not self.text_rects:
			self.text_w = self.text_rect.get_rect().width
			self.text_h = self.text_rect.get_rect().height
			self.half_text_w = self.text_w / 2
			self.half_text_h = self.text_h / 2

	def set_alignment(self, alignment):
		self.alignment = alignment

	def set_margin(self, margin):
		self.margin = margin

	def draw(self, surface):
		self.rect.draw(surface)
		if hasattr(self, "border"): self.border.draw(surface)
		if hasattr(self, "image"): self.draw_image(surface)
		if not self.text_rects:
			if self.alignment == TextLabel.ALIGN_LEFT:
				surface.blit(
					self.text_rect, 
					(self.pos[0] + self.margin, self.pos[1] + (self.half_h - self.half_text_h), self.dimensions[0], self.dimensions[1])
				)
			elif self.alignment == TextLabel.ALIGN_CENTER:
				surface.blit(
					self.text_rect, 
					(self.pos[0] + (self.half_w - self.half_text_w), self.pos[1] + (self.half_h - self.half_text_h), self.dimensions[0], self.dimensions[1])
				)
			elif self.alignment == TextLabel.ALIGN_RIGHT:
				surface.blit(
					self.text_rect, 
					(self.pos[0] + (self.dimensions[0] - (self.text_w + self.margin)), self.pos[1] + (self.half_h - self.half_text_h), self.dimensions[0], self.dimensions[1])
				)
		else:
			for n in range(len(self.texts)):
				surface.blit(
					self.text_rects[n], 
					(self.pos[0] + self.margin, self.pos[1] + (self.text_rects[n].get_rect().height * n), self.dimensions[0], self.dimensions[1])
				)

class RectButton(PanelSpecific):

	def __init__(self, parent, position_in_grid):
		PanelSpecific.__init__(self, parent, position_in_grid)

	def on_click(self, event, function, *args):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if self.rect.R.collidepoint(event.pos):
					function(*args) if args else function()

	def on_release(self, event, function, *args):
		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				if self.rect.R.collidepoint(event.pos):
					function(*args) if args else function()

	def on_mouse_button_click(self, event, mouse_button, function, *args):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == mouse_button:
				if self.rect.R.collidepoint(event.pos):
					function(*args) if args else function()

	def on_mouse_button_release(self, event, mouse_button, function, *args):
		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == mouse_button:
				if self.rect.R.collidepoint(event.pos):
					function(*args) if args else function()

class TextButton(TextLabel, RectButton):

	def __init__(self, parent, position_in_grid, text):
		TextLabel.__init__(self, parent, position_in_grid, text)
		RectButton.__init__(self, parent, position_in_grid)

class TextField(PanelSpecific):

	def __init__(self, parent, position_in_grid):
		PanelSpecific.__init__(self, parent, position_in_grid)
		self.focused = False
		self.set_text("", core.DEFAULT_FONT_SIZE)
		self.value = []
		self.set_carret(
			core.WHITE, 
			[self.pos[0], self.pos[1]], 
			[self.dimensions[0] / (self.parent.get_cell_width() / self.text.size), self.dimensions[1]], 
			core.FILLED
		)
		self.mods = {
			"shift": False,
			"left control": False,
			"left alt": False,
			"right alt": False,
			"right control": False
		}

	def set_carret(self, color, pos, dimensions, width):
		self.carret_color = color
		self.carret_pos = pos
		self.carret_dimensions = dimensions
		self.carret_width = width
		self.carret = core.Rectangle(
			self.carret_color,
			self.carret_pos,
			self.carret_dimensions,
			self.carret_width
		)
		self.carret_counter = 0
		self.carret_blinking_state_manager = False
		self.set_carret_blinking_speed(75)

	def set_carret_blinking_speed(self, value):
		self.carret_blinking_speed = value

	def set_carret_color(self, color):
		self.carret_color = color
		self.set_carret(
			self.carret_color,
			self.carret_pos,
			self.carret_dimensions,
			self.carret_width
		)

	def set_text(self, value, size):
		self.text_value = value
		self.text_size = size
		self.half_w = self.dimensions[0] / 2
		self.half_h = self.dimensions[1] / 2
		self.text = core.Text(self.text_value, self.text_size)
		self.text_rect = self.text.font.render(
			self.text.value, 
			1, 
			self.text.color
		)
		self.half_text_w = self.text_rect.get_rect().width / 2
		self.half_text_h = self.text_rect.get_rect().height / 2

	def get_value(self):
		return ''.join(self.value)

	def register(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if self.rect.R.collidepoint(event.pos):
					self.focused = True
				else:
					self.focused = False
		if event.type == pygame.KEYDOWN:
			if self.focused:
				key_name = pygame.key.name(event.key)
				# Backward operations:
				if key_name == "backspace":
					self.value.pop() if self.value else []
				elif key_name == "delete":
					self.value.clear()
				# Foward operations:
				else:
					if self.text_rect.get_rect().width + self.carret_dimensions[0] < self.border.dimensions[0] + core.DEFAULT_TEXT_SPACING if self.border else self.dimensions[0] + core.DEFAULT_TEXT_SPACING :
						if key_name == "space":
							self.value.append(' ')
						elif key_name == "left shift" or key_name == "right shift":
							self.mods["shift"] = True
						else:
							# Check for special
							if key_name.isalnum():
								cross_r = (
									[str(n) for n in range(0, 10)],
									['!', '@', '#', '$', '%', '¨', '&', '*', '(', ')']
								)
								if self.mods["shift"] or core.get_capslock_state():
									if key_name in cross_r[0]:
										for c in cross_r[0]:
											if key_name == c: 
												key_name = cross_r[1][cross_r[0].index(c)-1]
									else:
										key_name = key_name.upper()
								self.value.append(key_name)
				self.set_text(''.join(self.value), self.text_size)
				self.carret_x = self.pos[0] + self.text_rect.get_rect().width + core.DEFAULT_TEXT_SPACING if self.value else self.pos[0] + self.text_rect.get_rect().width
				self.set_carret(
					self.carret_color,
					[self.carret_x, self.carret.pos[1]],
					[self.dimensions[0] / (self.parent.get_cell_width() / self.text.size), self.dimensions[1]],
					self.carret_width
				)
		elif event.type == pygame.KEYUP:
			key_name = pygame.key.name(event.key)
			if key_name == "left shift" or key_name == "right shift":
				self.mods["shift"] = False

	def draw(self, surface):
		self.rect.draw(surface)
		if hasattr(self, "border"): self.border.draw(surface)
		if hasattr(self, "image"): self.draw_image(surface)
		if hasattr(self, "carret") and self.focused: 
			self.carret.draw(surface)
			if self.carret_counter == self.carret_blinking_speed:
				self.carret_blinking_state_manager = True
			if self.carret_blinking_state_manager:
				self.carret.set_alpha(0)
				self.carret_counter = 0
				self.carret_blinking_state_manager = False
			else:
				self.carret.set_alpha(255)
			self.carret_counter += 1
			surface.blit(
				self.text_rect, (
					self.border.dimensions[0] + core.DEFAULT_TEXT_SPACING if self.border else self.pos[0] + core.DEFAULT_TEXT_SPACING, 
					self.pos[1] + (self.half_h - self.half_text_h), 
					self.dimensions[0], 
					self.dimensions[1]
				)
			)

class ToggleButton(RectButton):

	def __init__(self, parent, position_in_grid):
		RectButton.__init__(self, parent, position_in_grid)
		self.state = False
		self.on = RectWidget(self.pos, self.dimensions, self.parent)
		self.off = RectWidget(self.pos, self.dimensions, self.parent)
		self.on.set_color(core.GREEN)
		self.off.set_color(core.RED)
		self.visual_states = [
			self.on,
			self.off
		]

	def set_state(self, state):
		self.state = state

	def toggle(self, e):
		self.on_click(e, 
			lambda: self.set_state(True) if not self.state else self.set_state(False)
		)

	def set_visual_states(self, visual_states):
		self.visual_states = visual_states

	def set_on(self, on):
		self.visual_states[0] = on

	def set_on(self, off):
		self.visual_states[1] = off

	def draw(self, surface):
		self.rect.draw(surface)
		if hasattr(self, "border"): self.border.draw(surface)
		if self.state:
			self.visual_states[0].draw(surface)
		else:
			self.visual_states[1].draw(surface)

class OptionChooser(Panel):

	def __init__(self, parent, position_in_grid, values=[], default_index=0):
		Panel.__init__(self, core.Grid((6, 1), (parent.get_cell_width(), parent.get_cell_height())), parent=parent, position_in_grid=position_in_grid, pos=None)
		# self.set_color(core.TRANSPARENT)
		
		self.previous_button = RectButton(self, (0, 0))
		self.previous_button.set_color(core.TRANSPARENT)
		self.previous_button.set_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gfx/gray_arrow_0.png"))
		self.values = values
		self.index = default_index
		if (self.values):
			self.current_value = self.values[self.index]
		else:
			self.current_value = "Undefined"
		self.text_size = 32
		self.text_color = core.WHITE
		self.font_name = "monospace"
		self.bold = False
		self.italic = False
		self.label = TextLabel(self, (0, 0), core.Text(self.current_value))
		self.label.set_span((5, 0))
		self.label.set_color(core.TRANSPARENT)
		self.forward_button = RectButton(self, (5, 0))
		self.forward_button.set_color(core.TRANSPARENT)
		self.forward_button.set_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gfx/gray_arrow_1.png"))

	def set_images(self, paths):
		self.previous_button.set_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), paths[0]))
		self.forward_button.set_image(os.path.join(os.path.dirname(os.path.abspath(__file__)), paths[1]))

	def update_text(self):
		self.text = core.Text(
			self.current_value,
			self.text_size,
			self.text_color,
			self.font_name,
			self.bold,
			self.italic
		)
		self.label.set_text(self.text)

	def previous(self):
		if self.values:
			if self.index == 0:
				self.index = len(self.values)-1
			else:
				self.index -= 1
			self.current_value = self.values[self.index]
			self.update_text()

	def forward(self):
		if self.values:
			if self.index == len(self.values)-1:
				self.index = 0
			else:
				self.index += 1
			self.current_value = self.values[self.index]
			self.update_text()

	def activate(self, e):
		self.previous_button.on_click(e, lambda: self.previous())
		self.forward_button.on_click(e, lambda: self.forward())

	def set_span(self, span):
		self.span = [span[0]+1, span[1]+1]
		self.span_w = sum([self.dimensions[0] for w in range(self.span[0])])
		self.span_h = sum([self.dimensions[1] for h in range(self.span[1])])
		self.dimensions = [
			self.span_w,
			self.span_h
		]
		self.label.pos = [
			self.pos[0] + ((self.span_w / 2) - (self.label.dimensions[0] / 2)),
			self.pos[1] + ((self.span_h / 2) - (self.label.dimensions[1] / 2))
		]
		self.forward_button.pos = [
			self.pos[0] + (self.span_w - self.forward_button.dimensions[0]),
			self.pos[1]
		]
		if self.previous_button.image:
			self.previous_button.set_image_dimensions((
				self.previous_button.dimensions[0],
				self.span_h
			))
		else:
			self.previous_button.pos[1] = (self.span_h - self.previous_button.dimensions[1])
			self.previous_button.rect.R.width = self.previous_button.pos[0]
			self.previous_button.rect.R.height = self.previous_button.pos[1]
		if self.forward_button.image:
			self.forward_button.set_image_dimensions((
				self.forward_button.dimensions[0],
				self.span_h
			))
		else:
			self.forward_button.pos[1] = (self.span_h - self.forward_button.dimensions[1])
			self.forward_button.rect.R.width = self.forward_button.pos[0]
			self.forward_button.rect.R.height = self.forward_button.pos[1]

	def on_change(self, e, function, *args):
		self.previous_button.on_click(e, function, *args)
		self.forward_button.on_click(e, function, *args)

	def draw(self, surface):
		if hasattr(self, "image"): self.draw_image(surface)
		if hasattr(self, "border"): self.border.draw(surface)
		self.label.draw(surface)
		self.previous_button.draw(surface)
		self.forward_button.draw(surface)
