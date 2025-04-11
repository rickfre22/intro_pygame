import pygame
import random
import sys
#espaciios para variables
color1 = (114, 178, 207)
blanco = (255,255,255)
color2 =(194, 229, 178)

pygame.init()

ventana = pygame.display.set_mode((500,500))
pygame.display.set_caption(":)")
clock = pygame.time.Clock()
while True:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
    
    ventana.fill(color1)

    fuente_arial = pygame.font.SysFont("arial",30,1,1)
    texto = fuente_arial.render("colegio san jose de guaneta", 1, blanco)
    ventana.blit(texto,(50,10))
    fuente_arial = pygame.font.SysFont("arial",30,1,1)
    texto = fuente_arial.render("especialida sistemas", 1, blanco)
    ventana.blit(texto,(100,40))
    pygame.draw.rect(ventana,color2,(50,100,400,350))
    
    for i in range(100):
        x1 = random.randint(50,300)
        y1 = random.randint(100,450)
        x2 = random.randint(100,450)
        y2 = random.randint(100,350)
        color_random= (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.draw.line(ventana,color_random,(x1,y1),(x2,y2))
        
        pygame.display.flip()