import pygame



class Personaje():
   def __init__(self, x, y, w, h):
      self.x = x
      self.y = y
      self.w = w
      self.h = h



class Pelota():


   def __init__(self, x, y, r):
      self.x = x
      self.y = y
      self.r = r
   

bolita = Pelota(110, 775, 10)


   







def crearBola(ventana, color):
   global bolita
   bolita = Pelota(500, 500 ,10)
   bolita = pygame.draw.circle(ventana, color, ((bolita.x), (bolita.y)), 10)






# def moverBola():
#    pass
    

plataforma = Personaje(350, 785, 100, 15)




def crearCuadrado(ventana, color):
   global plataforma
   plataforma =  pygame.draw.rect(ventana, color, (plataforma.x, plataforma.y, plataforma.w, plataforma.h))

def moverPersonaje():
   teclas = pygame.key.get_pressed()
   if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
      plataforma.x -= 10
   elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d] :
      plataforma.x += 10

def colisionVentana(tamaño):
   if plataforma.x <= 0:
      plataforma.x = 0
   elif plataforma.x >= tamaño[0] - plataforma.w:
      plataforma.x = tamaño[0] - plataforma.w

