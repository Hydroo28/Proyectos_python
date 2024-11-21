import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Break Brick")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Plataforma
plataforma = pygame.Rect(350, 550, 100, 10)
velocidad_plataforma = 5

# Bolita
radio_bola = 10
pos_bola = [400, 540]  # Inicialmente sobre la plataforma
velocidad_bola = [0, 0]
bola_en_movimiento = False

# Reloj para FPS
reloj = pygame.time.Clock()

# Bucle del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Detectar lanzamiento
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_UP, pygame.K_w) and not bola_en_movimiento:
                bola_en_movimiento = True
                velocidad_bola = [4, -4]  # Velocidad inicial de la bola

    # Movimiento de la plataforma
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and plataforma.left > 0:
        plataforma.move_ip(-velocidad_plataforma, 0)
    if teclas[pygame.K_RIGHT] and plataforma.right < ANCHO:
        plataforma.move_ip(velocidad_plataforma, 0)

    # Movimiento de la bolita
    if bola_en_movimiento:
        pos_bola[0] += velocidad_bola[0]
        pos_bola[1] += velocidad_bola[1]

        # Colisiones con los bordes de la ventana
        if pos_bola[0] - radio_bola <= 0 or pos_bola[0] + radio_bola >= ANCHO:
            velocidad_bola[0] *= -1
        if pos_bola[1] - radio_bola <= 0:
            velocidad_bola[1] *= -1
    else:
        # Mantener la bola sobre la plataforma si no está en movimiento
        pos_bola[0] = plataforma.centerx

    # Dibujar todo
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, BLANCO, plataforma)
    pygame.draw.circle(pantalla, BLANCO, pos_bola, radio_bola)

    pygame.display.flip()
    reloj.tick(60)
