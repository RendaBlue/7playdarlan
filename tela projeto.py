import pygame
from mutagen.mp3 import MP3
import sys
import os
import random
import re

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
telaP = pygame.display.set_mode(TelaMobile, pygame.RESIZABLE)
pygame.display.set_caption("Tela")
posX, posY = telaP.get_size()
Clock = pygame.time.Clock()

# ===================================================================================
# Variaveis |------------------------------------------------------------------------
# ===================================================================================

Scroll = 0
VelScroll = 30

Interface = 0

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
Loop = False
Pausado = False
Arrastar = False
Infor = pygame.display.get_desktop_sizes()

BotaoEncerrar = pygame.Rect(10, posY-175-3, 86, 91)
PlayStop = pygame.Rect(10, 85, 86, 91)
BAleatorio = pygame.Rect(10, 200, 86, 91)
#pygame.draw.rect(telaP, CorVermelho, (PF[0], 265+45, PF[2], PF[3]))
#pygame.draw.rect(telaP, CorBranco, (PF[0], 355+70, PF[2], PF[3]))
ClickList = pygame.Rect(106, 85, posX-116, posY-170)
Bolinha = pygame.Rect(BarraTempoX-20, BarraTempoY-20, 40, BarraAltura+20)
BarraTTotal = pygame.Rect(BarraTempoX, BarraTempoY-15, BarraLargura, BarraAltura+15)

mx, my = pygame.mouse.get_pos()

PF = 10, 0, 86, 91

# ========================================================================================
# Sistema |-------------------------------------------------------------------------------
# ========================================================================================

Run = True
while Run:
    telaP.fill(CorCinza)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            Run = False

        if evento.type == pygame.VIDEORESIZE:

            posX = evento.w
            posY = evento.h

            BarraTempoY = posY - 45
            BarraLargura = posX-165-BarraTempoX
            BarraTTotal = pygame.Rect(BarraTempoX, BarraTempoY - 15, BarraLargura, BarraAltura + 15)
            Bolinha = pygame.Rect(BarraTempoX - 20, BarraTempoY - 20, 40, BarraAltura + 20)
            ClickList = pygame.Rect(106, 85, posX - 116, posY - 170)

# ==========================================================================================================
# -----| Mouse + Musica |-----------------------------------------------------------------------------------
# ==========================================================================================================

    # Barra de Tempo ==================================================================

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if Bolinha.collidepoint(pygame.mouse.get_pos()):
                if TC == CorVerde and not Arrastar and not Pausado:

                    Arrastar = True

            elif BarraTTotal.collidepoint(pygame.mouse.get_pos()):
                if TC == CorVerde and not Pausado:

                    Porcentagem = (mx - BarraTempoX) / BarraLargura
                    Ntempo = T1 * Porcentagem
                    TempoInicial = Ntempo
                    #Bolinha.x = mx-20
                    pygame.mixer.music.play(start=Ntempo)

                elif TC == CorVerde and Pausado:

                    Porcentagem = (mx - BarraTempoX) / BarraLargura
                    Ntempo = T1 * Porcentagem
                    TempoInicial = Ntempo
                    pygame.mixer.music.play(start=Ntempo)
                    if Pausado:
                        pygame.mixer.music.pause()

                    #Bolinha.x = mx - 20

        if Arrastar:
            if BarraTempoX <= mx <= BarraTempoX + BarraLargura:
                Porcentagem = (mx - BarraTempoX) / BarraLargura
                Ntempo = T1 * Porcentagem
                Bolinha.x = mx - 20

        if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            if Arrastar and TC == CorVerde:

                TempoInicial = Ntempo
                pygame.mixer.music.play(start=Ntempo)
                Arrastar = False

                if Pausado:
                    pygame.mixer.music.pause()



    # Botao Pause/Despause com o Click ================================

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if PlayStop.collidepoint(evento.pos):

                if TC == CorVerde:
                    if not Pausado:
                        Pausado = True
                        pygame.mixer.music.pause()
                    elif Pausado:
                        Pausado = False
                        pygame.mixer.music.unpause()
                elif TC == CorVermelho:
                    pygame.mixer.music.play()
                    TC = CorVerde


    # Botao Play/Stop com o click ========================================

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if BotaoEncerrar.collidepoint(evento.pos):

                if TC == CorVermelho:
                    pygame.mixer.music.play()
                    TC = CorVerde
                else:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unpause()
                    Pausado = False
                    TC = CorVermelho
                    TempoInicial = 0

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

