
import pygame
import random


class Ladrillos():
    def __init__(self, x, y, w, h):


        self.x = x
        self.y = y
        self.w = w
        self.h = h

    
        


bloque1 = Ladrillos(0, 0, 20, 20)
bloque2 = Ladrillos(20, 0, 20, 20)
bloque3 = Ladrillos(40, 0, 20, 20)
bloque4 = Ladrillos(60, 0, 20, 20)
bloque5 = Ladrillos(80, 0, 20, 20)
bloque6 = Ladrillos(100, 0, 20, 20)
bloque7 = Ladrillos(120, 0, 20, 20)
bloque8 = Ladrillos(140, 0, 20, 20)
bloque9 = Ladrillos(160, 0, 20, 20)
bloque10 = Ladrillos(180, 0, 20, 20)
bloque11 = Ladrillos(200, 0, 20, 20)
bloque12 = Ladrillos(220, 0, 20, 20)
bloque13 = Ladrillos(240, 0, 20, 20)
bloque14 = Ladrillos(260, 0, 20, 20)
bloque15 = Ladrillos(280, 0, 20, 20)
bloque16 = Ladrillos(300, 0, 20, 20)
bloque17 = Ladrillos(320, 0, 20, 20)
bloque18 = Ladrillos(340, 0, 20, 20)
bloque19 = Ladrillos(360, 0, 20, 20)
bloque20 = Ladrillos(380, 0, 20, 20)
bloque21 = Ladrillos(400, 0, 20, 20)
bloque22 = Ladrillos(420, 0, 20, 20)
bloque23 = Ladrillos(440, 0, 20, 20)
bloque24 = Ladrillos(460, 0, 20, 20)
bloque25 = Ladrillos(480, 0, 20, 20)
bloque26 = Ladrillos(500, 0, 20, 20)
bloque27 = Ladrillos(520, 0, 20, 20)
bloque28 = Ladrillos(540, 0, 20, 20)

def crearBloquesMoradosFila1(ventana, color):
    global bloque1, bloque2, bloque3, bloque4, bloque5, bloque6, bloque7
    bloque1 = pygame.draw.rect(ventana, color, (bloque1.x, bloque1.y, bloque1.w, bloque1.h), 2)
    bloque2 = pygame.draw.rect(ventana, color, (bloque2.x, bloque2.y, bloque2.w, bloque2.h), 2)
    bloque3 = pygame.draw.rect(ventana, color, (bloque3.x, bloque3.y, bloque3.w, bloque3.h), 2)
    bloque4 = pygame.draw.rect(ventana, color, (bloque4.x, bloque4.y, bloque4.w, bloque4.h), 2)
    bloque5 = pygame.draw.rect(ventana, color, (bloque5.x, bloque5.y, bloque5.w, bloque5.h), 2)
    bloque6 = pygame.draw.rect(ventana, color, (bloque6.x, bloque6.y, bloque6.w, bloque6.h), 2)
    bloque7 = pygame.draw.rect(ventana, color, (bloque7.x, bloque7.y, bloque7.w, bloque7.h), 2)
  
    

def crearBloquesRosasFila1(ventana, color):
    global bloque8, bloque9, bloque10, bloque11, bloque12, bloque13, bloque14
    bloque8 = pygame.draw.rect(ventana, color, (bloque8.x , bloque8.y, bloque8.w, bloque8.h), 2)
    bloque9 = pygame.draw.rect(ventana, color, (bloque9.x, bloque9.y, bloque9.w, bloque9.h), 2)
    bloque10 = pygame.draw.rect(ventana, color, (bloque10.x, bloque10.y, bloque10.w, bloque10.h), 2)
    bloque11 = pygame.draw.rect(ventana, color, (bloque11.x, bloque11.y, bloque11.w, bloque11.h), 2)
    bloque12 = pygame.draw.rect(ventana, color, (bloque12.x, bloque12.y, bloque12.w, bloque12.h), 2)
    bloque13 = pygame.draw.rect(ventana, color, (bloque13.x, bloque13.y, bloque13.w, bloque13.h), 2)
    bloque14 = pygame.draw.rect(ventana, color, (bloque14.x, bloque14.y, bloque14.w, bloque14.h), 2)

def crearBloquesAmarillosFila1(ventana, color):
    global bloque15, bloque16, bloque17, bloque18, bloque19, bloque20, bloque21
    bloque15 = pygame.draw.rect(ventana, color, (bloque15.x, bloque15.y, bloque15.w, bloque15.h), 2)
    bloque16 = pygame.draw.rect(ventana, color, (bloque16.x, bloque16.y, bloque16.w, bloque16.h), 2)
    bloque17 = pygame.draw.rect(ventana, color, (bloque17.x, bloque17.y, bloque17.w, bloque17.h), 2)
    bloque18 = pygame.draw.rect(ventana, color, (bloque18.x, bloque18.y, bloque18.w, bloque18.h), 2)
    bloque19 = pygame.draw.rect(ventana, color, (bloque19.x, bloque19.y, bloque19.w, bloque19.h), 2)
    bloque20 = pygame.draw.rect(ventana, color, (bloque20.x, bloque20.y, bloque20.w, bloque20.h), 2)
    bloque21 = pygame.draw.rect(ventana, color, (bloque21.x, bloque21.y, bloque21.w, bloque21.h), 2)

def crearBloquesAzulesfila1(ventana, color):
    global bloque22, bloque23, bloque24, bloque25, bloque26, bloque27, bloque28
    bloque22 = pygame.draw.rect(ventana, color, (bloque22.x, bloque22.y, bloque22.w, bloque22.h), 2)
    bloque23 = pygame.draw.rect(ventana, color, (bloque23.x, bloque23.y, bloque23.w, bloque23.h), 2)
    bloque24 = pygame.draw.rect(ventana, color, (bloque24.x, bloque24.y, bloque24.w, bloque24.h), 2)
    bloque25 = pygame.draw.rect(ventana, color, (bloque25.x, bloque25.y, bloque25.w, bloque25.h), 2)
    bloque26 = pygame.draw.rect(ventana, color, (bloque26.x, bloque26.y, bloque26.w, bloque26.h), 2)
    bloque27 = pygame.draw.rect(ventana, color, (bloque27.x, bloque27.y, bloque27.w, bloque27.h), 2)
    bloque28 = pygame.draw.rect(ventana, color, (bloque28.x, bloque28.y, bloque28.w, bloque28.h), 2)   


