# importamos la libreria
import pygame
import random
rojo = random.randint(0,255)
verde = random.randint(0,255)
azul = random.randint(0,255)
color_aleatorio = (rojo,verde,azul)
#inicializamos los modulos
pygame.init()

# establecer titulo a la ventana
pygame.display.set_caption("surface")

#esblecemos las dimeciones de la vbetntana
ventana = pygame.display.set_mode((400,400))

#defenimos in color
zul =(0, 0,255)

#crear una superficie

zul_Superficie = pygame.Surface((400,400))
color_Superficie = pygame.Surface((200,200))
#rellenamos la superficie de azul
zul_Superficie.fill(zul)
color_Superficie.fill(color_aleatorio)
#inserto o muevo la superficie de la ventana
ventana.blit(zul_Superficie,(0,0))
ventana.blit(color_Superficie,(100,100))
# actualizo la visualizacion de la ventana
pygame.display.flip()

# bucle del juego
while True:
    event =pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()