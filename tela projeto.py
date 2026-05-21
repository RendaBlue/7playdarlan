import pygame
from mutagen.mp3 import MP3
import sys
import os

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
# ==================================================================
# Fontes |----------------------------------------------------------
# ==================================================================
Fonte = pygame.font.SysFont("Comic Sans", 50, True)
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
Info = pygame.display.Info()
TamanhoTela = (Info.current_w, Info.current_h)
telaP = pygame.display.set_mode((1280, 720))
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
BarraTempoX = 200
BarraTempoY = 660
BarraLargura = posX - 410
BarraAltura = 20
TempoInicial = 0

# ==========================================================================================
# Outros |----------------------------------------------------------------------------------
# ==========================================================================================
TC = CorVermelho
Pausado = False
Infor = pygame.display.get_desktop_sizes()
Objeto = pygame.Rect(10, 110, 300, 300)

# ========================================================================================
# Sistema |-------------------------------------------------------------------------------
# ========================================================================================

Run = True
while Run:
    telaP.fill(CorAzulEstranho)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            Run = False

# ==========================================================================================================
# -----| Mouse + Musica |-----------------------------------------------------------------------------------
# ==========================================================================================================

    # Barra de Tempo ==================================================================

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            mx, my = pygame.mouse.get_pos()

            if BarraTempoX <= mx <= BarraTempoX + BarraLargura:
                if BarraTempoY <= my <= BarraTempoY + BarraAltura:

                    Porcentagem = (mx - BarraTempoX) / BarraLargura
                    Ntempo = T1 * Porcentagem
                    print(Ntempo)

                    if TC == CorVerde:
                        TempoInicial = Ntempo
                        pygame.mixer.music.play(start=Ntempo)

                        if Pausado:
                            pygame.mixer.music.pause()

    # Botão de Play e Stop ================================================

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

            if Objeto.collidepoint(evento.pos):
                if TC == CorVermelho:
                    TC = CorVerde
                    pygame.mixer.music.play()
                    Pausado = False
                else:
                    TC = CorVermelho
                    pygame.mixer.music.stop()
                    TempoInicial = 0

        # Click na Musica para Selecionar =====================================

            mx, my = evento.pos

            for rect, indice in RectMusic:

                if rect.collidepoint(evento.pos):
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

            LimiteScroll = max(0, AltConteudo - 450)
            Scroll = max(0, min(Scroll, LimiteScroll))

    # Atulizar a Lista de Musica ==============================================

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
            musicas = [
        os.path.join(Pmusicas, musica)
        for musica in os.listdir(Pmusicas)
        if musica.endswith(".mp3")
        ]

# =================================================================================
# Teclado + Musica |---------------------------------------------------------------
# =================================================================================

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

    Tnome = os.path.splitext(os.path.basename(musicas[LM]))[0]
    RectMusic.clear()
    Tpy = 115 - Scroll
    AltConteudo = len(musicas) * 47
    Scroll = max(0, min(Scroll, AltConteudo - 450))
    for i, musica in enumerate(musicas):
        T2nome = os.path.splitext(os.path.basename(musica))[0]
        Objeto2 = pygame.draw.rect(telaP, CorPreto, (320, Tpy, 950, 45))
        if i == LM:
            MusicCor = CorAmarelo
        else:
            MusicCor = CorLaranja
        TextoT2 = Fonte3.render(T2nome, True, MusicCor)
        PosMusic = (330, Tpy+5)
        if 90 < Tpy < 610:
            telaP.blit(TextoT2, PosMusic)
            RectTexto = TextoT2.get_rect(topleft=PosMusic)
            RectMusic.append((RectTexto, i))
        Tpy += 50


    # Sistema de Tempo da Musica
    NomePause = "Pausado"
    Texto3 = Fonte2.render(NomePause, True, CorVermelho)
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

    pygame.draw.line(telaP, CorPreto, (10, 50), (posX, 50), 100) # Linha Preta Cima
    pygame.draw.line(telaP, CorPreto, (10, 660), (posX, 660), 100) # Linha Preta Baixo
    pygame.draw.line(telaP, CorAzul, (314, 110), (314, 610), 10)  # Linha Azul Meio
    pygame.draw.line(telaP, CorAzul, (10, 415), (310,  415), 10) # Linha Azul Meio Esquerda
    pygame.draw.rect(telaP, CorAzul, (0, 0, posX, posY), 10) # Borda azul da Janela
    pygame.draw.rect(telaP, CorAzul, (0, 100, posX, posY-200), 10) # Borda Mais Dentro da Janela
    pygame.draw.rect(telaP, CorCiano, (10, 420, 300, 190)) # Retangulo sem Função Ainda


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
    pygame.draw.circle(telaP, CorLaranja, (int(BolinhaX), 660), 20)

    pygame.draw.rect(telaP, TC, Objeto) # Botão de Play e Stop

    # Nome da música atual =======================================
    Texto = Fonte.render(Tnome, True, CorBranco)
    telaP.blit(Texto, (30, 10))

    # Tempo =======================================================
    telaP.blit(TextoT1, (20, 625))
    telaP.blit(TextoT2, (posX-170, 625))

    # Pausado ==================================================
    if Pausado and TC == CorVerde:
        telaP.blit(Texto3, (15, 535))

    pygame.display.flip()
    Clock.tick(60)

pygame.quit()
sys.exit()
