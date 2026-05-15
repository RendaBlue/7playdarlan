import pygame

# Inicialização
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

# Carregar e tocar música
# Substitua 'sua_musica.mp3' pelo caminho do seu arquivo
pygame.mixer.music.load('../musicas/129. Graveyard Ops Combat C High loop.mp3')
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- LÓGICA DO TEMPO ---
    # get_pos() retorna o tempo em milissegundos
    tempo_ms = pygame.mixer.music.get_pos()

    # Converte para segundos
    tempo_segundos = tempo_ms // 1000

    # Formata como minutos:segundos
    minutos = tempo_segundos // 60
    segundos = tempo_segundos % 60
    tempo_formatado = f"{minutos:02d}:{segundos:02d}"

    # --- DESENHO NA TELA ---
    screen.fill((0, 0, 0))  # Fundo preto
    texto = font.render(f"Tempo: {tempo_formatado}", True, (255, 255, 255))
    screen.blit(texto, (100, 80))

    pygame.display.flip()
    clock.tick(30)  # 30 FPS

pygame.quit()
