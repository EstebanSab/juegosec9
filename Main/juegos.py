import pygame
import random
import sys
from time import sleep
pygame.init()

# - Menu simple
# - Mecánica de niveles
# - Sistema de puntuación: resta puntos a contrario en acierto, resta propios puntos en fallo
# - Barrera de pantalla
# - Modularizar código en funciones, evitar repeticiones
# - Comentarios de código explicativos
# - Código escalable de niveles
# - Cartel de victoria y redirección a menú
# - Superposición de objetos: evitar colisiones aleatorias entre texto, obstáculos y jugadores
# - CSV con imágenes de seañales de tránsito con su respectiva descripción
#def menu():
#    while(true)
        

#definición de colores

def generar_color_random():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    time.sleep(1000)

def generar_color_random1():
    return (random.randint(0,100),random.randint(0,200),random.randint(0,100))

pygame.init()
claro=(151, 201, 92)
azul=(0,0,255)
rojo=(60,45,122)
color= claro
cubo=generar_color_random()
cubo1=generar_color_random1()
ventana=pygame.display.set_mode((1024,720))



señal1=pygame.image.load("señales/1.png")
icono=pygame.image.load("16.png")
jugador=pygame.image.load("jugador1.png").convert_alpha()
jugador1=pygame.image.load("jugador2.png").convert_alpha()
fondo=pygame.image.load("fondo_ciudad1.png")

pygame.display.flip()
pygame.display.set_icon(icono)
reloj=pygame.time.Clock()
running=True
player_pos = pygame.Vector2(110, 400)
player_pos1 = pygame.Vector2(ventana.get_width() / 2, ventana.get_height() / 2)
dt= 0

puntos=[0,0]

font1 = pygame.font.SysFont("ArialBlack", 40)#font with size of 52 and font style specified




pygame.display.set_caption("Leyes de transito")
players = [pygame.Rect(0, 0, 14, 34),pygame.Rect(0, 0, 14, 34)]


#Cartel correcto
obstacle_rect = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)

#cantidad de carteles erroneos
obstacle_num = 4
obstacle_rects= []

for x in range(0,obstacle_num):
    obstacle_rects.append(pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100))





while running:

    #Funcion que carga los obstaculos en posiciones random
    def  obstacle_rects_random():
        for x in range(0, obstacle_num):
             obstacle_rects[x] = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
    
    #Si un jugador toca el cartel correcto
    for x in range(0,2):
        if players[x].colliderect(obstacle_rect) :
            puntos[x]= puntos[x] + 1
            obstacle_rect = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
            obstacle_rects_random()


    #Si un jugador toca un cartel incorrecto 
    for x in range(0, obstacle_num):
        for j in range(0,2):
            if players[j].colliderect(obstacle_rects[x]):
                puntos[j]= puntos[j] - 1
                obstacle_rects[x] = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)

        
        
       
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
           running=False


    ventana.fill(claro)
    ventana.blit(fondo, (0,-100))
    

    pos= pygame.mouse.get_pos()
    players[0].center = player_pos+pygame.math.Vector2(8, 15)
    players[1].center = player_pos1+pygame.math.Vector2(8, 15)
    
    pygame.draw.rect(ventana, color, players[0], -1)
    pygame.draw.rect(ventana, color, players[1], -1)
    


    
    text1= font1.render("Puntuacion(1): " + str(puntos[0]), True,(255,0,0))
    text2= font1.render("Puntuacion(2): " + str(puntos[1]), True,(255,0,0))
    ventana.blit(text1,(20,50))
    ventana.blit(text2,(500,50))



    #Dibujo los obstaculos
    for x in range(0,obstacle_num):
        pygame.draw.rect(ventana, rojo, obstacle_rects[x])
    
    pygame.draw.rect(ventana, "red", obstacle_rect)

    ventana.blit(señal1, obstacle_rect)
    ventana.blit(jugador1, player_pos1)
    ventana.blit(jugador, player_pos)



    #Movimiento de los jugadores
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 30 * dt
    if keys[pygame.K_s]:
        player_pos.y += 30 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 30 * dt
        jugador=pygame.image.load("jugador1invertido.png").convert_alpha()
    if keys[pygame.K_d]:
        player_pos.x += 30 * dt
        jugador=pygame.image.load("jugador1.png").convert_alpha()
    if keys[pygame.K_UP]:
        player_pos1.y -= 30 * dt
    if keys[pygame.K_DOWN]:
        player_pos1.y += 30 * dt
    if keys[pygame.K_LEFT]:
        player_pos1.x -= 30 * dt
        jugador1=pygame.image.load("jugador2invertido.png").convert_alpha()
    if keys[pygame.K_RIGHT]:
        player_pos1.x += 30 * dt
        jugador1=pygame.image.load("jugador2.png").convert_alpha()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    pygame.display.flip()
    dt = reloj.tick(60) / 100
pygame.quit()
