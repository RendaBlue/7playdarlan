import pygame
import sys

pygame.init()
Tela = pygame.display.set_mode((1200, 800),pygame.RESIZABLE)
clock = pygame.time.Clock()

x, y = 100, 100
x2 = 100
y2 = 100
Vel = 10

corRosa = (255, 255, 255, 155)
corBranco = (255, 255, 255)

Run = True
while Run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN and evento.key == pygame.K_F11:
                Run = False

    Teclas = pygame.key.get_pressed()

    if Teclas[pygame.K_UP]:
        y -= Vel
    if Teclas[pygame.K_DOWN]:
        y += Vel
    if Teclas[pygame.K_LEFT]:
        x -= Vel
    if Teclas[pygame.K_RIGHT]:
        x += Vel

    if Teclas[pygame.K_w]:
        y2 -= Vel
    if Teclas[pygame.K_s]:
        y2 += Vel
    if Teclas[pygame.K_a]:
        x2 -= Vel
    if Teclas[pygame.K_d]:
        x2 += Vel

    x2 = max(60, min(x2, 1200))
    y2 = max(60, min(y2, 800))

    x = max(0, min(x, 1200 - x2))
    y = max(0, min(y, 800 - y2))

    pygame.display.flip()
    Tela.fill((0, 0, 0))
    Objeto = pygame.Rect(x, y, x2, y2)
    pygame.draw.rect(Tela, corRosa, Objeto,20)

    clock.tick(60)

pygame.quit()
sys.exit()
