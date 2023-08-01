import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

musica_de_fundo= pygame.mixer.music.load('musica_legal_mp3.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

x = 400
y = 300
velocidade = 20

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo")


executando = True
while executando:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

        comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
            y-= velocidade
    if comandos[pygame.K_DOWN]:
            y+= velocidade
    if comandos[pygame.K_RIGHT]:
            x+= velocidade
    if comandos[pygame.K_LEFT]:
            x-= velocidade

    tela.fill((255, 255, 255))

    
    ret_verde = pygame.draw.rect(tela,(0,255,0),(x,y,40,50))
    ret_vermelho =  pygame.draw.rect(tela,(255,0,0),(200,300,40,50) )

    pygame.display.flip()


pygame.quit()
