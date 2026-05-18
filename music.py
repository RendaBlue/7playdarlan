import pygame

TelaMobile = pygame.display.set_mode((720, 1280), pygame.FULLSCREEN)

pygame.init()

TelaMobile.fill((255, 255, 255))


Run = True
while Run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            Run = False

    pygame.display.update()
    TelaMobile.fill((255, 255, 255))

pygame.quit()



