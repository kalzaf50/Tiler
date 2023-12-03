import pygame
from pygame.locals import *
from os import path
from button import *
from vars import *
import world
import player
import json
import images
import time

class TileEngine:
	def __init__(self, title: str, tile_size: int, cols: int, rows: int, margin: int):
		pygame.init()
		self.tile_size = tile_size
		self.rows = rows
		self.cols = cols
		self.width = self.tile_size * cols
		self.height = (self.tile_size * cols) + margin
		self.title = title
		self.clock = pygame.time.Clock()
		self.bg_img = pygame.transform.scale(bg_img, (self.tile_size * cols, (self.tile_size * cols)))

		self.clicked = False
		self.level = 1
		self.saved = False
		self.verified_saved = False
		self.loaded = False
		self.test = False
		self.exit_count = 0
		self.player_count = 0
		self.player_alive = False
		self.player_win = False
		self.warning = False
		self.stats = False
		self.warning_text = ""

		# Creating Pygame window
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption(self.title)

		self.world = world.World(self.screen, self.tile_size, self.rows, self.cols)

	def get_font(self, size):
		return pygame.font.Font("assets/fonts/Bebas-Regular.ttf", size)

	#function for outputting text onto the screen
	def draw_text(self, input_text, font, text_col, x, y, center):
		text = font.render(input_text, True, text_col)
		if center:
			text_rect = text.get_rect(center=(x, y))
		else:
			text_rect = (x, y)
		self.screen.blit(text, text_rect)

	def draw_grid(self):
		for c in range(self.rows + 1):
			#vertical lines
			pygame.draw.line(self.screen, white, (c * self.world.tile_size, 0), (c * self.world.tile_size, self.world.rows * self.world.tile_size))
			#horizontal lines
			pygame.draw.line(self.screen, white, (0, c * self.world.tile_size), (self.world.cols * self.world.tile_size, c * self.world.tile_size))

	def run(self):
		width = 300
		height = 200
		loading_time = 0
		warning_rect = pygame.Rect((self.screen.get_width() - width) // 2, (self.screen.get_height() - height) // 2, width, height)
		stats_rect = pygame.Rect(0, 0, self.screen.get_width(), 100)

		save_button = Button(image=None, pos=(self.width // 2 - 100, self.height - 70), 
							text_input="SAVE", font=self.get_font(32), base_color="#d7fcd4", hovering_color="#39FF14")
		load_button = Button(image=None, pos=(self.width // 2 + 100, self.height - 70), 
							text_input="LOAD", font=self.get_font(32), base_color="#d7fcd4", hovering_color="#39FF14")
		clear_button = Button(image=None, pos=(load_button.x_pos + 80, self.height - 70), 
							text_input="CLEAR", font=self.get_font(32), base_color="#d7fcd4", hovering_color="#39FF14")
		stats_button = Button(image=None, pos=(clear_button.x_pos + 80, self.height - 70), 
							text_input="STATS", font=self.get_font(32), base_color="#d7fcd4", hovering_color="#39FF14")
		play_button = Button(image=play_img, pos=(self.width // 2 - 170, save_button.y_pos + 3 ), 
							text_input="", font=self.get_font(30), base_color="#d7fcd4", hovering_color="#39FF14")
		stop_button = Button(image=stop_img, pos=((play_button.x_pos - 30), play_button.y_pos), 
							text_input="", font=self.get_font(30), base_color="#d7fcd4", hovering_color="#39FF14")
		quit_button = Button(image=None, pos=(self.width - 30, self.height - 30), 
							text_input="QUIT", font=self.get_font(20), base_color="#990000", hovering_color="#FF3131")
		okay_button = Button(image=None, pos=(self.width // 2, warning_rect.y + 160), 
							text_input="OKAY", font=self.get_font(20), base_color="#d7fcd4", hovering_color="#39FF14")
		yes_button = Button(image=None, pos=(self.width // 2 - 50, warning_rect.y + 160), 
							text_input="YES", font=self.get_font(20), base_color="#d7fcd4", hovering_color="#39FF14")
		no_button = Button(image=None, pos=(self.width // 2 + 50, warning_rect.y + 160), 
							text_input="NO", font=self.get_font(20), base_color="#d7fcd4", hovering_color="#39FF14")

		#Special images
		lava_group = world.World.get_group("lava")
		exit_group = world.World.get_group("exit")
		player_group = world.World.get_group("player")
		moving_platforms = world.World.get_group("platform")
		slime_group = world.World.get_group("slime")
		stage_props =  [lava_group, exit_group, player_group, moving_platforms, slime_group]

		#main game loop
		run = True
		while run:

			self.clock.tick(fps)
			start_time = time.time()
			mouse_pos = pygame.mouse.get_pos()

			#draw background
			self.screen.fill(dark_grey)
			self.screen.blit(self.bg_img, (0, 0))

			#Draw images
			lava_group.draw(self.screen)
			exit_group.draw(self.screen)
			player_group.draw(self.screen)
			moving_platforms.draw(self.screen)
			slime_group.draw(self.screen)
			if self.test:
				lava_group.update("lava")
				moving_platforms.update()
				slime_group.update("normal", False)

			for button in [save_button, load_button, quit_button, clear_button, play_button, stop_button, stats_button]:
				button.changeColor(mouse_pos)
				button.update(self.screen)

			#show the grid and draw the level tiles
			if self.test and self.player_count > 0:
				self.world.draw()
				self.player_alive, self.player_win = test_player.update(self.screen, self.world.tile_list)
			else:
				self.world.edit_world()
				self.draw_grid()

			#text showing current level
			self.draw_text(f'Level: {self.level}', self.get_font(25), white, 50, stop_button.y_pos - 16, False)
			self.draw_text('Press UP or DOWN to change level', self.get_font(25), white, 50, self.height - 40, False)
			if self.saved or self.loaded:
				if self.saved:
					pygame.draw.rect(self.screen, "#0b0b0b", warning_rect)
					self.warning_text = "THIS WILL OVERWRITE EXISTING DATA!"
					self.draw_text('WARNING!', self.get_font(25), 'red', self.screen.get_width() // 2, warning_rect.y + 40, True)
					self.draw_text(self.warning_text, self.get_font(20), white, self.screen.get_width() // 2, warning_rect.y + 90, True)
					for button in [yes_button, no_button]:
						button.changeColor(mouse_pos)
						button.update(self.screen)

			if self.verified_saved or self.loaded:
				if self.verified_saved:
					self.saved = False
					display_txt = "SAVED!"
				if self.loaded:
					display_txt = "LOADED!"
				self.draw_text(display_txt, self.get_font(32), white, self.width // 2, self.height - 70, True)
				current_time = pygame.time.get_ticks()
				elapsed_time = (current_time - start_time) // 1000  # Convert milliseconds to seconds
				remaining_time = 3 - elapsed_time
				if remaining_time <= 0:
					remaining_time = 0

				if elapsed_time >= 3:
					self.verified_saved = False
					self.loaded = False
			
			if self.warning:
				self.warning_text = "Cannot edit the map in testing mode!"
				warning_rect = pygame.Rect((self.screen.get_width() - width) // 2, (self.screen.get_height() - height) // 2, width, height)
				pygame.draw.rect(self.screen, dark_grey, warning_rect)
				self.draw_text('WARNING!', self.get_font(25), 'red', self.screen.get_width() // 2, warning_rect.y + 40, True)
				self.draw_text(self.warning_text, self.get_font(20), white, self.screen.get_width() // 2, warning_rect.y + 90, True)
				okay_button.changeColor(mouse_pos)
				okay_button.update(self.screen)
			
			if self.stats:
				pygame.draw.rect(self.screen, dark_grey, stats_rect)
				self.draw_text(f'FPS: {int(self.clock.get_fps())}', self.get_font(25), 'white', stats_rect.x + 50, stats_rect.height // 2, False)
				self.draw_text(f"Loading Time: {loading_time:.5f} Secs", self.get_font(25), 'white', stats_rect.x + 200, stats_rect.height // 2, False)

			#event handler
			for event in pygame.event.get():
				#quit game
				if event.type == pygame.QUIT:
					run = False
				#mouseclicks to change tiles
				if event.type == pygame.MOUSEBUTTONDOWN:
					if save_button.checkForInput(mouse_pos):
						button_sound.play()
						if not self.test:
							self.saved = True
						else:
							self.warning = True
							print("Cannot edit map while testing")

					if load_button.checkForInput(mouse_pos): 
						start_time_loading = time.time()
						button_sound.play()
						if not self.test:
							if path.exists(f'levels\level{self.level}_data.json'):
								f = open(f'levels\level{self.level}_data.json', 'r')
								self.world.world_data = json.load(f)
								f.close()
								self.loaded = True
								loading_time = time.time() - start_time_loading
								start_time = pygame.time.get_ticks()
						else:
							self.warning = True
							print("Cannot edit map while testing")

					if clear_button.checkForInput(mouse_pos):
						button_sound.play()
						if not self.test:
							self.world.clear_world()
						else:
							self.warning = True
							print("Cannot edit map while testing")
					
					if stats_button.checkForInput(mouse_pos):
						button_sound.play()
						self.stats = not self.stats

					if play_button.checkForInput(mouse_pos) and not self.test and self.player_count > 0:
						button_sound.play()
						player_x, player_y = self.world.get_position(10)
						test_player = player.Player(player_x, player_y)
						self.world.load_world()
						self.test = True
						self.player_alive = True

					if stop_button.checkForInput(mouse_pos):
						button_sound.play()
						self.world.clear_tile()
						for prop in stage_props:
							images.Images.reset_npcs(prop)
						self.test = False
					
					if okay_button.checkForInput(mouse_pos):
						button_sound.play()
						self.warning = False
					
					if yes_button.checkForInput(mouse_pos):
						button_sound.play()
						self.verified_saved = True
						#save level data
						f = open(f'levels\level{self.level}_data.json', 'w')
						json.dump(self.world.world_data, f, indent=1)
						f.close()
						start_time = pygame.time.get_ticks()
					
					if no_button.checkForInput(mouse_pos):
						button_sound.play()
						self.saved = False

					if quit_button.checkForInput(mouse_pos):
						button_sound.play()
						run = False

					if self.clicked == False and not self.warning:
						self.exit_count = self.world.count_exits()
						self.player_count = self.world.count_player()
						self.clicked = True
						pos = pygame.mouse.get_pos()
						x = pos[0] // self.world.tile_size
						y = pos[1] // self.world.tile_size

						#check that the coordinates are within the tile area
						if x < self.rows and y < self.rows:
							#update tile value
							if pygame.mouse.get_pressed()[0] == 1 and not self.test:
								self.world.world_data[y][x] += 1
								if self.world.world_data[y][x] == 8 and self.exit_count == 0:
									self.exit_count += 1
								elif self.world.world_data[y][x] == 8 and self.exit_count > 0:
									self.world.world_data[y][x] += 1
								if self.world.world_data[y][x] == 10 and self.player_count == 0:
									self.player_count += 1
								elif self.world.world_data[y][x] == 10 and self.player_count > 0:
									self.world.world_data[y][x] += 1
								if self.world.world_data[y][x] > 10:
									self.world.world_data[y][x] = 0
							elif pygame.mouse.get_pressed()[2] == 1 and not self.test:
								self.world.world_data[y][x] -= 1
								if self.world.world_data[y][x] == 8 and self.exit_count == 0:
									self.exit_count += 1
								elif self.world.world_data[y][x] == 8 and self.exit_count > 0:
									self.world.world_data[y][x] -= 1
								if self.world.world_data[y][x] == 10 and self.player_count == 0:
									self.player_count += 1
								elif self.world.world_data[y][x] == 10 and self.player_count > 0:
									self.world.world_data[y][x] -= 1
								if self.world.world_data[y][x] < 0:
									if self.player_count > 0:
										self.world.world_data[y][x] = 9
									else:
										self.world.world_data[y][x] = 10
				if event.type == pygame.MOUSEBUTTONUP:
					self.clicked = False

				#up and down key presses to change level number
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.level += 1
					elif event.key == pygame.K_DOWN and self.level > 1:
						self.level -= 1
			
			print(self.clock.get_fps())
			#update game display window
			pygame.display.flip()

		pygame.quit()