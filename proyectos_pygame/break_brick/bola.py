import pygame

class Pelota():
    def __init__(self, x, y, radio):
        self.x = x
        self.y = y
        self.radio = radio

bolita = Pelota(110, 775, 10)


def crearBola(ventana, color):
    global bolita
    bolita = pygame.draw.circle(ventana, color, (bolita.x, bolita.y), bolita.radio)
