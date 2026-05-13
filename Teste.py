import pygame
import sys
# pygame inicio

pygame.init()

# Janelinha
JanelaTamanho = (1800, 900)
TelaCheia = pygame.displayfullscreen()
Janela = pygame.display.set_mode(JanelaTamanho, TelaCheia)

# Janela
clock = pygame.time.Clock()
cor1 = ((100, 40, 255))
cor2 = ((30, 250, 0))
corB = ((255, 255, 255))
alvoPosicao = (100, 100)
#alvo = pygame.Rect((alvoPosicao), (1800/10, 900/10))

# Eventos
run = True
while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

        # Mouse
        #if evento.type == pygame.MOUSEBUTTONDOWN:
            #if alvo.collidepoint(evento.pos):
                #run = False


    Janela.fill((10, 10, 10))

    #Janela2
    #pygame.draw.rect(Janela, corB, alvo)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()