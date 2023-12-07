import animation
import pygame
from pygame.locals import *
import world
from pygame import mixer
from vars import *

class Player():
	def __init__(self, x, y):
		self.walk_index = 0
		self.idle_index = 0
		self.death_index = 0
		self.jump_index = 0
		self.attack_index = 0

		self.idle_counter = 0
		self.walk_counter = 0
		self.death_counter = 0
		self.jump_counter = 0
		self.attack_counter = 0

		self.idle_running = True
		self.walking = False
		self.alive = True
		self.death_anim = False
		self.attack_anim = False
		self.win = False

		self.image = animation.get_player_animation("player", "idle_right")[self.idle_index]
		self.rect = pygame.Rect(0, 0 , 32, 64)
		self.width = self.image.get_width() / 2
		self.height = self.image.get_height() 

		self.vel_x = 0
		self.vel_y = 0
		self.jumped = False
		self.can_jump = False
		self.attacked = False
		self.can_attack = True
		self.direction = 1
		self.rect.x = x
		self.rect.y = y

		self.clock = pygame.time.Clock()

	def __del__(self):
		print('Destructor called, Player deleted.')
	
	#Return player's state of attacking
	def getAttacked(self):
		return self.attacked
	
	#Update player's action and state
	def update(self, screen, world_data):
		dx = 0
		dy = 0
		
		if self.death_anim == False:
			
			#get keypresses
			key = pygame.key.get_pressed()
			if key[pygame.K_SPACE] and self.can_jump == True:
				self.vel_y = -15
				self.jumped = True
				self.idle_running = False
				self.can_jump = False

			if key[pygame.K_SPACE] == False:
				self.jumped = False

			if key[pygame.K_a]:
				dx -= 3
				self.vel_x = -3
				self.walk_counter += 1
				self.direction = -1
				self.idle_counter = 0
				self.idle_running = False

			if key[pygame.K_d]:
				dx += 3
				self.vel_x = 3
				self.walk_counter += 1
				self.direction = 1
				self.idle_counter = 0
				self.idle_running = False
			
			if key[pygame.K_a] or key[pygame.K_d]:
				if not self.walking and not walking_channel.get_busy():
					walking_channel.play(walk_sound)
					self.walking = True
				else:
					self.walking = False
			
			if not key[pygame.K_a] and not key[pygame.K_d]:
				walk_sound.stop()

			if key[pygame.K_q]:
				if not self.attacked and not attack_channel.get_busy():
					attack_channel.play(attack_sound)
					self.attacked = True
				self.idle_running = False
				self.can_attack = False
				self.attack_anim = True

			if key[pygame.K_a] == False and key[pygame.K_d] == False:
				self.walk_counter = 0
				self.idle_counter += 1
				self.walk_index = 0
				self.vel_x = 0

				if self.idle_counter > 5:
					self.idle_running = True

				self.idle_running, self.idle_counter, self.idle_index, self.image = animation.idle_animation(self.idle_running, self.idle_counter, idle_cooldown, self.idle_index, 
																			  self.direction, self.image)
		
		#handle walk animation
		if self.alive == True and self.death_anim == False:
			self.walk_counter, self.walk_index, self.image = animation.walk_animation(self.walk_counter, walk_cooldown, self.walk_index, 
																			 self.direction, self.jumped, self.image)

		# Handle attack animation
		if self.attack_anim and self.can_attack == False:
			self.attack_counter, self.attack_index, self.attack_anim, self.can_attack, self.image = animation.attack_animation(self.attack_counter, attack_cooldown, self.attack_index, 
																			 self.direction, self.image)
		
		if self.can_attack:
			self.attacked = False
			
		#handle jump animation
		if self.can_jump == False and self.jumped == True:
			self.jump_counter, self.jump_index, self.image = animation.jump_animation(self.jump_counter, jump_cooldown, self.jump_index, 
																			 self.direction, self.can_jump, self.image)

		if self.can_jump == True:
			self.jump_index = 0

		#handle death animation
		if self.death_anim == True:
			walk_sound.stop()
			self.death_counter, self.death_index, self.alive, self.image = animation.death_animation(self.death_counter, death_cooldown, self.death_index, 
																			 self.direction, self.alive, self.image)
				
		# Apply acceleration due to gravity
		self.vel_y += gravity
		# Limit the velocity to the terminal velocity
		if self.vel_y > terminal_velocity:
			self.vel_y = terminal_velocity
		# Update the position using the updated velocity
		dy += self.vel_y

        #check for collision
		for tile in world_data:
			#check for collision in x direction
			if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
				dx = 0
			#check for collision in y direction
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				#check if below the ground i.e. jumping
				if self.vel_y < 0:
					dy = tile[1].bottom - self.rect.top
					self.vel_y = 0
					self.can_jump = False
				#check if above the ground i.e. falling
				elif self.vel_y >= 0:
					dy = tile[1].top - self.rect.bottom
					self.vel_y = 0
					self.can_jump = True
		
		#check for collision with platforms
		for platform in world.World.get_group("platform"):
			#collision in the x direction
			if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
				dx = 0
			#collision in the y direction
			if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				#check if below platform
				if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
					self.vel_y = 0
					dy = platform.rect.bottom - self.rect.top
				#check if above platform
				elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
					self.rect.bottom = platform.rect.top - 1
					dy = 0
					self.can_jump = True

					if platform.move_x != 0:
						self.rect.x += platform.move_direction * 2
					elif platform.move_y != 0:
						self.rect.y += platform.move_direction * 2

		#check for collision with lava
		lava_group = world.World.get_group("lava")
		if pygame.sprite.spritecollide(self, lava_group, False):
			self.death_anim = True
		
		#check for collision with fireflies
		exit_group = world.World.get_group("exit")
		if pygame.sprite.spritecollide(self, exit_group, False):
			self.win = True
		
		#check for collision with slimes
		slime_group = world.World.get_group("slime")
		for member in slime_group:
			if pygame.sprite.collide_rect(self, member):
				if self.attacked:
					member.checkDeath(True)

				elif not member.getDeath():
					self.death_anim = True

		#update player coordinates
		self.rect.x += dx
		self.rect.y += dy

		if self.rect.bottom > screen.get_height() - 100:
			self.rect.bottom = screen.get_height() - 100
			dy = 0
			self.can_jump = True
		
		if self.rect.left < 0:
			self.rect.left = 0
			dx = 0

		if self.rect.right > 950:
			self.rect.right = 950
			dx = 0

		#draw player onto screen
		screen.blit(self.image, (self.rect.x - 15, self.rect.y))
		return self.alive, self.win