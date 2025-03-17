import pygame
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello Kitty Mágica ✨")

# Cores
PINK = (255, 182, 193)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 220, 100)

# Carregar imagem da Hello Kitty
hello_kitty = pygame.image.load("hello_kitty.png")  # Substitua pela imagem correta
hello_kitty = pygame.transform.scale(hello_kitty, (200, 200))
kitty_x, kitty_y = WIDTH // 2 - 100, HEIGHT // 2 - 100

# Lista de corações
hearts = []

# Função para desenhar os corações fofinhos
def draw_hearts():
    for heart in hearts:
        pygame.draw.circle(screen, PINK, (heart[0], heart[1]), 8)

# Loop principal
running = True
while running:
    screen.fill(WHITE)
    screen.blit(hello_kitty, (kitty_x, kitty_y))
    draw_hearts()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type in (pygame.MOUSEBUTTONDOWN, pygame.FINGERDOWN):
            x, y = pygame.mouse.get_pos()
            if kitty_x < x < kitty_x + 200 and kitty_y < y < kitty_y + 200:
                for _ in range(5):
                    hearts.append([x + random.randint(-30, 30), y + random.randint(-30, 30)])
    
    pygame.display.flip()
    pygame.time.delay(50)
    
    if len(hearts) > 20:
        hearts.pop(0)

pygame.quit()
