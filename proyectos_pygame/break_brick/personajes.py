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
      self.vel_x = 0
      self.vel_y = 0
   




   





#########################   BOLITA
bolita = Pelota(400, 775, 10)



def crearBola(ventana, color):
   global bolita
   
   pygame.draw.circle(ventana, color, ((bolita.x), (bolita.y)), bolita.r,)

def lanzarBola():
   global bolita
   teclas = pygame.key.get_pressed()
   if teclas[pygame.K_UP] or teclas[pygame.K_w]:
      if bolita.vel_x == 0 and bolita.vel_y == 0:
         bolita.vel_x = 5
         bolita.vel_y = -5

def moverBola(tamaño):
   global bolita
   #aqui le digo que le sume a la x su velocidad y a la y tambien
   
   bolita.x += bolita.vel_x
   bolita.y += bolita.vel_y
   


  #Rebote en los bordes
   if bolita.x - bolita.r <= 0 or bolita.x + bolita.r >= tamaño[0]:  # Colisiones con los lados
      bolita.vel_x *= -1
   if bolita.y - bolita.r <= 0:  # Colisión con el techo
      bolita.vel_y *= -1
   if bolita.y + bolita.r >= tamaño[1]:  # Colisión con el suelo (reinicio)
      bolita.vel_x = 0
      bolita.vel_y = 0
      bolita.x = plataforma.x + plataforma.w // 2
      bolita.y = plataforma.y - bolita.r
   

   #Reiniciar si toca la parte inferior 
   if bolita.y + bolita.r >= tamaño[0]:
      bolita.vel_x = 0
      bolita.vel_y = 0
      bolita.x = plataforma.x + plataforma.w // 2
      bolita.y = plataforma.y - bolita.r





#########################   PLATAFORMA





plataforma = Personaje(350, 785, 100, 15)




def crearCuadrado(ventana, color):
   global plataforma
   pygame.draw.rect(ventana, color, (plataforma.x, plataforma.y, plataforma.w, plataforma.h))

def moverPersonaje():
   teclas = pygame.key.get_pressed()
   if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
      plataforma.x -= 10
   elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d] :
      plataforma.x += 10

def colisionPlataforma(tamaño):
   if plataforma.x <= 0:
      plataforma.x = 0
   elif plataforma.x >= tamaño[0] - plataforma.w:
      plataforma.x = tamaño[0] - plataforma.w

