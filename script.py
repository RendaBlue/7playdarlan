# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

pygame.init()

LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))

BRANCO = (255,255,255)
PRETO = (0,0,0)
CYAN = (0,172,193)

x, y = 400, 500
tamanho = 50

alvo_x = random.randint(0,750)
alvo_y = 0
velocidade = 5


# Pontuação
pontos = 0

rodando = True
relogio = pygame.time.Clock()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT] and x > 0:
        x -= 10
    if teclas[pygame.K_RIGHT] and x < LARGURA - tamanho:
        x += 10

    if alvo_y > ALTURA:
        alvo_y = 0
        alvo_x = random.randint(0, LARGURA - 40)



    alvo_y += velocidade

    tela.fill(PRETO)

    jogador = pygame.draw.rect(tela, CYAN, (x, y, tamanho, tamanho))
    alvo = pygame.draw.rect(tela, (255,0,0), (alvo_x,alvo_y,40,40))

    # Colisão
    if jogador.colliderect(alvo):
        print("Colisão!")


        pontos += 1
        print(pontos)
        # Reinicia o alvo
        alvo_y = 0
        alvo_x = random.randint(0, LARGURA - alvo_x)

    pygame.display.flip()
    relogio.tick(60)


pygame.quit()






















