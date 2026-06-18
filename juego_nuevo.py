import pygame
import sys
import os

# 1. Inicializar Pygame
pygame.init()

# 2. Configurar la pantalla (Ancho, Alto)
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("¡Empieza motogp!")

# 3. CARGAR LA IMAGEN DE LA MOTO
ruta_imagen = os.path.join('imagenes', 'bot-i.png')
try:
    robot_image = pygame.image.load(ruta_imagen)
    robot_image = robot_image.convert_alpha() 
    robot_image = pygame.transform.scale(robot_image, (80, 80))
    robot_image.set_colorkey((255, 255, 255)) # Quita el fondo blanco
except pygame.error as e:
    # Si no encuentra la moto, un cuadrado verde de emergencia
    robot_image = pygame.Surface((80, 80))
    robot_image.fill((0, 255, 0))

# 4. CREAR EL FONDO DE LA CARRETERA CON CÓDIGO
fondo_image = pygame.Surface((WIDTH, HEIGHT))
fondo_image.fill((40, 40, 40)) # Gris asfalto

# Dibujamos los laterales verdes (arcén)
pygame.draw.rect(fondo_image, (34, 139, 34), (0, 0, 50, HEIGHT))          # Izquierda
pygame.draw.rect(fondo_image, (34, 139, 34), (WIDTH - 50, 0, 50, HEIGHT))  # Derecha

# Dibujamos las líneas blancas discontinuas del centro
for y in range(0, HEIGHT, 40):
    if y % 80 == 0:
        pygame.draw.rect(fondo_image, (255, 255, 255), (WIDTH // 2 - 5, y, 10, 40))

# Posición inicial de la moto
robot_rect = robot_image.get_rect()
robot_rect.center = (WIDTH // 2, HEIGHT // 2)
robot_speed = 7  

# 5. El Bucle Principal del Juego
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controles del teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        robot_rect.x -= robot_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        robot_rect.x += robot_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:        
        robot_rect.y -= robot_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        robot_rect.y += robot_speed

    # Bordes de la pantalla
    if robot_rect.left < 0: robot_rect.left = 0
    if robot_rect.right > WIDTH: robot_rect.right = WIDTH
    if robot_rect.top < 0: robot_rect.top = 0
    if robot_rect.bottom > HEIGHT: robot_rect.bottom = HEIGHT

    # Dibujado limpio sin duplicados
    screen.blit(fondo_image, (0, 0))     # 1º Fondo carretera
    screen.blit(robot_image, robot_rect) # 2º Moto encima
    pygame.display.flip()                # 3º Actualizar pantalla

    clock.tick(60) 

pygame.quit()
sys.exit()
