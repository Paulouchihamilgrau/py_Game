import pygame
pygame.init()

x = 400
y = 300
velocidade = 10

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

    tela.fill((0, 0, 0))

    
    pygame.draw.circle(tela,(0,255,0),(x,y),50)
    pygame.display.update()

pygame.quit()
