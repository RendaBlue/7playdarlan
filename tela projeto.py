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
Fonte3 = pygame.font.SysFont("Arial", 35, True)

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
T1 = MP3(musicas[LM]).info.length
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
Scroll = 0
VelScroll = 30
posX, posY = telaP.get_size()
BarraTempoX = 200
BarraTempoY = 660
BarraLargura = posX - 410
BarraAltura = 15
TempoInicial = 0

# Outros -----------------------------------------------------------------------------------
TC = CorVermelho
Pausado = False
Infor = pygame.display.get_desktop_sizes()
Objeto = pygame.Rect(10, 110, 300, 300)

# Sistema --------------------------------------------------------------------------------
Run = True
while Run:
    telaP.fill(CorBranco)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            Run = False

        # Barra Tempo
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            mx, my = pygame.mouse.get_pos()

            if BarraTempoX <= mx <= BarraTempoX + BarraLargura:
                if BarraTempoY <= my <= BarraTempoY + BarraAltura:

                    Porcentagem = (mx - BarraTempoX) / BarraLargura
                    Ntempo = T1 * Porcentagem

                    if TC == CorVerde:
                        TempoInicial = Ntempo
                        pygame.mixer.music.play(start=Ntempo)

                        if Pausado:
                            pygame.mixer.music.pause()

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
            musicas = [
        os.path.join(Pmusicas, musica)
        for musica in os.listdir(Pmusicas)
        if musica.endswith(".mp3")
        ]
        if evento.type == pygame.MOUSEWHEEL:
            Scroll -= evento.y * VelScroll

            LimiteScroll = max(0, AltConteudo - 450)
            Scroll = max(0, min(Scroll, LimiteScroll))

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
                    TempoInicial = 0

            # Clique na lista de músicas
            mx, my = evento.pos

            for rect, indice in RectMusic:

                if rect.collidepoint(evento.pos):
                    if 120 <= my <= 600:
                        LM = indice
                        pygame.mixer.music.load(musicas[LM])
                        Pausado = False

                    if TC == CorVerde and Pausado == False:
                        pygame.mixer.music.play()
                        TempoInicial = 0

                    break

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
            T1 = MP3(musicas[LM]).info.length
            TempoInicial = 0
            Pausado = False
            pygame.mixer.music.unpause()
            if TC == CorVerde and Pausado == False:
                pygame.mixer.music.play()

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            LM = (LM - 1) % len(musicas)
            pygame.mixer.music.load(musicas[LM])
            T1 = MP3(musicas[LM]).info.length
            TempoInicial = 0
            Pausado = False
            pygame.mixer.music.unpause()
            if TC == CorVerde and Pausado == False:
                pygame.mixer.music.play()

        if evento.type == ResetMusic and not TC == CorVermelho:
            LM = (LM + 1) % len(musicas)
            pygame.mixer.music.load(musicas[LM])
            T1 = MP3(musicas[LM]).info.length
            TempoInicial = 0
            Pausado = False
            pygame.mixer.music.unpause()
            if TC == CorVerde:
                pygame.mixer.music.play()

    # Volume da musica

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
            Volume = min(Volume + 0.1, 1.0)
            pygame.mixer.music.set_volume(Volume)

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
            Volume = max(Volume - 0.1, 0.1)
            pygame.mixer.music.set_volume(Volume)

# Mensagem ------------------------------------------------------------------------------------

    #_Texto1 = Musicas
    Tnome = os.path.splitext(os.path.basename(musicas[LM]))[0]
    RectMusic.clear()
    Tpy = 110 - Scroll
    AltConteudo = len(musicas) * 52
    Scroll = max(0, min(Scroll, AltConteudo - 450))

    for i, musica in enumerate(musicas):
        T2nome = os.path.splitext(os.path.basename(musica))[0]
        pygame.draw.rect(telaP, CorPreto, (320, Tpy, 950, 45)) #(320, 110, 950, Tpy))
        if i == LM:
            MusicCor = CorVermelho
        else:
            MusicCor = CorCiano
        TextoT2 = Fonte3.render(T2nome, True, MusicCor)
        PosMusic = (330, Tpy)
        if -50 < Tpy < 720:
            telaP.blit(TextoT2, PosMusic)
            RectTexto = TextoT2.get_rect(topleft=PosMusic)
            RectMusic.append((RectTexto, i))
        Tpy += 55

        # Limite de Scroll



    # _Texto2 = Pausado (ON/OFF)
    NomePause = "Pausado"
    Texto3 = Fonte2.render(NomePause, True, CorVermelho)
    if TC == CorVerde:
        if not Pausado:
            pos = (pygame.mixer.music.get_pos() / 1000) + TempoInicial

    elif TC == CorVermelho:
        pos = 0

    minutos = int(pos // 60)
    segundos = int(pos % 60)
    T1minutos = int(T1 // 60)
    T1segundos = int(T1 % 60)
    TextoT1 = Fonte.render(f"{minutos:02}:{segundos:02}", True, CorBranco)
    TextoT2 = Fonte.render(f"{T1minutos:02}:{T1segundos:02}", True, CorBranco)
    #telaP.blit(TextoT1, (20, 410)



    #telaP.blit(TextoT2, (20, 460))

# Atulização ------------------------------------------------------------------------------------

    pygame.draw.line(telaP, CorPreto, (10, 50), (posX, 50), 100) # Linha Preta Cima
    pygame.draw.line(telaP, CorPreto, (10, 660), (posX, 660), 100) # Linha Preta Baixo
    pygame.draw.line(telaP, CorAzul, (314, 110), (314, 610), 10)  # Linha Azul Meio
    pygame.draw.line(telaP, CorAzul, (10, 415), (310,  415), 10) # Linha Azul Meio Esquerda
    pygame.draw.rect(telaP, CorAzul, (0, 0, posX, posY), 10)
    pygame.draw.rect(telaP, CorAzul, (0, 100, posX, posY-200), 10)
    pygame.draw.rect(telaP, CorCiano, (10, 420, 300, 190))


    # Barra de Tempo da Musica

    pygame.draw.line(telaP, CorCiano, (BarraTempoX, BarraTempoY), (BarraTempoX + BarraLargura, BarraTempoY), BarraAltura)

    if T1 > 0:
        Progresso = pos / T1
    else:
        Progresso = 0

    Progresso = max(0, min(Progresso, 1))

    BolinhaX = BarraTempoX + (BarraLargura * Progresso)
    BolinhaX = max(BarraTempoX,min(BolinhaX, BarraTempoX + BarraLargura))
    pygame.draw.circle(telaP, CorBranco, (int(BolinhaX), 660), 20)

    pygame.draw.line(telaP, CorBranco, (BarraTempoX, BarraTempoY), (BolinhaX, BarraTempoY), BarraAltura)

    pygame.draw.rect(telaP, TC, Objeto)

    pygame.draw.rect(telaP, TC, Objeto, 25)

    # Nome da música atual
    Texto = Fonte.render(Tnome, True, CorBranco)
    telaP.blit(Texto, (30, 10))

    # Tempo
    telaP.blit(TextoT1, (20, 625))
    telaP.blit(TextoT2, (posX-170, 625))

    # Pausado
    if Pausado and TC == CorVerde:
        telaP.blit(Texto3, (15, 535))

    pygame.display.flip()
    Clock.tick(60)

pygame.quit()
sys.exit()
