import pygame

#Return frames of animations
def get_player_animation(type, animation_type):

    animations = []

    if type == "player":
        if animation_type == "walk_right":
            
            for i in range(0, 4):
                walk_img_right = pygame.image.load(f'assets/characters/Hood/walk_{i}.png')
                walk_img_right = pygame.transform.scale(walk_img_right, (walk_img_right.get_width() * 2, walk_img_right.get_height() * 2))
                animations.append(walk_img_right)
        
        elif animation_type == "walk_left":
            for i in range(0, 4):
                walk_img_right = pygame.image.load(f'assets/characters/Hood/walk_{i}.png')
                walk_img_right = pygame.transform.scale(walk_img_right, (walk_img_right.get_width() * 2, walk_img_right.get_height() * 2))
                walk_img_left = pygame.transform.flip(walk_img_right, True, False)
                animations.append(walk_img_left)

        elif animation_type == "idle_right":
            for i in range(0, 2):
                idle_img_right = pygame.image.load(f'assets/characters/Hood/idle_{i}.png')
                idle_img_right = pygame.transform.scale(idle_img_right, (idle_img_right.get_width() * 2, idle_img_right.get_height() * 2))
                animations.append(idle_img_right)
        
        elif animation_type == "idle_left":
            for i in range(0, 2):
                idle_img_right = pygame.image.load(f'assets/characters/Hood/idle_{i}.png')
                idle_img_right = pygame.transform.scale(idle_img_right, (idle_img_right.get_width() * 2, idle_img_right.get_height() * 2))
                idle_img_left = pygame.transform.flip(idle_img_right, True, False)
                animations.append(idle_img_left)
        
        elif animation_type == "death_right":
            for i in range(0, 8):
                death_img_right = pygame.image.load(f'assets/characters/Hood/death_{i}.png')
                death_img_right = pygame.transform.scale(death_img_right, (death_img_right.get_width() * 2, death_img_right.get_height() * 2))
                animations.append(death_img_right)
        
        elif animation_type == "death_left":
            for i in range(0, 8):
                death_img_right = pygame.image.load(f'assets/characters/Hood/death_{i}.png')
                death_img_right = pygame.transform.scale(death_img_right, (death_img_right.get_width() * 2, death_img_right.get_height() * 2))
                death_img_left = pygame.transform.flip(death_img_right, True, False)
                animations.append(death_img_left)
        
        elif animation_type == "jump_right":
            for i in range(0, 5):
                jump_img_right = pygame.image.load(f'assets/characters/Hood/jump_{i}.png')
                jump_img_right = pygame.transform.scale(jump_img_right, (jump_img_right.get_width() * 2, jump_img_right.get_height() * 2))
                animations.append(jump_img_right)

        elif animation_type == "jump_left":
            for i in range(0, 5):
                jump_img_right = pygame.image.load(f'assets/characters/Hood/jump_{i}.png')
                jump_img_right = pygame.transform.scale(jump_img_right, (jump_img_right.get_width() * 2, jump_img_right.get_height() * 2))
                jump_img_left = pygame.transform.flip(jump_img_right, True, False)
                animations.append(jump_img_left)
        
        elif animation_type == "attack_right":
            for i in range(0, 8):
                attack_img_right = pygame.image.load(f'assets/characters/Hood/attack_{i}.png')
                attack_img_right = pygame.transform.scale(attack_img_right, (attack_img_right.get_width() * 2, attack_img_right.get_height() * 2))
                animations.append(attack_img_right)

        elif animation_type == "attack_left":
            for i in range(0, 8):
                attack_img_right = pygame.image.load(f'assets/characters/Hood/attack_{i}.png')
                attack_img_right = pygame.transform.scale(attack_img_right, (attack_img_right.get_width() * 2, attack_img_right.get_height() * 2))
                attack_img_left = pygame.transform.flip(attack_img_right, True, False)
                animations.append(attack_img_left)

        elif animation_type == "barrier":
            barrier_img = pygame.image.load(f'assets/characters/Hood/barrier.png')
            barrier_img = pygame.transform.scale(barrier_img, (barrier_img.get_width() * 2, barrier_img.get_height() * 2))
            animations.append(barrier_img)

    elif type == "slime":
        if animation_type == "walk_right":
            
            for i in range(0, 4):
                walk_img_left = pygame.image.load(f'assets/characters/Enemy/Slime/slime-move-{i}.png')
                walk_img_left = pygame.transform.scale(walk_img_left, (walk_img_left.get_width() * 2, walk_img_left.get_height() * 2))
                walk_img_right = pygame.transform.flip(walk_img_left, True, False)
                animations.append(walk_img_right)
        
        elif animation_type == "walk_left":
            for i in range(0, 4):
                walk_img_left = pygame.image.load(f'assets/characters/Enemy/Slime/slime-move-{i}.png')
                walk_img_left = pygame.transform.scale(walk_img_left, (walk_img_left.get_width() * 2, walk_img_left.get_height() * 2))
                animations.append(walk_img_left)

        elif animation_type == "idle":
            for i in range(0, 4):
                idle_img = pygame.image.load(f'assets/characters/Enemy/Slime/slime-idle-{i}.png')
                idle_img = pygame.transform.scale(idle_img, (idle_img.get_width() * 2, idle_img.get_height() * 2))
                animations.append(idle_img)

        elif animation_type == "death":
            for i in range(0, 4):
                death_img = pygame.image.load(f'assets/characters/Enemy/Slime/slime-die-{i}.png')
                death_img = pygame.transform.scale(death_img, (death_img.get_width() * 2, death_img.get_height() * 2))
                animations.append(death_img)
    
    elif type == "king_slime":
        if animation_type == "walk_right":
            
            for i in range(0, 4):
                walk_img_left = pygame.image.load(f'assets/characters/Enemy/Slime/slime-move-{i}.png')
                walk_img_left = pygame.transform.scale(walk_img_left, (walk_img_left.get_width() * 15, walk_img_left.get_height() * 20))
                walk_img_right = pygame.transform.flip(walk_img_left, True, False)
                animations.append(walk_img_right)
        
        elif animation_type == "walk_left":
            for i in range(0, 4):
                walk_img_left = pygame.image.load(f'assets/characters/Enemy/Slime/slime-move-{i}.png')
                walk_img_left = pygame.transform.scale(walk_img_left, (walk_img_left.get_width() * 15, walk_img_left.get_height() * 20))
                animations.append(walk_img_left)
        
        elif animation_type == "idle":
            for i in range(0, 4):
                idle_img = pygame.image.load(f'assets/characters/Enemy/Slime/slime-idle-{i}.png')
                idle_img = pygame.transform.scale(idle_img, (idle_img.get_width() * 15, idle_img.get_height() * 20))
                animations.append(idle_img)
        
        elif animation_type == "death":
            for i in range(0, 4):
                death_img = pygame.image.load(f'assets/characters/Enemy/Slime/slime-die-{i}.png')
                death_img = pygame.transform.scale(death_img, (death_img.get_width() * 15, death_img.get_height() * 20))
                animations.append(death_img)

    elif type == "props":

        if animation_type == "lava":
            for i in range(0, 8):
                lava_img = pygame.image.load(f'assets/images/lava_{i}.png')
                lava_img = pygame.transform.scale(lava_img, (50, 50))
                animations.append(lava_img)

        elif animation_type == "fireflies":
            for i in range(0, 4):
                small_fireflies_img = pygame.image.load(f'assets/images/small_fireflies_{i}.png')
                small_fireflies_img = pygame.transform.scale(small_fireflies_img, (50, 50))
                animations.append(small_fireflies_img)
            
        elif animation_type == "warning":
            for i in range(0, 9):
                warning_img = pygame.image.load(f'assets/images/warning_{i}.png')
                warning_img = pygame.transform.scale(warning_img, (warning_img.get_width() * 3, warning_img.get_height() * 3))
                animations.append(warning_img)

    return animations

