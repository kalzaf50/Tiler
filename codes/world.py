import pygame, sys
from vars import *
import images
import moving_images
import animation

lava_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
moving_platforms = pygame.sprite.Group()
slime_group = pygame.sprite.Group()

#World class
class World():
	def __init__(self, screen, tile_size, rows, cols):
		self.world_data = []
		self.tile_list = []
		self.boundary_tile = []
		self.screen = screen
		self.tile_size = tile_size
		self.cols = cols
		self.rows = rows
		self.clear = False

		#Create empty tile list
		for row in range(self.rows):
			r = [0] * self.rows
			self.world_data.append(r)
		#create editable boundary
		if not self.clear:
			for tile in range(0, self.rows):
				self.world_data[self.rows - 1][tile] = 2
				self.world_data[0][tile] = 1
				self.world_data[tile][0] = 1
				self.world_data[tile][self.rows - 1] = 1

	#Clear the world
	def clear_world(self):
		for row in range(self.rows):
			for col in range(self.rows):
				self.world_data[row][col] = 0
				self.clear = True

	#Empty the tile list
	def clear_tile(self):
		self.tile_list.clear()

	#Returns the number of exit
	def count_exits(self):
		exit_count = 0
		for row in range(self.rows):
			for col in range(self.rows):
				if self.world_data[row][col] == 8:
					exit_count += 1
		return exit_count
	
	#Returns the number of player's start position
	def count_player(self):
		player_count = 0
		for row in range(self.rows):
			for col in range(self.rows):
				if self.world_data[row][col] == 10:
					player_count += 1
		return player_count
	
	#Returns the number of NPCS
	def count_npcs(self):
		npcs_count = 0
		for row in range(self.rows):
			for col in range(self.rows):
				if self.world_data[row][col] == 9:
					npcs_count += 1
		return npcs_count
	
	#Returns the number of total blocks
	def count_blocks(self):
		blocks_count = 0
		for row in range(self.rows):
			for col in range(self.rows):
				if self.world_data[row][col] > 0 and self.world_data[row][col] < 5:
					blocks_count += 1
		return int(blocks_count)
	
	#Returns the 2D position of an image
	def get_position(self, type):
		for row in range(self.rows):
			for col in range(self.rows):
				if self.world_data[row][col] == type:
					return col * self.tile_size , row * self.tile_size
	
	#Allows the user to edit the world real-time
	def edit_world(self):
		for row in range(self.rows):
			for col in range(self.rows):
				if self.world_data[row][col] > 0:
					if self.world_data[row][col] == 1:
						#barrier blocks
						img = pygame.transform.scale(barrier_img, (self.tile_size, self.tile_size))
						img_rect = img.get_rect()
						img_rect.x = col * self.tile_size
						img_rect.y = row * self.tile_size
						self.screen.blit(img, img_rect)
					if self.world_data[row][col] == 2:
						#ground blocks
						img = pygame.transform.scale(ground_img, (self.tile_size, self.tile_size))
						img_rect = img.get_rect()
						img_rect.x = col * self.tile_size
						img_rect.y = row * self.tile_size
						self.screen.blit(img, img_rect)
					if self.world_data[row][col] == 3:
						#wall blocks
						img = pygame.transform.scale(wall_left_img, (self.tile_size, self.tile_size))
						img_rect = img.get_rect()
						img_rect.x = col * self.tile_size
						img_rect.y = row * self.tile_size
						self.screen.blit(img, img_rect)
					if self.world_data[row][col] == 4:
						#wall blocks
						img = pygame.transform.scale(wall_right_img, (self.tile_size, int(self.tile_size)))
						img_rect = img.get_rect()
						img_rect.x = col * self.tile_size
						img_rect.y = row * self.tile_size
						self.screen.blit(img, img_rect)
					if self.world_data[row][col] == 5:
						#horizontally moving platform
						img = pygame.transform.scale(platform_x_img, (self.tile_size, self.tile_size // 2))
						img_rect = img.get_rect()
						img_rect.x = col * self.tile_size
						img_rect.y = row * self.tile_size
						self.screen.blit(img, img_rect)
					if self.world_data[row][col] == 6:
						#vertically moving platform
						img = pygame.transform.scale(platform_y_img, (self.tile_size, self.tile_size // 2))
						img_rect = img.get_rect()
						img_rect.x = col * self.tile_size
						img_rect.y = row * self.tile_size
						self.screen.blit(img, img_rect)
					if self.world_data[row][col] == 7:
						#lava
						img = pygame.transform.scale(lava_img, (self.tile_size, self.tile_size))
						img_rect = img.get_rect()
						img_rect.x = col * self.tile_size
						img_rect.y = row * self.tile_size
						self.screen.blit(img, img_rect)
					if self.world_data[row][col] == 8:
						#exit
						img = pygame.transform.scale(exit_img, (self.tile_size, int(self.tile_size * 1.5)))
						img_rect = img.get_rect()
						img_rect.x = col * self.tile_size
						img_rect.y = row * self.tile_size - (self.tile_size // 2)
						self.screen.blit(img, img_rect)
					if self.world_data[row][col] == 9:
						#enemy
						img = animation.get_player_animation("slime", "idle")[0]
						img_rect = self.rect = pygame.Rect(0, 0 , 32, 25)
						img_rect.x = col * self.tile_size - 8
						img_rect.y = row * self.tile_size + 5
						self.screen.blit(img, img_rect)
					if self.world_data[row][col] == 10:
						#player
						img = pygame.transform.scale(player_img, (self.tile_size, self.tile_size))
						img_rect = img.get_rect()
						img_rect.x = col * self.tile_size
						img_rect.y = row * self.tile_size
						self.screen.blit(img, img_rect)

	#Load world
	def load_world(self):
		for row in range(self.rows):
			for col in range(self.rows):
				if self.world_data[row][col] > 0:
					if self.world_data[row][col] == 1:
						#barrier blocks
						img = pygame.transform.scale(barrier_img, (self.tile_size, self.tile_size))
						img_rect = img.get_rect()
						img_rect.x = col * self.tile_size
						img_rect.y = row * self.tile_size
						tile = (img, img_rect)
						self.tile_list.append(tile)
					if self.world_data[row][col] == 2:
						#ground blocks
						img = pygame.transform.scale(ground_img, (self.tile_size, self.tile_size))
						img_rect = img.get_rect()
						img_rect.x = col * self.tile_size
						img_rect.y = row * self.tile_size
						tile = (img, img_rect)
						self.tile_list.append(tile)
					if self.world_data[row][col] == 3:
						#wall blocks
						img = pygame.transform.scale(wall_left_img, (self.tile_size, self.tile_size))
						img_rect = img.get_rect()
						img_rect.x = col * self.tile_size
						img_rect.y = row * self.tile_size
						tile = (img, img_rect)
						self.tile_list.append(tile)
					if self.world_data[row][col] == 4:
						#wall blocks
						img = pygame.transform.scale(wall_right_img, (self.tile_size, int(self.tile_size)))
						img_rect = img.get_rect()
						img_rect.x = col * self.tile_size
						img_rect.y = row * self.tile_size
						tile = (img, img_rect)
						self.tile_list.append(tile)
					if self.world_data[row][col] == 5:
						#horizontally moving platform
						move_platform = moving_images.Platform(col * self.tile_size, row * self.tile_size, 2, 0)
						moving_platforms.add(move_platform)
					if self.world_data[row][col] == 6:
						#vertically moving platform
						move_platform = moving_images.Platform(col * self.tile_size, row * self.tile_size, 0, 2)
						moving_platforms.add(move_platform)
					if self.world_data[row][col] == 7:
						#lava
						lava = images.Images("lava", col * self.tile_size, row * self.tile_size)
						lava_group.add(lava)
					if self.world_data[row][col] == 8:
						#exit
						exit = images.Images("exit", col * self.tile_size, row * self.tile_size)
						exit_group.add(exit)
					if self.world_data[row][col] == 9:
						#enemy
						slime = moving_images.Enemy(col * self.tile_size - 8, row * self.tile_size + 5, "normal")
						slime_group.add(slime)
					if self.world_data[row][col] == 10:
						#player
						player = images.Images("player", col * self.tile_size, row * self.tile_size)
						player_group.add(player)

	#Return the spirte group 
	def get_group(group):

		if group == "lava":
			return lava_group
		elif group == "exit":
			return exit_group
		elif group == "player":
			return player_group
		elif group == "platform":
			return moving_platforms
		elif group == "slime":
			return slime_group
	
	#Draw the tiles on the screen
	def draw(self):
		for tile in self.tile_list:
			self.screen.blit(tile[0], tile[1])
			# pygame.draw.rect(screen, (255, 255, 255), tile[1], 1)