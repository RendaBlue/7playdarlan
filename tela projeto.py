import pygame
from mutagen.mp3 import MP3
import sys
import os

pygame.init()

# Cores ---------------------------------------------------------------------------------
CorAzul = (0, 0, 255)
CorVerde = (0, 255, 0)
CorVermelho = (255, 0, 0)
CorPreto = (0, 0, 0)
CorBranco = (255, 255, 255)
CorCiano = (0, 255, 255)
CorCinza = (100, 100, 100)

# Fonte ------
Fonte = pygame.font.SysFont("Comic Sans", 50, True)
Fonte2 = pygame.font.SysFont("none", 100, False)
Fonte3 = pygame.font.SysFont("Arial", 40, True)

# muscias ----------------------------------------------------------------------
pygame.mixer.init()
ResetMusic = pygame.USEREVENT
pygame.mixer.music.set_endevent(ResetMusic)
def ResetM():
    pygame.mixer.music.play()
Pmusicas = "../musicas/"

musicas = [
    os.path.join(Pmusicas, musica)
    for musica in os.listdir(Pmusicas)
    if musica.endswith(".mp3")
]
LM = 0
ListMusic = os.path.basename(musicas[0])
Volume = 0.5
pygame.mixer.music.set_volume(Volume)
pygame.mixer.music.load(musicas[LM])
RectMusic = []

# Tela Codigo ----------------------------------------------------------------------------
Info = pygame.display.Info()
TamanhoTela = (Info.current_w, Info.current_h)

# Tela Principal ------------------------------------------------------------------------
telaP = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Tela")
Clock = pygame.time.Clock()
Tempo = 0
UPos = 0

# Outros -----------------------------------------------------------------------------------
TC = CorVermelho
Pausado = False
Infor = pygame.display.get_desktop_sizes()
Objeto = pygame.Rect(10, 110, 300, 300)

# Sistema --------------------------------------------------------------------------------
Run = True
while Run:
    telaP.fill(CorCinza)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            Run = False

         # Click Mouse/Teclado + Musica
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

            # Botão play/stop
            if Objeto.collidepoint(evento.pos):
                if TC == CorVermelho:
                    TC = CorVerde
                    pygame.mixer.music.play()
                    Pausado = False
                else:
                    TC = CorVermelho
                    pygame.mixer.music.stop()

            # Clique na lista de músicas
            for rect, indice in RectMusic:

                if rect.collidepoint(evento.pos):
                    LM = indice
                    pygame.mixer.music.load(musicas[LM])

                    if TC == CorVerde:
                        pygame.mixer.music.play()

                    break

#        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
#            if Objeto.collidepoint(evento.pos):
#                if TC == CorVermelho:
#                    TC = CorVerde
#                    pygame.mixer.music.play()
#                    Pausado = False
#                else:
#                    TC = CorVermelho
#                    pygame.mixer.music.stop()

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
                pygame.mixer.music.play()

    # Troca a musica
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            LM = (LM + 1) % len(musicas)
            pygame.mixer.music.load(musicas[LM])
            if TC == CorVerde:
                pygame.mixer.music.play()

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            LM = (LM - 1) % len(musicas)
            pygame.mixer.music.load(musicas[LM])
            if TC == CorVerde:
                pygame.mixer.music.play()

        if evento.type == ResetMusic and not TC == CorVermelho:
            LM = (LM + 1) % len(musicas)
            pygame.mixer.music.load(musicas[LM])
            if TC == CorVerde:
                pygame.mixer.music.play()

    # Volume da musica
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 4:
            Volume = min(Volume + 0.1, 1.0)
            pygame.mixer.music.set_volume(Volume)

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 5:
            Volume = max(Volume - 0.1, 0.1)
            pygame.mixer.music.set_volume(Volume)

# Mensagem ------------------------------------------------------------------------------------

    #_Texto1 = Musicas
    Tnome = os.path.splitext(os.path.basename(musicas[LM]))[0]
    #Texto = Fonte.render(Tnome, True, CorBranco)
    #telaP.blit(Texto, (30, 10))
    RectMusic.clear()
    Tpy = 110

    for i, musica in enumerate(musicas):
        T2nome = os.path.splitext(os.path.basename(musica))[0]
        if i == LM:
            MusicCor = CorVermelho
        else:
            MusicCor = CorBranco
        TextoT2 = Fonte3.render(T2nome, True, MusicCor)
        PosMusic = (330, Tpy)
        telaP.blit(TextoT2, PosMusic)
        RectTexto = TextoT2.get_rect(topleft=PosMusic)
        RectMusic.append((RectTexto, i))
        Tpy += 55



    # _Texto2 = Pausado (ON/OFF)
    NomePause = "Pausado"
    Texto3 = Fonte2.render(NomePause, True, CorVermelho)
    #if Pausado == True and TC == CorVerde:
    #    telaP.blit(Texto3, (15, 535))

    #_Texto3 = Tempo
    #pos = max(0, pygame.mixer.music.get_pos()) // 1000
    pos = pygame.mixer.music.get_pos() / 1000

    if pos < 0:
        pos = 0
    minutos = int(pos // 60)
    segundos = int(pos % 60)
    T1 = MP3(musicas[LM]).info.length
    T1minutos = int(T1 // 60)
    T1segundos = int(T1 % 60)
    TextoT1 = Fonte.render(f"{minutos:02}:{segundos:02}", True, CorPreto)
    TextoT2 = Fonte.render(f"{T1minutos:02}:{T1segundos:02}", True, CorPreto)
    #telaP.blit(TextoT1, (20, 410))
    #telaP.blit(TextoT2, (20, 460))

# Atulização ------------------------------------------------------------------------------------
    posX, posY = telaP.get_size()
    pygame.draw.line(telaP, CorPreto, (10, 50), (posX, 50), 100) # Linha Preta Cima
    pygame.draw.line(telaP, CorPreto, (10, 660), (posX, 660), 100) # Linha Preta Baixo
    pygame.draw.line(telaP, CorAzul, (314, 110), (314, 610), 10)  # Linha Azul Meio
    pygame.draw.line(telaP, CorAzul, (10, 415), (310,  415), 10) # Linha Azul Meio Esquerda
    pygame.draw.rect(telaP, CorAzul, (0, 0, posX, posY), 10)
    pygame.draw.rect(telaP, CorAzul, (0, 100, posX, posY-200), 10)
    pygame.draw.rect(telaP, CorCiano, (10, 420, 300, 190))
    pygame.draw.rect(telaP, TC, Objeto, 25)


    pygame.draw.rect(telaP, TC, Objeto, 25)

    # Nome da música atual
    Texto = Fonte.render(Tnome, True, CorBranco)
    telaP.blit(Texto, (30, 10))

    # Tempo
    telaP.blit(TextoT1, (20, 410))
    telaP.blit(TextoT2, (20, 460))

    # Pausado
    if Pausado and TC == CorVerde:
        telaP.blit(Texto3, (15, 535))

    pygame.display.flip()
    Clock.tick(120)

pygame.quit()
sys.exit()
