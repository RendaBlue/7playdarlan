import pygame
import math

pygame.init()

tela = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Ícone de Configurações")

BRANCO = (255, 255, 255)
CINZA = (180, 180, 180)
PRETO = (0, 0, 0)

def desenhar_configuracao(superficie, x, y, raio):
    # Dentes da engrenagem
    for angulo in range(0, 360, 45):
        rad = math.radians(angulo)

        x1 = x + math.cos(rad) * (raio - 5)
        y1 = y + math.sin(rad) * (raio - 5)

        x2 = x + math.cos(rad) * (raio + 10)
        y2 = y + math.sin(rad) * (raio + 10)

        pygame.draw.line(superficie, CINZA, (x1, y1), (x2, y2), 6)

    # Corpo da engrenagem
    pygame.draw.circle(superficie, CINZA, (x, y), raio)

    # Furo central
    pygame.draw.circle(superficie, PRETO, (x, y), raio // 3)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(BRANCO)

    desenhar_configuracao(tela, 200, 150, 40)

    pygame.display.flip()

pygame.quit()