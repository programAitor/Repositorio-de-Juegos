import pygame
import sys
import os

# 1. Inicializar Pygame
pygame.init()

# 2. Configurar la pantalla (Ancho, Alto)
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mi Primer Juego Gráfico: Bot-i")

# 3. Definir color de fondo (Gris oscuro para que resalte el robot)
BG_COLOR = (30, 30, 30)

# 4. CARGAR LA IMAGEN DEL PERSONAJE
# Usamos 'imagenes' porque así es como llamaste a tu carpeta en VS Code
ruta_imagen = os.path.join('imagenes', 'bot-i.png')

try:
    robot_image = pygame.image.load(ruta_imagen)
    robot_image = robot_image.convert_alpha() 
    # Hacemos al robot un poquito más grande para que se vea genial
    robot_image = pygame.transform.scale(robot_image, (80, 80))
    
except pygame.error as e:
    print(f"Error: No se pudo cargar la imagen en {ruta_imagen}.")
    print("Verifica que la carpeta 'imagenes' esté en el mismo sitio que este archivo .py")
    pygame.quit()
    sys.exit()

# Posición inicial de Bot-i
robot_rect = robot_image.get_rect()
robot_rect.center = (WIDTH // 2, HEIGHT // 2)
robot_speed = 7  # Velocidad de movimiento

# 5. El Bucle Principal del Juego
running = True
clock = pygame.time.Clock()

while running:
    # 6. Capturar si el usuario cierra la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 7. Movimiento con Teclado (Flechas o WASD)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        robot_rect.x -= robot_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        robot_rect.x += robot_speed
    if keys[keys[pygame.K_UP]] or keys[pygame.K_w]:
        robot_rect.y -= robot_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        robot_rect.y += robot_speed

    # 8. Evitar que se salga de los bordes de la pantalla
    if robot_rect.left < 0: robot_rect.left = 0
    if robot_rect.right > WIDTH: robot_rect.right = WIDTH
    if robot_rect.top < 0: robot_rect.top = 0
    if robot_rect.bottom > HEIGHT: robot_rect.bottom = HEIGHT

    # 9. Dibujar en la pantalla
    screen.fill(BG_COLOR)          # Fondo gris
    screen.blit(robot_image, robot_rect) # Pintar robot
    pygame.display.flip()          # Actualizar ventana

    clock.tick(60) # 60 FPS

pygame.quit()
sys.exit()
