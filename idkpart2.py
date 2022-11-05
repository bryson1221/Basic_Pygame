import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/VINERITC.ttf',50)

sky_surface = pygame.image.load('graphics/sp2.jpg').convert()
text_surface = test_font.render('My Game', False, 'White')

enemy_surface = pygame.image.load('graphics/enemy.png').convert_alpha()
enemy_x_pos = 600

player_surf = pygame.image.load('graphics/idle_24.gif').convert_alpha()
player_rect = player_surf.get_rect(topleft = (80,150))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(text_surface,(300,50))
    enemy_x_pos -= 4
    if enemy_x_pos < -100: enemy_x_pos = 800
    screen.blit(enemy_surface,(enemy_x_pos,250))
    print(player_rect.left)
    screen.blit(player_surf,player_rect)

    # draw all elements and update everything
    pygame.display.update()
    clock.tick(60)
