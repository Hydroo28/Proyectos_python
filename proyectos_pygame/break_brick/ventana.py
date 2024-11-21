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
   
    ventana.fill(negro)    ####Esto lo voy a cambiar de sitio 
    
    # #Creamos los ladrillos de la primera fila.
    # ladrillos.crearBloquesMoradosFila1(ventana, morado)
    # ladrillos.crearBloquesRosasFila1(ventana, rosa_palo)
    # ladrillos.crearBloquesAmarillosFila1(ventana, verde)
    # ladrillos.crearBloquesAzulesfila1(ventana, azul_cielo)

    
    personajes.crearCuadrado(ventana, blanco)
    personajes.moverPersonaje()
    personajes.colisionPlataforma(tamaño)

    
    # Si la bola está quieta, mantenerla pegada a la plataforma
    if personajes.bolita.vel_x == 0 and personajes.bolita.vel_y == 0:
        personajes.bolita.x = personajes.plataforma.x + personajes.plataforma.w // 2
        personajes.bolita.y = personajes.plataforma.y - personajes.bolita.r
    else:
        # Si la bola está en movimiento, actualizar su posición
        personajes.moverBola(tamaño)

    personajes.crearBola(ventana, blanco)
    personajes.lanzarBola()
    
    
    # print(personajes.bolita.x, personajes.bolita.y)
    
    # print(personajes.bolita.x, personajes.bolita.y)

    



    

    

    
    print(personajes.bolita.x, personajes.bolita.y, personajes.plataforma.x, personajes.plataforma.y)
    
    pygame.display.update()
    pygame.time.Clock().tick(60)