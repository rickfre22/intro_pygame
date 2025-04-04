import pygame
pygame.init()
pygame.display.set_caption("colombia")
ventana = pygame.display.set_mode((400,400))
amarilllo = (255, 247, 0)
azul = (0, 36, 255)
rojo = (249, 4, 4)

amarilllo_Superficie = pygame.Surface((400,200))
azul_Superficie = pygame.Surface((400,100))
rojo_Superficie = pygame.Surface((400,100))

amarilllo_Superficie.fill(amarilllo)
azul_Superficie.fill(azul)
rojo_Superficie.fill(rojo)
ventana.blit(amarilllo_Superficie,(0,0))
ventana.blit(azul_Superficie,(0,200))
ventana.blit(rojo_Superficie,(0,300))
pygame.display.flip()
while True:
    event =pygame.event.wait()
    if event.type == pygame.QUIT:
        break
pygame.quit()

