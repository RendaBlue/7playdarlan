import pygame
import sys

# Inicialização
pygame.init()
largura, altura = 800, 600
# 1. Adicionar flag RESIZABLE
screen = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
pygame.display.set_caption("Rect no Centro Resizable")
clock = pygame.time.Clock()

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 128, 255)

running = True
while running:
    # 2. Gerenciar eventos de redimensionamento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            # Atualiza o tamanho da tela quando o usuário redimensiona
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    # Limpar a tela
    screen.fill(BRANCO)

    # 3. Calcular centro e desenhar o rect
    rect_largura = 200
    rect_altura = 150

    # Obtém o centro atualizado da janela
    centro_x = screen.get_width() // 2
    centro_y = screen.get_height() // 2

    # Cria o retângulo centralizado
    retangulo = pygame.Rect(0, 0, rect_largura, rect_altura)
    retangulo.center = (centro_x, centro_y)

    # Desenha o retângulo
    pygame.draw.rect(screen, AZUL, retangulo)

    # Atualizar display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
