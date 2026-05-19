import pygame
from mutagen.mp3 import MP3

pygame.init()

Tela = pygame.display.set_mode((800, 300))
Clock = pygame.time.Clock()

# Música
Musica = "musica.mp3"

pygame.mixer.music.load(Musica)
pygame.mixer.music.play()

# Duração total da música
audio = MP3(Musica)
Duracao = audio.info.length

# Barra
BarraX = 100
BarraY = 200
BarraLargura = 600
BarraAltura = 20

Rodando = True

while Rodando:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            Rodando = False

        # Clique na barra
        if event.type == pygame.MOUSEBUTTONDOWN:

            mx, my = pygame.mouse.get_pos()

            if BarraX <= mx <= BarraX + BarraLargura:
                if BarraY <= my <= BarraY + BarraAltura:

                    # Porcentagem clicada
                    porcentagem = (mx - BarraX) / BarraLargura

                    # Tempo novo
                    novo_tempo = Duracao * porcentagem

                    # Toca a música nesse tempo
                    pygame.mixer.music.play(start=novo_tempo)

    Tela.fill((30, 30, 30))

    # Tempo atual
    tempo_atual = pygame.mixer.music.get_pos() / 1000

    # Corrige caso fique negativo
    tempo_atual = max(0, tempo_atual)

    # Porcentagem atual
    progresso = tempo_atual / Duracao

    # Tamanho da barra preenchida
    largura_preenchida = BarraLargura * progresso

    # Barra vazia
    pygame.draw.rect(Tela, (80, 80, 80),
                     (BarraX, BarraY, BarraLargura, BarraAltura))

    # Barra preenchida
    pygame.draw.rect(Tela, (0, 200, 0),
                     (BarraX, BarraY,
                      largura_preenchida, BarraAltura))

    pygame.display.update()
    Clock.tick(60)

pygame.quit()