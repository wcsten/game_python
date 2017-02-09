import pygame
from pygame.locals import *

screenDimension = (500, 500)
screen = pygame.display.set_mode(screenDimension, 0, 32)

player = pygame.image.load('./imagens/mario2.png')
keys = [False, False, False, False]
playerpos = [200, 100]
velocidade = 3.0

while True:

    screen.blit(player, playerpos)
    pygame.display.flip()
    screen.fill(0)

    pygame.draw.polygon(screen, (0, 255, 0), ( (10, 250), (250, 110), (500, 250), (250, 390), (10, 250) ), 0)
    pygame.draw.line(screen, (170, 150, 0), (9, 270), (250, 410), 42)
    pygame.draw.line(screen, (100, 80, 0), (250, 410), (499, 270), 42)

    casa = pygame.image.load('./imagens/castel.png')
    screen.blit(casa, (80, 90) )




    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

    if keys[0]:
        playerpos[1] -= velocidade
    elif keys[2]:
        playerpos[1] += velocidade
    elif keys[1]:
        playerpos[0] -= velocidade
    elif keys[3]:
        playerpos[0] += velocidade

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
