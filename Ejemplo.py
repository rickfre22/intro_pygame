import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejemplo de Sprite y Group")

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Colores
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

# Clase Jugador
class Jugador(pygame.sprite.Sprite): # Esta linea crea una clase de tipo jugador, con el () se comportara como un sprite
    def __init__(self): # Este es el constructor de la clase.Cada vez que hacés Jugador(), esto se ejecuta para inicializar ese jugador.
        super().__init__() # Estalinea llama al constructor padre (sprite)
        # Es obligatorio cuando estás heredando de pygame.sprite.Sprite, 
        # porque el Sprite necesita configurarse internamente para funcionar con los grupos (Group).
        self.image = pygame.Surface((50, 50))
        self.image.fill(VERDE)
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 10

    def update(self): #Sirve para actualizar la lógica del sprite en cada frame (por ejemplo: movimiento, animaciones, física, etc).
        teclas = pygame.key.get_pressed()  # De l linea 34 a la 38 l da movimiento al juegador , de izq-der
        if teclas[pygame.K_LEFT] and self.rect.left > 0: 
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x += 5

# Clase Enemigo: (De la linea 40 a la 49) es el ismo comando del jugador pero ahra para los enemigos
class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.velocidad_y = random.randint(2, 5)

    def update(self): #Sirve para actualizar la lógica del sprite en cada frame (por ejemplo: movimiento, animaciones, física, etc).
        self.rect.y += self.velocidad_y
        # Si se va del fondo, reaparece arriba
        if self.rect.top > ALTO: # Este "if"  le da movimento autonomo a los enemigo
            self.rect.x = random.randint(0, ANCHO - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.velocidad_y = random.randint(2, 5)

# Grupos de sprites
todos_los_sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()

# Crear jugador y añadirlo
jugador = Jugador()
todos_los_sprites.add(jugador)

# Crear enemigos y añadirlos
for _ in range(8):
    enemigo = Enemigo()
    todos_los_sprites.add(enemigo)
    enemigos.add(enemigo)

# Bucle principal
corriendo = True
while corriendo:
    clock.tick(60)  # 60 FPS

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Actualizar sprites
    todos_los_sprites.update()

    # Verificar colisión jugador - enemigos
    if pygame.sprite.spritecollideany(jugador, enemigos):
        print("¡Colisión! Game Over.")
        corriendo = False

    # Dibujar en pantalla
    pantalla.fill(NEGRO)
    todos_los_sprites.draw(pantalla)
    pygame.display.flip()

pygame.quit()