#Walk animation
def walk_animation(counter, cooldown, index, direction, jumped, image):
        
        #walk animation
        if counter > cooldown:
            counter = 0	
            index += 1
            if index >= len(get_player_animation("player", "walk_right")):
                index = 0
            if direction == 1 and jumped == False:
                image = get_player_animation("player", "walk_right")[index]
            if direction == -1 and jumped == False:
                image = get_player_animation("player", "walk_left")[index]
        
        return counter, index, image

#Jump animation
def jump_animation(counter, cooldown, index, direction, can_jump, image):
        
        #jump animation
        counter += 1
        if counter > cooldown:
            counter = 0
            index += 1
            if (can_jump == True) or (index >= len(get_player_animation("player", "jump_right"))):
                index = 0

            if direction == 1:
                image = get_player_animation("player", "jump_right")[index]
            if direction == -1:
                image = get_player_animation("player", "jump_left")[index]
        
        return counter, index, image

#Attack animation    
def attack_animation(counter, cooldown, index, direction, image):
    
    attack_anim = True
    can_attack = False

    #attack animation
    counter += 1
    if counter > cooldown:
        counter = 0
        index += 1
        if index >= len(get_player_animation("player", "attack_right")):
            index = 0
            attack_anim = False
            can_attack = True
        if direction == 1:
            image = get_player_animation("player", "attack_right")[index]
        elif direction == -1:
            image = get_player_animation("player", "attack_left")[index]


    return counter, index, attack_anim, can_attack, image

#Death animation
def death_animation(counter, cooldown, index, direction, alive, image):

    #Death animation
    counter += 1
    if counter > cooldown:
        counter = 0	
        index += 1
        if index >= len(get_player_animation("player", "death_right")):
            index = len(get_player_animation("player", "death_right")) - 1
            alive = False
        if direction == 1:
            image = get_player_animation("player", "death_right")[index]
        if direction == -1:
            image = get_player_animation("player", "death_left")[index]	
        
    return counter, index, alive, image

#Idle animation
def idle_animation(running, counter, cooldown, index, direction, image):

    #handle animation
    if direction == 1:

        if running == False:
            image = get_player_animation("player", "idle_right")[0]

        if counter > cooldown:
            counter = 0	
            index += 1
            if index >= len(get_player_animation("player", "idle_right")):
                index = 0
            image = get_player_animation("player", "idle_right")[index]
    
    if direction == -1:

        if running == False:
            image = get_player_animation("player", "idle_left")[0]
        
        if counter > cooldown:
            counter = 0	
            index += 1
            if index >= len(get_player_animation("player", "idle_left")):
                index = 0
            image = get_player_animation("player", "idle_left")[index]
    
    return running, counter, index, image