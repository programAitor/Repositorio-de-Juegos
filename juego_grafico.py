```python
import pygame
import sys
import os

# 1. Inicializar Pygame
# Esto prepara todas las herramientas de Pygame
pygame.init()

# 2. Configurar la pantalla
# Definimos el tamaño de la ventana (Ancho, Alto)
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mi Primer Juego Gráfico: Bot-i")

# 3. Definir colores básicos (RGB)
WHITE = (255, 255, 255)

# 4. CARGAR LA IMAGEN DEL PERSONAJE
# Primero, localizamos la ruta del archivo de forma segura
ruta_imagen = os.path.join('assets', 'bot-i.png')

try:
    # Intentamos cargar la imagen
    robot_image = pygame.image.load(ruta_imagen)
    # Convertimos la imagen para que sea más rápida de procesar
    robot_image = robot_image.convert_alpha() 
    
    # OPCIONAL: Si la imagen es muy pequeña, podemos escalarla.
    # robot_image = pygame.transform.scale(robot_image, (50, 50))
    
except pygame.error as e:
    # Si la imagen no se encuentra o hay un error, el juego avisa y se cierra.
    print(f"Error: No se pudo cargar la imagen en {ruta_imagen}. Verifica que el archivo exista.")
    print(f"Detalle del error: {e}")
    pygame.quit()
    sys.exit()

# Definimos el 'Rect' (rectángulo de colisión y posición) del personaje
robot_rect = robot_image.get_rect()
# Posicionamos a Bot-i en el centro de la pantalla al inicio
robot_rect.center = (WIDTH // 2, HEIGHT // 2)
# Definimos la velocidad de movimiento (píxeles por frame)
robot_speed = 5

# 5. El Bucle Principal del Juego (Game Loop)
# Este bucle se ejecuta constantemente para mantener el juego vivo
running = True
clock = pygame.time.Clock() # Controla la velocidad de fotogramas

while running:
    # 6. Gestión de Eventos (Entradas del usuario)
    # Buscamos qué ha pasado (clics, teclas, cerrar ventana)
    for event in pygame.event.get():
        # Si el usuario cierra la ventana, paramos el bucle
        if event.type == pygame.QUIT:
            running = False

    # 7. Movimiento del Jugador (Leer teclas presionadas)
    keys = pygame.key.get_pressed()
    # Las flechas del teclado o WASD
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        robot_rect.x -= robot_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        robot_rect.x += robot_speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        robot_rect.y -= robot_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        robot_rect.y += robot_speed

    # 8. Comprobación de límites (Evitar que Bot-i se salga de la pantalla)
    if robot_rect.left < 0:
        robot_rect.left = 0
    if robot_rect.right > WIDTH:
        robot_rect.right = WIDTH
    if robot_rect.top < 0:
        robot_rect.top = 0
    if robot_rect.bottom > HEIGHT:
        robot_rect.bottom = HEIGHT

    # 9. Dibujo (Renderizado)
    # PASO IMPORTANTE: Primero limpiamos la pantalla con un color de fondo (blanco)
    screen.fill(WHITE)
    # PASO CLAVE: 'Pintamos' (blit) la imagen de Bot-i en su posición actual (rect)
    screen.blit(robot_image, robot_rect)
    
    # Actualizamos toda la pantalla para mostrar el nuevo frame
    pygame.display.flip()

    # 10. Control de tasa de fotogramas
    # Limitamos el juego a 60 frames por segundo (FPS)
    clock.tick(60)

# 11. Limpieza y salida
# Cerramos Pygame y el programa de forma ordenada
pygame.quit()
sys.exit()
