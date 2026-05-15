import pygame

# Inicialização
pygame.init()
tela = pygame.display.set_mode((400, 300))
preto = (0, 0, 0)
branco = (255, 255, 255)

# Preencher o fundo de branco para a linha aparecer
tela.fill(branco)

# Desenhar linha: superfície, cor, (x_inicio, y_inicio), (x_fim, y_fim), espessura
pygame.draw.line(tela, preto, (0, 50), (300, 50), 20)

# Atualizar a tela
pygame.display.flip()

# Loop para manter a janela aberta
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

pygame.quit()
