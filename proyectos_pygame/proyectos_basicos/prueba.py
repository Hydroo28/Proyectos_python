import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FPS (cuadros por segundo)
FPS = 60
clock = pygame.time.Clock()

# Parámetros de la paleta
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7

# Parámetros de la pelota
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Crear las paletas
player1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 70, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Crear la pelota
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Puntuación
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

# Función para reiniciar la pelota
def reset_ball():
    ball.x = WIDTH // 2 - BALL_SIZE // 2
    ball.y = HEIGHT // 2 - BALL_SIZE // 2
    global BALL_SPEED_X, BALL_SPEED_Y
    BALL_SPEED_X *= random.choice((1, -1))
    BALL_SPEED_Y *= random.choice((1, -1))

# Función para dibujar los elementos en la pantalla
def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    score_text = font.render(f"{score1}   {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - 30, 20))
    
    pygame.display.flip()

# Lógica del juego
def game_loop():
    global BALL_SPEED_X, BALL_SPEED_Y, score1, score2

    running = True
    while running:
        # Control de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Teclas para controlar las paletas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.top > 0:
            player1.y -= PADDLE_SPEED
        if keys[pygame.K_s] and player1.bottom < HEIGHT:
            player1.y += PADDLE_SPEED
        if keys[pygame.K_UP] and player2.top > 0:
            player2.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
            player2.y += PADDLE_SPEED

        # Movimiento de la pelota
        ball.x += BALL_SPEED_X
        ball.y += BALL_SPEED_Y

        # Colisiones con las paredes superiores e inferiores
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            BALL_SPEED_Y *= -1

        # Colisiones con las paletas
        if ball.colliderect(player1) or ball.colliderect(player2):
            BALL_SPEED_X *= -1

        # Verificar si un jugador anota
        if ball.left <= 0:
            score2 += 1
            reset_ball()
        if ball.right >= WIDTH:
            score1 += 1
            reset_ball()

        # Dibujar todo
        draw()

        # Control de la velocidad del juego
        clock.tick(FPS)

    pygame.quit()

# Iniciar el juego
reset_ball()
game_loop()