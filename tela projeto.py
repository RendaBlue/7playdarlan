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

# muscias ----------------------------------------------------------------------
pygame.mixer.init()
ResetMusic = pygame.USEREVENT
pygame.mixer.music.set_endevent(ResetMusic)
def ResetM():
    pygame.mixer.music.play(-1)
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
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            Run = False

         # Click Mouse/Teclado + Musica
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if Objeto.collidepoint(evento.pos):
                if TC == CorVermelho:
                    TC = CorVerde
                    pygame.mixer.music.play()
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

    #_Texto1 = Musica atual
    Tnome = os.path.splitext(os.path.basename(musicas[LM]))[0]
    Texto = Fonte.render(Tnome, True, CorBranco)
    telaP.blit(Texto, (30,20))

    # _Texto2 = Pausado (ON/OFF)
    NomePause = "Pausado"
    Texto3 = Fonte2.render(NomePause, True, CorVermelho)
    TCentro = Texto3.get_rect(center=(1100, 655))
    if Pausado == True and TC == CorVerde:
        telaP.blit(Texto3, TCentro)

    #_Texto3 = Tempo
    pos = max(0, pygame.mixer.music.get_pos()) // 1000
    minutos = int(pos // 60)
    segundos = int(pos % 60)
    Texto2 = Fonte.render(f"Tempo:{minutos:02}:{segundos:02}/", True, CorBranco)
    TCentro2 = Texto2.get_rect(center=(220, 650))
    telaP.blit(Texto2, TCentro2)

    T1 = MP3(musicas[LM]).info.length
    T1minutos = int(T1 // 60)
    T1segundos = int(T1 % 60)
    Texto2 = Fonte.render(f"{T1minutos:02}:{T1segundos:02}", True, CorCinza)
    TCentro2 = Texto2.get_rect(center=(470 , 650))
    telaP.blit(Texto2, TCentro2)

# Atulização ------------------------------------------------------------------------------------
    pygame.display.flip()
    posX, posY = telaP.get_size()
    telaP.fill((CorCinza))
    pygame.draw.line(telaP, CorPreto, (10, 60), (posX, 60), 100)
    pygame.draw.line(telaP, CorPreto, (10, 660), (posX, 66 0), 100)
    pygame.draw.rect(telaP, CorAzul, (0, 0, posX, posY), 10)
    pygame.draw.rect(telaP, CorBranco, (10, 410, 300, 200))
    pygame.draw.rect(telaP, TC, Objeto)
    Clock.tick(120)

pygame.quit()
sys.exit()
