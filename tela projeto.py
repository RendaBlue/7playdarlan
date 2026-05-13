import pygame
import sys
#import time
#import os

pygame.init()

# Cores ---------------------------------------------------------------------------------
CorAzul = (0, 0, 255)
CorVerde = (0, 255, 0)
CorVermelho = (255, 0, 0)
CorPreto = (0, 0, 0)
CorBranco = (255, 255, 255)

# Fonte ------
Fonte = pygame.font.SysFont("Comic Sans", pygame.SCALED // 10, True)
Fonte2 = pygame.font.SysFont("none", 300, False)

# muscias ----------------------------------------------------------------------
pygame.mixer.init()
def ResetM():
    pygame.mixer.music.play(-1)
M1 = '109. Graveyard Ops Combat A High loop.mp3'
M2 = '121. Graveyard Ops Combat B High loop.mp3'
M3 = '129. Graveyard Ops Combat C High loop.mp3'
musicas = [M1, M2, M3]
LM = 0
Volume = 0.5
pygame.mixer.music.set_volume(Volume)
pygame.mixer.music.load(musicas[LM])
Tempo = pygame.mixer.music.get_pos()
tempoS = Tempo // 1000
temp_aux = 0

# Tela Codigo ----------------------------------------------------------------------------
Info = pygame.display.Info()
TamanhoTela = (Info.current_w, Info.current_h)

# Tela Principal ------------------------------------------------------------------------
telaP = pygame.display.set_mode((1800, 900), pygame.RESIZABLE)
pygame.display.set_caption("Tela")
Clock = pygame.time.Clock()

# Outros -----------------------------------------------------------------------------------
TC = CorVermelho
Pausado = False
Infor = pygame.display.get_desktop_sizes()
y = 300
x = 300
Objeto = pygame.Rect(x, y, 100, 100)

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
                    pygame.mixer.music.play(-1)
                    Pausado = False
                else:
                    TC = CorVermelho
                    pygame.mixer.music.stop()

    # Pausar e despausar a musica
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_1:
            if Pausado == False and TC == CorVerde:
                Pausado = True
                pygame.mixer.music.pause()
            else:
                Pausado = False
                pygame.mixer.music.unpause()

    # Resetar musica
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_q:
            pygame.mixer.music.rewind()

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

        # Tela Cheia -----------------------------------------------------------------------------
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()

        Teclas = pygame.key.get_pressed()

    if Teclas[pygame.K_w]:
        y -= 20
    if Teclas[pygame.K_s]:
        y += 20
    if Teclas[pygame.K_a]:
        x -= 20
    if Teclas[pygame.K_d]:
        x += 20

    x = max(20, min(x, 1800 - 120))
    y = max(20, min(y, 900 - 120))

    Objeto.x = x
    Objeto.y = y
# Mensagem ------------------------------------------------------------------------------------

    #_Texto1 = Monitor
    Tnome = "Tamanho do monitor: " + (str(Infor)).replace("(","").replace(")", "").replace(",", " x").replace("[","").replace("]","")
    Texto = Fonte.render(Tnome, True, CorBranco)
    TCentro = Texto.get_rect(center=(470, 50))
    telaP.blit(Texto, TCentro)

    #_Texto2 = Tempo
    if tempoS == -1:
        tempoS = temp_aux

    Texto2 = Fonte.render(f"Segundos: {tempoS}", True, CorBranco)
    temp_aux = tempoS
    TCentro2 = Texto2.get_rect(center=(300, 820))
    telaP.blit(Texto2, TCentro2)

    #_Texto3 = Pausado (ON/OFF)
    NomePause = "Pausado"
    Texto3 = Fonte2.render(NomePause, True, CorVermelho)
    if Pausado == True and TC == CorVerde:
        telaP.blit(Texto3, (200, 200))

# Atulização ------------------------------------------------------------------------------------
    pygame.display.flip()
    posX, posY = telaP.get_size()
    telaP.fill((0, 0, 0))
    cubo = pygame.draw.rect(telaP, CorAzul, (0, 0, posX, posY), 20)
    pygame.draw.rect(telaP, TC, Objeto)
    Clock.tick(120)

pygame.quit()
sys.exit()
