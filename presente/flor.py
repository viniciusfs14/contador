import pygame
import math

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flor Mágica 🌸")

# Cores
BACKGROUND = (255, 230, 250)  # Rosa claro
PETAL_COLOR = (255, 100, 150)  # Rosa forte
CENTER_COLOR = (255, 220, 100)  # Amarelo

# Variável de controle do tamanho das pétalas
petal_size = 20  # Pequena inicialmente
max_petal_size = 60  # Tamanho máximo ao desabrochar

def draw_flower(center_x, center_y, petal_size):
    """Desenha uma flor com pétalas circulares."""
    screen.fill(BACKGROUND)  # Limpa a tela
    
    # Desenha as pétalas
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        petal_x = center_x + math.cos(rad) * petal_size
        petal_y = center_y + math.sin(rad) * petal_size
        pygame.draw.circle(screen, PETAL_COLOR, (int(petal_x), int(petal_y)), petal_size)
    
    # Centro da flor
    pygame.draw.circle(screen, CENTER_COLOR, (center_x, center_y), petal_size // 2)
    
    pygame.display.flip()

# Posição inicial da flor
flower_x, flower_y = WIDTH // 2, HEIGHT // 2
running = True

touching = False  # Controle de toque

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type in (pygame.MOUSEBUTTONDOWN, pygame.FINGERDOWN):  # Detecta toque ou clique
            touching = True  # Começa a abrir a flor
        
        if event.type in (pygame.MOUSEBUTTONUP, pygame.FINGERUP):  # Solta o clique ou toque
            touching = False  # Para de crescer

    # Se estiver tocando, aumenta o tamanho da flor
    if touching and petal_size < max_petal_size:
        petal_size += 1  # Cresce suavemente
    elif not touching and petal_size > 20:
        petal_size -= 1  # Volta ao tamanho original

    draw_flower(flower_x, flower_y, petal_size)
    pygame.time.delay(30)

pygame.quit()
