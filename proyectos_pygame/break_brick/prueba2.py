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




    personajes.moverPersonaje()
    personajes.colisionPlataforma(tamaño)
    personajes.lanzarBola()

    if personajes.bolita.x != 0 or personajes.bolita.y != 0:
        personajes.lanzarBola()
    else:
        personajes.bolita.x = personajes.plataforma.x + personajes.plataforma.w // 2
        personajes.bolita.y = personajes.plataforma.y - personajes.bolita.r
    
    ventana.fill(negro)
    personajes.crearCuadrado(ventana, blanco)
    personajes.crearBola(ventana, blanco)

    pygame.display.update()
    pygame.time.Clock().tick(60)

    # #Pintamos la ventana de negro
   
    # ventana.fill(negro)    ####Esto lo voy a cambiar de sitio 
    
    # # #Creamos los ladrillos de la primera fila.
    # # ladrillos.crearBloquesMoradosFila1(ventana, morado)
    # # ladrillos.crearBloquesRosasFila1(ventana, rosa_palo)
    # # ladrillos.crearBloquesAmarillosFila1(ventana, verde)
    # # ladrillos.crearBloquesAzulesfila1(ventana, azul_cielo)

    

    # personajes.crearBola(ventana, blanco)
    # personajes.lanzarBola()
    
    # if personajes.bolita.x != 0 or personajes.bolita.y != 0:
    #     personajes.lanzarBola()
    # else:
    #     personajes.bolita.x = personajes.plataforma.x + personajes.plataforma.w // 2
    #     personajes.bolita.y = personajes.plataforma.y - personajes.bolita.r

    
    # # print(personajes.bolita.x, personajes.bolita.y)
    
    # # print(personajes.bolita.x, personajes.bolita.y)

    



    # personajes.crearCuadrado(ventana, blanco)

    # personajes.moverPersonaje()

    # personajes.colisionPlataforma(tamaño)
    # print(personajes.bolita.x, personajes.bolita.y, personajes.plataforma.x, personajes.plataforma.y)
    
    # pygame.display.update()
    # pygame.time.Clock().tick(60)