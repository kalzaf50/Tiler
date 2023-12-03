import pygame
import animation
from vars import *

tile_size = 50

#Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('assets/images/cart.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 25:
            self.move_direction *= -1
            self.move_counter *= -1

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y, type):
		pygame.sprite.Sprite.__init__(self)

		if type == "normal":
			self.image = animation.get_player_animation("slime", "idle")[0]
			self.rect = pygame.Rect(0, 0 , 32, 25)
		
		else:
			self.image = animation.get_player_animation("king_slime", "idle")[0]
			self.rect = pygame.Rect(0, 0 , 32 * 14, 25 * 20)
		
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0
		self.move_steps = 0
		self.move_index = 0
		self.death = False
		self.death_sound = False
		self.idle_running = True

		self.idle_index = 0
		self.idle_counter = 0

		self.death_counter = 0
		self.death_index = 0

	def checkDeath(self, death):
		self.death = death

	def getDeath(self):
		return self.death

	def update(self, type, idle):
		
		move_cooldown = 15
		death_cooldown = 10
		idle_cooldown = 15
		self.idle_running = idle

		if not self.death:
			
			if not self.idle_running:
				self.rect.x += self.move_direction
				self.move_counter += 1
				self.move_steps += 1
			
			else:
				self.idle_counter += 1

			if type == "normal":

				if abs(self.move_steps) > 50:
					self.move_direction *= -1
					self.move_steps *= -1

				# handle walk animation
				if self.move_counter > move_cooldown + 10:
					self.move_index += 1
					self.move_counter = 0
					if self.move_index >= len(animation.get_player_animation("slime", "walk_right")):
						self.move_index = 0
					if self.move_direction == 1:
						self.image = animation.get_player_animation("slime", "walk_right")[self.move_index]
					if self.move_direction == -1:
						self.image = animation.get_player_animation("slime", "walk_left")[self.move_index]
			
			else:
				
				if self.idle_running == True:
					if self.idle_counter > idle_cooldown:
						self.idle_counter = 0	
						self.idle_index += 1
						if self.idle_index >= len(animation.get_player_animation("king_slime", "idle")):
							self.idle_index = 0
						self.image = animation.get_player_animation("king_slime", "idle")[self.idle_index]
				
				else:

					self.move_direction = -1
					# handle walk animation
					if self.move_counter > move_cooldown:
						self.move_index += 1
						self.move_counter = 0
						if self.move_index >= len(animation.get_player_animation("king_slime", "walk_right")):
							self.move_index = 0
						if self.move_direction == 1:
							self.image = animation.get_player_animation("king_slime", "walk_right")[self.move_index]
						if self.move_direction == -1:
							self.image = animation.get_player_animation("king_slime", "walk_left")[self.move_index]

		else:
			
			if not self.death_sound:
				splatSound.play()
				self.death_sound = True

			if type == "normal":
				#Death animation
				self.death_counter += 1
				if self.death_counter > death_cooldown:
					self.death_counter = 0	
					self.death_index += 1
					if self.death_index >= len(animation.get_player_animation("slime", "death")):
						self.death_index = len(animation.get_player_animation("slime", "death")) - 1
						self.death = True

					self.image = animation.get_player_animation("slime", "death")[self.death_index]
			
			else:
				#Death animation
				self.death_counter += 1
				if self.death_counter > death_cooldown:
					self.death_counter = 0	
					self.death_index += 1
					if self.death_index >= len(animation.get_player_animation("king_slime", "death")):
						self.death_index = len(animation.get_player_animation("king_slime", "death")) - 1
						self.death = True

					self.image = animation.get_player_animation("king_slime", "death")[self.death_index]