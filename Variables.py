import pygame
displayHeight = 500
displayWidth = 500
background = pygame.image.load('Assets\\bg.png')
grass = pygame.image.load("Assets\\grass.jpg")
player_standing = pygame.image.load("Assets\\standing.png")
player_right = [pygame.image.load("Assets\\R1.png"),pygame.image.load("Assets\\R2.png"),pygame.image.load("Assets\\R3.png"),pygame.image.load("Assets\\R4.png"),pygame.image.load("Assets\\R5.png"),pygame.image.load("Assets\\R6.png"),pygame.image.load("Assets\\R7.png"),pygame.image.load("Assets\\R8.png"),pygame.image.load("Assets\\R9.png")]
player_left =  [pygame.image.load("Assets\\L1.png"),pygame.image.load("Assets\\L2.png"),pygame.image.load("Assets\\L3.png"),pygame.image.load("Assets\\L4.png"),pygame.image.load("Assets\\L5.png"),pygame.image.load("Assets\\L6.png"),pygame.image.load("Assets\\L7.png"),pygame.image.load("Assets\\L8.png"),pygame.image.load("Assets\\L9.png")]
isJump = False
jumpCount = 10
walkCount = 0
enemy_right= [pygame.image.load("Assets\\R1E.png"),pygame.image.load("Assets\\R2E.png"),pygame.image.load("Assets\\R3E.png"),pygame.image.load("Assets\\R4E.png"),pygame.image.load("Assets\\R5E.png"),pygame.image.load("Assets\\R6E.png"),pygame.image.load("Assets\\R7E.png"),pygame.image.load("Assets\\R8E.png")]
enemy_left = [pygame.image.load("Assets\\L1E.png"),pygame.image.load("Assets\\L2E.png"),pygame.image.load("Assets\\L3E.png"),pygame.image.load("Assets\\L4E.png"),pygame.image.load("Assets\\L5E.png"),pygame.image.load("Assets\\L6E.png"),pygame.image.load("Assets\\L7E.png"),pygame.image.load("Assets\\L8E.png")]
enemy_attack_left=[pygame.image.load("Assets\\L9E.png"),pygame.image.load("Assets\\L10E.png"),pygame.image.load("Assets\\L11E.png")]
enemy_attack_right=[pygame.image.load("Assets\\R9E.png"),pygame.image.load("Assets\\R10E.png"),pygame.image.load("Assets\\R11E.png")]
walkCount1 = 10
attackCount = 3