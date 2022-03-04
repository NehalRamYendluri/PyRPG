import pygame
from global_var import *
from Variables import *
pygame.init()
screen = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Test")
run = True
class player(object):
    def __init__(self,x,y,right,left) -> None:
        self.x = x
        self.y = y
        self.right = right
        self.left = left  
        self.facing = 1  
        self.vel = self.facing * 8
        self.walkCount = 0
        self.right1 = False
        self.left1 = False
        self.health = 100
    def draw(self):
        global player_collide
        player_collide = pygame.draw.rect(screen,(255,0,0),(self.x+25,self.y+10,20,50),1)
        pygame.draw.rect(screen,(255,0,0),(self.x+5,self.y-10,50,10))
        pygame.draw.rect(screen,(0,255,0),(self.x+5,self.y-10,self.health * 1/2,10))
        if self.walkCount + 1 > 27:
            self.walkCount = 0
        if self.right:
            self.x += self.vel
            screen.blit(player_right[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        elif self.left:
            self.x -= self.vel 
            screen.blit(player_left[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        elif self.left1:
            screen.blit(player_left[0],(self.x,self.y)) 
        elif self.right1:
            screen.blit(player_right[0],(self.x,self.y))          
        else:
            screen.blit(player1,(self.x,self.y)) 

class enemies(object):
    def __init__(self,x,y,right,left):
      self.x = x
      self.y = y
      self.right = right
      self.left = left
      self.attacking = False
      self.walkCount = 0
      self.attackCount = 0
      self.attackCooldown = 0
    def draw(self):
        global enemy_collide
        enemy_collide = pygame.draw.rect(screen,(255,0,0),(self.x+25,self.y,20,50),1)
        if self.walkCount + 1 >= 24:
            self.walkCount = 0
        if self.attackCount + 1 >= 9:
            self.attackCount = 0  
        if self.attackCooldown > 0 <= 10:
            self.attackCooldown += 1 
        if self.attackCooldown == 10:
            self.attackCooldown = 0         
        if enemy_collide.colliderect(player_collide):
            if self.left:
              screen.blit(enemy_attack_left[self.attackCount//3],(self.x,self.y))
              self.attackCount += 1
              self.attackCooldown += 1
              if self.attackCount//3 == 1:
                man.health -= 5
            elif self.right:
              screen.blit(enemy_attack_right[self.attackCount//3],(self.x,self.y))    
              self.attackCount += 1
              self.attackCooldown += 1
              if self.attackCount//3 == 1:
                man.health -= 5
        elif man.x > self.x:
            self.x += 5
            screen.blit(enemy_right[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
            self.right = True
            self.left = False
        elif man.x < self.x:
            self.x -= 5
            screen.blit(enemy_left[self.walkCount//3],(self.x,self.y))    
            self.walkCount += 1
            self.left = True
            self.right = False
class map(object):
    def __init__(self,level):
        self.level = level
    def draw(self):
      pass
         
l1 = map(1)                   
def redrawwindow():
    screen.blit(background,(0,0))
    screen.blit(grass,(0,displayHeight - 100))
    man.draw()
    enemy.draw()
    l1.draw()
    enemy1.draw()
                 
man = player(10,displayHeight-160,False,False) 
enemy = enemies(displayWidth-100,displayHeight-150,False,False) 
enemy1 = enemies(displayWidth-300,displayHeight-150,False,False)  
while run:
    pygame.time.delay(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
        keys = pygame.key.get_pressed()
    if keys[ord("d")]:
        man.right = True
        man.left = False
        man.left1 = False
        man.right1 = False
    elif keys[ord("a")]:
        man.right = False
        man.left = True 
    else:
        if man.right:
          man.right1 = True
          man.right = False
          man.left1 = False
          man.left = False
        if man.left: 
          man.left1 = True
          man.right = False
          man.right1 = False
          man.left = False   
    redrawwindow()
    pygame.display.update()        