# =================================================================================
# Teclado + Musica |---------------------------------------------------------------
# =================================================================================

         # Rodinha do Mouse para mover a lista para cima e para baixo =============

        if evento.type == pygame.MOUSEWHEEL:
            Scroll -= evento.y * VelScroll

            LimiteScroll = max(0, AltConteudo - posY + 270)
            Scroll = max(0, min(Scroll, LimiteScroll))

        # Atulizar a Lista de Musica ==============================================

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
            musicas = [
        os.path.join(Pmusicas, musica)
        for musica in os.listdir(Pmusicas)
        if musica.endswith(".mp3")
        ]

        # Escolher Musica Aleatorio ================================================

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_q:
            if TC == CorVerde:

                LM = random.randint(0, len(musicas) -1)

                pygame.mixer.music.load(musicas[LM])
                pygame.mixer.music.play()

                T1 = MP3(musicas[LM]).info.length
                TempoInicial = 0
                Pausado = False

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
            pygame.mixer.music.unpause()
            Arrastar = False
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
    Scroll = max(0, min(Scroll, AltConteudo - posY+270))
    for i, musica in enumerate(musicas):
        T2nome = os.path.splitext(os.path.basename(musica))[0]
        T2nome = re.sub(r'^[0-9.\- ]+', '', T2nome)
        Objeto2 = pygame.Rect(110, Tpy, posX-125, 45)
        ObjetoCor = CorPreto
        if i == LM:
            MusicCor = CorAmarelo
            ObjetoCor = CorVerdeDark
        else:
            MusicCor = CorLaranja
            ObjetoCor = CorPreto
        ObjetoD2 = pygame.draw.rect(telaP, ObjetoCor, Objeto2)
        TextoT2 = Fonte3.render(f"{i+1:03}. " + T2nome, True, MusicCor)
        PosMusic = (120, Tpy+5)
        if 55 < Tpy < posY-100:
            telaP.blit(TextoT2, PosMusic)
            RectMusic.append((Objeto2, i))
        Tpy += 50

    # Sistema de Tempo da Musica
    if TC == CorVerde:
        pos = (pygame.mixer.music.get_pos() / 1000) + TempoInicial

    elif TC == CorVermelho:
        pos = 0

    # Tempo Atual da Musica
    minutos = int(pos // 60)
    segundos = int(pos % 60)
    mx, my = pygame.mouse.get_pos()

    TM_limite = (mx - BarraTempoX) / BarraLargura
    TM_limite = max(0, min(TM_limite, 1))

    TMusic = int(T1 * TM_limite)

    TextoT1 = Fonte.render(f"{minutos:02}:{segundos:02}", True, CorBranco)

    if Arrastar:
        TextoT1 = Fonte.render(f"{TMusic // 60:02}:{TMusic % 60:02}", True, CorCiano)
    elif BarraTempoX <= mx <= BarraTempoX + BarraLargura:
        if BarraTempoY - 15 <= my <= BarraTempoY + BarraAltura:
            if TC == CorVerde and not Arrastar:
                if not Bolinha.collidepoint(mx, my):
                    TextoT1 = Fonte.render(f"{TMusic// 60:02}:{TMusic % 60:02}", True, BolinhaCor)
                else:
                    TextoT1 = Fonte.render(f"{minutos:02}:{segundos:02}", True, CorBranco)


    # Tempo Total da Musica
    T1minutos = int(T1 // 60)
    T1segundos = int(T1 % 60)
    TextoT2 = Fonte.render(f"{T1minutos:02}:{T1segundos:02}", True, CorBranco)

# Atulização ------------------------------------------------------------------------------------

    pygame.draw.line(telaP, CorPreto, (10, 42), (posX-10, 42), 65) # Linha Preta Cima
    pygame.draw.line(telaP, CorPreto, (10, posY-43), (posX-10, posY-43), 65) # Linha Preta Baixo
    pygame.draw.line(telaP, CorAzul, (100, 85), (100, posY-80), 10)  # Linha Azul Meio
    #pygame.draw.line(telaP, CorAzul, (10, 415), (310, 415), 10) # Linha Azul Meio Esquerda
    pygame.draw.rect(telaP, CorAzul, (0, 0, posX, posY), 10) # Borda azul da Janela
    pygame.draw.rect(telaP, CorAzul, (0, 75, posX, posY-150), 10) # Borda Mais Dentro da Janela
    #pygame.draw.rect(telaP, CorCinza, (10, 85, 86, posY-170)) # Linha Cinza das Funções

    #pygame.draw.rect(telaP, CorVerdeDark, PlayStop)
    #pygame.draw.rect(telaP, CorAzul, Bolinha)
    #pygame.draw.rect(telaP, CorCiano, BAleatorio) # Botão Aleatorio
    #pygame.draw.rect(telaP, CorVermelho, (PF[0], 265+45, PF[2], PF[3]))
    #pygame.draw.rect(telaP, CorBranco, (PF[0], 355+70, PF[2], PF[3]))

    # Botao de Looop
    #pygame.draw.circle(telaP, CorAmarelo, (54, 245), 30)
    #pygame.draw.circle(telaP, CorCinza, (54, 245), 20)
    #pygame.draw.line(telaP, CorCinza, (50, 250), (80, 275), 10)
    #pygame.draw.polygon(telaP, CorAmarelo, [(70, 272), (50, 255), (45, 285)])

    # Barra de Tempo da Musica
    pygame.draw.line(telaP, CorCinza, (BarraTempoX, BarraTempoY), (BarraTempoX + BarraLargura, BarraTempoY), BarraAltura)

    # Sistema da Bolinha do Tempo
    if T1 > 0:
        Progresso = pos / T1
    else:
        Progresso = 0

    Progresso = max(0, min(Progresso, 1))
    BolinhaXT = BarraTempoX + (BarraLargura * Progresso)
    BolinhaX = max(BarraTempoX,min(BolinhaXT, BarraTempoX + BarraLargura))

    if not Arrastar:
        Bolinha.centerx = int(BolinhaX)
        pygame.draw.line(telaP, CorBranco, (BarraTempoX, BarraTempoY), (BolinhaX, BarraTempoY), BarraAltura)

    BolinhaCor = CorVerde
    if BolinhaX > mx:
        BolinhaCor = CorVermelho
    elif BolinhaX < mx:
        BolinhaCor = CorVerde

    # Bolinha e Barra Vermelha e Verde
    mx, my = pygame.mouse.get_pos()
    if TC == CorVerde and not Bolinha.collidepoint(mx, my) and not Arrastar:
        if BarraTempoX <= mx <= BarraTempoX + BarraLargura:
            if BarraTempoY-15 <= my <= BarraTempoY + BarraAltura:

                pygame.draw.line(telaP, BolinhaCor, (BolinhaX, BarraTempoY),
                                 (mx, BarraTempoY), BarraAltura)
                BolinhaRect = pygame.draw.circle(telaP, BolinhaCor, (mx, posY-45), 15)

    # Previa da musica
    PAM = BarraTempoX + (BarraLargura * (pos / T1))

    if Arrastar:
        if BolinhaX < mx:
            BolinhaCor = CorVermelho
        elif BolinhaX > mx:
            BolinhaCor = CorVerde

    if Arrastar:
        pygame.draw.rect(telaP, BolinhaCor, (int(PAM),posY-64, 10, 40), border_radius=15)

    # Aparencia da Bolinha
    if TC == CorVerde and not Pausado and Bolinha.collidepoint(mx, my) or Arrastar:
        pygame.draw.circle(telaP, CorCiano, (Bolinha.x + 20, posY - 45), 20)
        pygame.draw.circle(telaP, CorAzul, (Bolinha.x + 20, posY - 45), 15)

    #elif Pausado:
        #pygame.draw.circle(telaP, CorBranco, (Bolinha.x + 8, posY - 45), 20)

    elif not Arrastar:
        pygame.draw.circle(telaP, CorBranco, (BolinhaX, posY - 45), 20)

    # Botão de Encerrar
    pygame.draw.rect(telaP,TC,(20, posY-165, 86-20, 86-20), border_radius=10) # Encerrar a Musica

    # Botão de Pause/Despause

    mx1, my1 = pygame.mouse.get_pos()

    if PlayStop.collidepoint(mx1, my1) and TC == CorVerde:
        pygame.draw.rect(telaP, CorVerde, (10 + 6, 85 + 5, 86 - 12, 91 - 10), border_radius=10)
    elif PlayStop.collidepoint(mx1, my1) and TC == CorVermelho :
        pygame.draw.rect(telaP, CorVermelho, (10 + 6, 85 + 5, 86 - 12, 91 - 10), border_radius=10)
    else:
        pygame.draw.rect(telaP, CorCinza, PlayStop)

    if Pausado == True or TC == CorVermelho:
        pygame.draw.polygon(telaP, CorPreto,[(80 ,129),(27, 98),(27, 162)])
    elif Pausado == False:
        pygame.draw.line(telaP, CorPreto,(35, 100),(35, 160),20,)
        pygame.draw.line(telaP, CorPreto, (68, 100), (68, 160), 20)

    # Nome da música atual =======================================
    TextoMusic = Fonte.render(Tnome, True, CorBranco)
    TextoMusicCenter = TextoMusic.get_rect(center=(posX/2, 35))
    telaP.blit(TextoMusic, TextoMusicCenter)

    # Tempo =======================================================
    telaP.blit(TextoT1, (20, posY-75)) # Atual
    telaP.blit(TextoT2, (posX-130, posY-75)) # Total


    pygame.display.flip()
    Clock.tick(60)

pygame.quit()
sys.exit()
