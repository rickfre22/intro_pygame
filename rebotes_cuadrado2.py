import pygame
import sys
import random


rojo =(255,0,0)
azul =(0,45,45)
color1 = (0,245,34)
color2 = (151, 37, 37)
color3= (127, 151, 162)


pygame.init()
ventana = pygame.display.set_mode((500,500))

pygame.display.set_caption("el cuadro que rebota")

clock = pygame.time.Clock()
 
XX = 300
MOVIMIENTO = 1

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    XX = XX + MOVIMIENTO 

    if XX >= 450:
        XX = 450
        MOVIMIENTO =-1
    elif XX<= 0:
        XX = 0
        MOVIMIENTO = 1

    pygame.draw.rect(ventana,rojo,(XX,0,50,50))
    
    pygame.draw.rect(ventana,color1,(XX,450,50,50))
    
    pygame.draw.rect(ventana,color2,(0,XX,50,50))
    
    pygame.draw.rect(ventana,color3,(450,XX,50,50))
    
    rojo1  =random.randint(0,255)
    verde1 = random.randint(0,255)
    azul1 = random.randint(0,255)
    color_random = (rojo1,verde1,azul1,)
    pygame.draw.rect(ventana,color_random,(200,200,100,100))
    pygame.display.flip()