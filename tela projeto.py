import pygame
from mutagen.mp3 import MP3
import sys
import os
import random
import re

from pygame.constants import K_KP_ENTER

pygame.init()

# ======================================================================================
# Cores |-------------------------------------------------------------------------------
# ======================================================================================
CorAzul = (0, 0, 255)
CorVerde = (0, 255, 0)
CorVermelho = (255, 0, 0)
CorPreto = (0, 0, 0)
CorBranco = (255, 255, 255)
CorCiano = (0, 255, 255)
CorCinza = (100, 100, 100)
CorLaranja = (255, 125, 0)
CorAzulEstranho = (0, 155, 155)
CorAmarelo = (255, 255, 0)
CorVerdeDark = (0, 100, 0)
# ==================================================================
# Fontes |----------------------------------------------------------
# ==================================================================
Fonte = pygame.font.SysFont("Comic Sans", 40, True)
Fonte2 = pygame.font.SysFont("none", 100, False)
Fonte3 = pygame.font.SysFont("Calibri", 35, True)

# =========================================================================================
# Sistema de Muscias |---------------------------------------------------------------------
# =========================================================================================
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
T1 = MP3(musicas[LM]).info.length
RectMusic = []

# ========================================================================================
# Tela Codigo |---------------------------------------------------------------------------
# ========================================================================================
TelaMobile = 1280, 720
TelaMonitor = 1920, 1080
Info = pygame.display.Info()
TamanhoTela = (Info.current_w, Info.current_h)
telaP = pygame.display.set_mode((TelaMobile), pygame.RESIZABLE)
pygame.display.set_caption("Tela")
posX, posY = telaP.get_size()
Clock = pygame.time.Clock()

# ===================================================================================
# Variaveis |------------------------------------------------------------------------
# ===================================================================================

Tempo = 0
UPos = 0
Scroll = 0
VelScroll = 30

Interface = 0
PosicaoCelular = True

# Tempo de Barra
BarraTempoX = 165 # incio
BarraTempoY = posY-45

BarraLargura = posX-165-BarraTempoX # tamanho
BarraAltura = 20

TempoInicial = 0

# ==========================================================================================
# Outros |----------------------------------------------------------------------------------
# ==========================================================================================
TC = CorVermelho
Pausado = False
Infor = pygame.display.get_desktop_sizes()
PlayStop = pygame.Rect(10, 85, 86, 86)
ClickList = pygame.Rect(106, 85, posX-116, posY-170)

# ========================================================================================
# Sistema |-------------------------------------------------------------------------------
# ========================================================================================

Run = True
while Run:
    telaP.fill(CorBranco)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            Run = False

        if evento.type == pygame.VIDEORESIZE:

            posX = evento.w
            posY = evento.h

            BarraTempoY = posY - 45
            BarraLargura = posX-165-BarraTempoX


# ==========================================================================================================
# -----| Mouse + Musica |-----------------------------------------------------------------------------------
# ==========================================================================================================

    # Barra de Tempo ==================================================================
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            mx, my = pygame.mouse.get_pos()

            if BarraTempoX <= mx <= BarraTempoX + BarraLargura:
                if BarraTempoY-15 <= my <= BarraTempoY + BarraAltura:

                    Porcentagem = (mx - BarraTempoX) / BarraLargura
                    Ntempo = T1 * Porcentagem
                    print(Ntempo)

                    if TC == CorVerde:
                        TempoInicial = Ntempo
                        pygame.mixer.music.play(start=Ntempo)

                        if Pausado:
                            pygame.mixer.music.pause()

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if PlayStop.collidepoint(evento.pos):

                if TC == CorVerde:
                    if not Pausado:
                        Pausado = True
                        pygame.mixer.music.pause()
                    else:
                        Pausado = False
                        pygame.mixer.music.unpause()

        # Click na Musica para Selecionar =====================================
            mx, my = evento.pos

            for rect, indice in RectMusic:

                if rect.collidepoint(mx, my) and ClickList.collidepoint(mx, my):
                    LM = indice
                    pygame.mixer.music.load(musicas[LM])
                    T1 = MP3(musicas[LM]).info.length
                    Pausado = False

                    if TC == CorVerde and Pausado == False:
                        pygame.mixer.music.play()
                        TempoInicial = 0

                    break

    # Rodinha do Mouse para mover a musica para cima e para baixo =============

        if evento.type == pygame.MOUSEWHEEL:
            Scroll -= evento.y * VelScroll

            LimiteScroll = max(0, AltConteudo - posY+252)
            Scroll = max(0, min(Scroll, LimiteScroll))

