import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()
running = True
dt = 0
grass = pygame.image.load("Programing/Python/Limited Survival/grass.png")
speed_x = 300

Jumping = False

y_grav = 1
jump_height = 1
y_vel = jump_height

x,y = pygame.mouse.get_pos()

env_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
mouse_pos = pygame.mouse.get_pos()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(360, 360))
        self.rect = pygame.Rect((screen.get_width() / 2, screen.get_height() / 2), (25,25))
        self.jumping = False
        self.y_grav = 1
        self.jump_height = 20
        self.y_vel = self.jump_height
        self.speed_x = 300
        self.speed_y = 10

    def update(self, env_pos):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self.speed_x = 5
        else:
            self.speed_x = 3
        if keys[pygame.K_d]:
            env_pos.x -= self.speed_x
            for element in blocks:
                element.rect.x -= self.speed_x
        if keys[pygame.K_a]:
            env_pos.x += self.speed_x
            for element in blocks:
                element.rect.x += self.speed_x
        if keys[pygame.K_SPACE]:
            self.jumping = True
        if keys[pygame.K_ESCAPE]:
            env_pos.y = 420
            for element in blocks:
                element.rect.x = 420
        if self.jumping:
            self.temp_env_posy = env_pos.y
            env_pos.y += self.y_vel
            for element in blocks:
                element.rect.y += self.y_vel
            self.y_vel -= self.y_grav
            if self.y_vel <= -self.jump_height:
                self.jumping = False
                self.y_vel = self.jump_height
        for block in blocks:
            if self.rect.colliderect(islandblock.rect) == False and not self.rect.colliderect(block.rect) and not self.jumping:
                env_pos.y -= self.speed_y
                block.rect.y -= self.speed_y

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        # self.image = pygame.image.load("Programing/Python/Limited Survival/grass.png")
        # self.image = pygame.transform.scale(self.image, (25,25))
        self.image.fill((25, 207, 70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x
        self.rect.y
        # if player.rect.colliderect(block.rect) == False and not player.rect.colliderect(islandblock.rect) and not Jumping:
        #     self.rect.y -= 1

class IslandBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image = pygame.image.load("Programing/Python/Limited Survival/grass.png")
        self.image = pygame.transform.scale(self.image, (25,25))
        # self.image.fill((25, 207, 70))
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect((self.rect.x, self.rect.y), (25,25))

    def update(self):
        self.rect.x = env_pos.x
        self.rect.y = env_pos.y
        # if player.rect.colliderect(block.rect) == False and not player.rect.colliderect(islandblock.rect) and not Jumping:
        #     self.rect.y -= 1
        

player = Player()
islandblock = IslandBlock()
block = Block(x,y)
blocks = pygame.sprite.Group()
blocks.add(islandblock)
player_group = pygame.sprite.Group()
player_group.add(player)
all_group = pygame.sprite.Group([player, islandblock])

while running:

    screen.fill("blue")
    mouse_pos = pygame.mouse.get_pos()
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_pos = pygame.mouse.get_pos()
        #     new_block_pos = (mouse_pos[0], mouse_pos[1])
        #     all_group.add(block)
        #     blocks.add(block)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 1 is the left mouse button
                x, y = pygame.mouse.get_pos()
                block = Block(x, y)
                all_group.add(block)
                blocks.add(block)
                
    # screen.blit(bg, (wall_pos.x, wall_pos.y))
    # bgrect = pygame.Rect(wall_pos.x, wall_pos.y, 2295, 1050)


    mouseRect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, 10)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_d]:
    #     env_pos.x -= speed_x * dt
    # if keys[pygame.K_a]:
    #     env_pos.x += speed_x * dt
    # if keys[pygame.K_LSHIFT]:
    #     speed_x = 500
    # else:
    #     speed_x = 300
    # if keys[pygame.K_SPACE]:
    #     Jumping = True
    # if keys[pygame.K_ESCAPE]:
    #     env_pos.y = 420
    #     block.rect.y = 420
        
    # if Jumping:
    #     env_pos.y += y_vel
    #     y_vel -= y_grav
    #     if y_vel < -jump_height:
    #         Jumping = False
    #         y_vel = jump_height
    
    player.update(env_pos)
    blocks.update()
    screen.blit(player.image, (375,375))

    for block in blocks:
        screen.blit(block.image, block.rect)
    # if player.rect.colliderect(block.rect) == False or player.rect.colliderect(islandblock.rect) == False and not Jumping:
    #      env_pos.y -= 1
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()