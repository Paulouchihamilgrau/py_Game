import pygame
pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo")


executando = True
while executando:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    
    tela.fill((0, 0, 0))

    
    pygame.display.flip()


pygame.quit()