# =================================================================================
# Teclado + Musica |---------------------------------------------------------------
# =================================================================================

            # Botão de Play e Stop ================================================

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:

            if TC == CorVermelho:
                TC = CorVerde
                pygame.mixer.music.play()
                Pausado = False
            else:
                TC = CorVermelho
                pygame.mixer.music.stop()
                TempoInicial = 0

        # Atulizar a Lista de Musica ==============================================

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
            musicas = [
        os.path.join(Pmusicas, musica)
        for musica in os.listdir(Pmusicas)
        if musica.endswith(".mp3")
        ]

    # Pausar e Despausar a musica ===============================================

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_1:
            if TC == CorVerde:
                if not Pausado:
                    Pausado = True
                    pygame.mixer.music.pause()
                else:
                    Pausado = False
                    pygame.mixer.music.unpause()

    # Resetar musica =============================================================

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_q:
            if TC == CorVerde and Pausado == False:
                pygame.mixer.music.play()

    # Trocando a Musica para Baixo ===============================================

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            LM = (LM + 1) % len(musicas)
            pygame.mixer.music.load(musicas[LM])
            T1 = MP3(musicas[LM]).info.length
            TempoInicial = 0
            Pausado = False
            pygame.mixer.music.unpause()
            if TC == CorVerde and Pausado == False:
                pygame.mixer.music.play()

    # Trocando a Musica Para Cima ================================================

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            LM = (LM - 1) % len(musicas)
            pygame.mixer.music.load(musicas[LM])
            T1 = MP3(musicas[LM]).info.length
            TempoInicial = 0
            Pausado = False
            pygame.mixer.music.unpause()
            if TC == CorVerde and Pausado == False:
                pygame.mixer.music.play()

    # Trocar a Musica Automaticamnete =========================================

        if evento.type == ResetMusic and not TC == CorVermelho:
            LM = (LM + 1) % len(musicas)
            pygame.mixer.music.load(musicas[LM])
            T1 = MP3(musicas[LM]).info.length
            TempoInicial = 0
            Pausado = False
            pygame.mixer.music.unpause()
            if TC == CorVerde:
                pygame.mixer.music.play()

    # Volume da Musica / Diminuir e Aumentar ===================================================

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            Volume = min(Volume + 0.1, 1.0)
            pygame.mixer.music.set_volume(Volume)

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            Volume = max(Volume - 0.1, 0.1)
            pygame.mixer.music.set_volume(Volume)

