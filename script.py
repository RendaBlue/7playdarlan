import pygame

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Área do Mouse")

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Posição do mouse
    x, y = pygame.mouse.get_pos()

    # Área: x entre 100 e 300, y entre 200 e 400
    if 100 <= x <= 300 and 200 <= y <= 400:
        print("Mouse dentro da área!")

    tela.fill((255, 255, 255))

    # Desenha a área monitorada
    pygame.draw.rect(tela, (0, 255, 0), (100, 200, 200, 200))

    pygame.display.flip()

pygame.quit()