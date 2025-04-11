import pygame
import sys
import math
rojo =(255,0,0)
azul =(0,0,255)
verde =(0,255,0)
rosado =(255,192,203)
negro =(0,0,0)
amarillo =(255,255,0)
blanco =(255,255,255)
naranja =(255,165,0)
cian = (0,255,255)
PI = math.pi
pygame.init()

ventana = pygame.display.set_mode((400,400))

pygame.display.set_caption(" dibuja formas en pygame")

clock = pygame.time.Clock()
 
XX = 300
MOVIMIENTO = 3

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()

    ventana.fill(negro)
    
    #dibujar formas en pygame 
    #dibujar una linea
    
    pygame.draw.line(ventana, rojo, (100,100),(300,300))
    pygame.draw.line(ventana, rojo, (100,300),(300,100))
    
    # dibujar una linea discontinua
    #True:crea un poligono
    puntos1 =[(0,0),(50,100),(100,50),(250,200),(400,400)]
    puntos2 =[(200,0),(400,200),(200,400),(0,200)]
    pygame.draw.lines(ventana,azul,True,puntos1)
    pygame.draw.lines(ventana,rojo,True,puntos2)

    #dibujar un rectangulo
    # rectangulo relleno
    pygame.draw.rect(ventana,rosado,(200,200,200,100))
    # rectangulo sin relleno
    pygame.draw.rect(ventana, verde,((100,100),(150,200)), 1)

    # dibujar un poigono
    puntos3 =[(200,200),(250,300),(300,325),(400,350)]
    pygame.draw.polygon(ventana,amarillo,puntos3,1)
    
    # dibujar un circulo
    pygame.draw.circle(ventana,blanco,(300,100), 100,1)

    #dibujar un elipse
    pygame.draw.ellipse(ventana,naranja,(100,150 ,200, 100), 1)
    
    #  dibujar un arco circunferencia
    pygame.draw.arc(ventana,cian,(300,25,180,150),PI/2,PI,1)

    #texto tamaño 35 negrila y cursiva------------"1,1"
    fuente_arial = pygame.font.SysFont("arial",35,1,1)
    texto = fuente_arial.render("sistemas guaneta", 1, blanco)
    ventana.blit(texto,(50,50))
    #actualiza la visualizacion de la ventana
    pygame.display.flip()
