import pygame

Run = True
while Run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            Run = False

         # Click Mouse/Teclado + Musica
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if Objeto.collidepoint(evento.pos):
                if TC == CorVermelho:
                    TC = CorVerde
                    pygame.mixer.music.play(-1)
                    Pausado = False
                else:
                    TC = CorVermelho
                    pygame.mixer.music.stop()

    # Pausar e despausar a musica
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_1:
            if TC == CorVerde:
                if not Pausado:
                    Pausado = True
                    pygame.mixer.music.pause()
                else:
                    Pausado = False
                    pygame.mixer.music.unpause()

    # Resetar musica
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_q:
            if TC == CorVerde and Pausado == False:
                pygame.mixer.music.play(-1)

    # Troca a musica
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            LM = (LM + 1) % len(musicas)
            pygame.mixer.music.load(musicas[LM])
            if TC == CorVerde:
                pygame.mixer.music.play(-1)

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            LM = (LM - 1) % len(musicas)
            pygame.mixer.music.load(musicas[LM])
            if TC == CorVerde:
                pygame.mixer.music.play(-1)

    # Volume da musica
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 4:
            Volume = min(Volume + 0.1, 1.0)
            pygame.mixer.music.set_volume(Volume)

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 5:
            Volume = max(Volume - 0.1, 0.1)
            pygame.mixer.music.set_volume(Volume)