# ======================================================================================
# Lista de Musicas |--------------------------------------------------------------------
# ======================================================================================

    pygame.draw.rect(telaP, CorAzulEstranho, ClickList) # fundo da lista
    Tnome = os.path.splitext(os.path.basename(musicas[LM]))[0]
    Tnome = re.sub(r'^[0-9.\- ]+', '', Tnome)
    RectMusic.clear()
    Tpy = 90 - Scroll
    AltConteudo = len(musicas) * 46
    Scroll = max(0, min(Scroll, AltConteudo - posY+252))
    for i, musica in enumerate(musicas):
        T2nome = os.path.splitext(os.path.basename(musica))[0]
        T2nome = re.sub(r'^[0-9.\- ]+', '', T2nome)
        Objeto2 = pygame.Rect(110, Tpy, posX-125, 45)
        ObjetoCor = CorCinza
        if i == LM:
            MusicCor = CorAmarelo
            ObjetoCor = CorVerdeDark
        else:
            MusicCor = CorLaranja
            ObjetoCor = CorPreto
        ObjetoD2 = pygame.draw.rect(telaP, ObjetoCor, Objeto2)
        TextoT2 = Fonte3.render(T2nome, True, MusicCor)
        PosMusic = (120, Tpy+5)
        if 55 < Tpy < posY-100:
            telaP.blit(TextoT2, PosMusic)
            RectMusic.append((Objeto2, i))
        Tpy += 50


    # Sistema de Tempo da Musica
    if TC == CorVerde:
        if not Pausado:
            pos = (pygame.mixer.music.get_pos() / 1000) + TempoInicial

    elif TC == CorVermelho:
        pos = 0

    # Tempo Atual da Musica
    minutos = int(pos // 60)
    segundos = int(pos % 60)
    TextoT1 = Fonte.render(f"{minutos:02}:{segundos:02}", True, CorBranco)

    # Tempo Total da Musica
    T1minutos = int(T1 // 60)
    T1segundos = int(T1 % 60)
    TextoT2 = Fonte.render(f"{T1minutos:02}:{T1segundos:02}", True, CorBranco)

# Atulização ------------------------------------------------------------------------------------

    pygame.draw.line(telaP, CorPreto, (10, 42), (posX-10, 42), 65) # Linha Preta Cima
    pygame.draw.line(telaP, CorPreto, (10, posY-43), (posX-10, posY-43), 65) # Linha Preta Baixo
    pygame.draw.line(telaP, CorAzul, (100, 85), (100, posY-80), 10)  # Linha Azul Meio
    #pygame.draw.line(telaP, CorAzul, (10, 415), (310,  415), 10) # Linha Azul Meio Esquerda
    pygame.draw.rect(telaP, CorAzul, (0, 0, posX, posY), 10) # Borda azul da Janela
    pygame.draw.rect(telaP, CorAzul, (0, 75, posX, posY-150), 10) # Borda Mais Dentro da Janela
    pygame.draw.rect(telaP, CorCinza, (10, 85, 86, posY-170)) # Linha Cinza das Funções



    # Barra de Tempo da Musica
    pygame.draw.line(telaP, CorAzulEstranho, (BarraTempoX, BarraTempoY), (BarraTempoX + BarraLargura, BarraTempoY), BarraAltura)

    # Sistema da Bolinha do Tempo
    if T1 > 0:
        Progresso = pos / T1
    else:
        Progresso = 0

    Progresso = max(0, min(Progresso, 1))
    BolinhaX = BarraTempoX + (BarraLargura * Progresso)
    BolinhaX = max(BarraTempoX,min(BolinhaX, BarraTempoX + BarraLargura))

    # Barra Sendo Preenchida
    pygame.draw.line(telaP, CorAmarelo, (BarraTempoX, BarraTempoY), (BolinhaX, BarraTempoY), BarraAltura)

    # Bolinha do Tempo
    pygame.draw.circle(telaP, CorLaranja, (int(BolinhaX), posY-45), 20)

    pygame.draw.rect(telaP,CorVermelho,(10+10, posY-165, 86-20, 86-20),border_radius=10) # Encerrar a Musica

    if Pausado == True:
        pygame.draw.polygon(telaP,CorBranco,[(85 ,129),(20, 93),(20, 162)])# Pause e Despause
    elif Pausado == False:
        pygame.draw.line(telaP, CorBranco,(35, 93),(35, 160),20,)
        pygame.draw.line(telaP, CorBranco, (68, 93), (68, 160), 20)
    # Loop
    # Encerar

    # Nome da música atual =======================================
    TextoMusic = Fonte.render(Tnome, True, CorBranco)
    TextoMusicCenter = TextoMusic.get_rect(center=(posX/2, 35))
    telaP.blit(TextoMusic, TextoMusicCenter)

    # Tempo =======================================================
    telaP.blit(TextoT1, (20, posY-75)) # Atual
    telaP.blit(TextoT2, (posX-130, posY-75)) # Total

    # Pausado ==================================================
    #if Pausado and TC == CorVerde:
        #telaP.blit(Texto3, (15, 535))

    pygame.display.flip()
    Clock.tick(60)

pygame.quit()
sys.exit()
