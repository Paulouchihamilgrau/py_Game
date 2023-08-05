import pygame
from sys import exit
from random import randint


pygame.init()


pygame.mixer.music.load('musica_legal_mp3.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

largura = 800
altura = 600
x = int(largura/2)
y = int(altura/2)

x_azul = randint(40,600)
y_azul = randint(50, 430)

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
        y -= 20
    if comandos[pygame.K_DOWN]:
        y += 20
    if comandos[pygame.K_RIGHT]:
        x += 20
    if comandos[pygame.K_LEFT]:
        x -= 20

    tela.fill((255, 255, 255))

    ret_verde = pygame.draw.rect(tela, (0, 255, 0), (x, y, 40, 50))
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x_azul, y_azul, 40, 50))

    if ret_verde.colliderect(ret_vermelho):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)

    pygame.display.flip()


pygame.quit()

