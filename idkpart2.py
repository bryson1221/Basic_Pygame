import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/VINERITC.ttf',50)

white = (255, 255, 255)
black = (0, 0, 0)

run = True


sky_surface = pygame.image.load('graphics/sp2.jpg').convert()
ground_surface = pygame.image.load('graphics/floor2.jpg').convert()
text_surface = test_font.render('My Game', False, 'White')

enemy_surf = pygame.image.load('graphics/enemy.png').convert_alpha()
enemy_rect = enemy_surf.get_rect(midbottom = (80,300))

player_surf = pygame.image.load('graphics/idle_24.gif').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
            #if player_rect.collidepoint(event.pos): print('collision')

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    enemy_rect.x -= 4
    if enemy_rect.right <= 0: enemy_rect.left = 800
    screen.blit(enemy_surf,enemy_rect)
    screen.blit(player_surf,player_rect)

    #if player_rect.colliderect(enemy_rect):
        #print('collision')
    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint((mouse_pos)):
        #print(pygame.mouse.get_pressed())


    # draw all elements and update everything
    pygame.display.update()
    clock.tick(60)
