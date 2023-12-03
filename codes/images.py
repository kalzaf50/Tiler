import pygame
import animation
from vars import *

tile_size = 50

class Images(pygame.sprite.Sprite):
	def __init__(self, image, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.counter = 0
		self.index = 0

		if image == "lava":
			self.image = pygame.transform.scale(lava_img, (tile_size, tile_size))
		elif image == "exit":
			self.image = pygame.transform.scale(exit_img, (tile_size, tile_size * 1.5))
		elif image == "player":
			self.image = pygame.transform.scale(player_img, (tile_size, tile_size))
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		if image == "exit":
			self.rect.y = y - (tile_size // 2)
		else:
			self.rect.y = y

	def update(self, image):
		lava_cooldown = 7
		
		if image == "lava":
			#Lava animation
			self.counter += 1
			if self.counter > lava_cooldown:
				self.index += 1
				self.counter = 0
				if self.index >= len(animation.get_player_animation("props", "lava")):
					self.index = 0
				self.image = animation.get_player_animation("props", "lava")[self.index]
				
	def reset_npcs(group):
		for member in group:
			group.remove(member)