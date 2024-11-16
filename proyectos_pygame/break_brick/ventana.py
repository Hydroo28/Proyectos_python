from colores import *
import personajes
import ladrillos
import pygame  
import sys




#Iniciamos el pygame
pygame.init()







tamaño = (800, 800)

# def actualizarColor():
#     global color_update, colores_ladrillos
#     color_update = random.choice(colores_ladrillos)



#Creamos una ventana.
ventana = pygame.display.set_mode(tamaño)





#ponemos el titulo a la ventana.
pygame.display.set_caption('Prueba')



while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #Pintamos la ventana de negro
   
    ventana.fill(negro)
    
    #Creamos los ladrillos de la primera fila.
    ladrillos.crearBloquesMoradosFila1(ventana, morado)
    ladrillos.crearBloquesRosasFila1(ventana, rosa_palo)
    ladrillos.crearBloquesAmarillosFila1(ventana, verde)
    ladrillos.crearBloquesAzulesfila1(ventana, azul_cielo)



    personajes.crearBola(ventana, blanco)

    personajes.crearCuadrado(ventana, blanco)

    personajes.moverPersonaje()

    personajes.colisionVentana(tamaño)

    pygame.display.update()
    pygame.time.Clock().tick(60)