import pygame

pygame.init()

#Initial variables
fps = 60

#define colours
white = (255, 255, 255)
dark_grey = "#101111"

#load images
bg_img = pygame.image.load('assets/backgrounds/stage1_background.png')
barrier_img = pygame.image.load('assets/images/barrier_0.png')
wall_left_img = pygame.image.load('assets/images/outer_wall_0.png')
wall_right_img = pygame.transform.flip(wall_left_img, True, False)
ground_img = pygame.image.load('assets/images/dirt_ground_0.png')
slime_img = pygame.image.load('assets/characters/Enemy/Slime/slime-idle-0.png')
platform_x_img = pygame.image.load('assets/images/cart_x.png')
platform_y_img = pygame.image.load('assets/images/cart_y.png')
lava_img = pygame.image.load('assets/images/lava_0.png')
exit_img = pygame.image.load('assets/images/door_0.png')
play_img = pygame.image.load('assets/images/play_button.png')
stop_img = pygame.image.load('assets/images/stop_icon.png')
player_img = pygame.image.load('assets/images/player_icon.png')
nutin_img = pygame.image.load('assets/images/nothing.png')

#load sound
button_sound = pygame.mixer.Sound("assets/sounds/button.wav")
splatSound = pygame.mixer.Sound("assets/sounds/splat.wav")

#Add win function
#Fix moving platform physics