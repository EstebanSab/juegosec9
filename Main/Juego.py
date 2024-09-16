import pygame
import random
import sys

from .Obstaculo import Obstaculo

from time import sleep


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

#creación de las hitboxes
#def __init__ (self,x ,y): 
    #self.x = x
    #self.y = y
    #self.hitbox = (self.x, self.y, 64, 64)
pygame.display.set_caption("Leyes de tránsito")
rect_1 = pygame.Rect(0, 0, 14, 34)
rect_2 = pygame.Rect(0, 0, 14, 34)
obstaculos = [pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100) for i in range(4)]
# obstacle_rect = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
# obstacle_rect2 = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
# obstacle_rect3 = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
# obstacle_rect4 = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)


señal1=pygame.image.load("recursos/señales/1.png")
icono=pygame.image.load("recursos/16.png")
jugador=pygame.image.load("recursos/jugador1.png").convert_alpha()
jugador1=pygame.image.load("recursos/jugador2.png").convert_alpha()
fondo=pygame.image.load("recursos/fondo_ciudad1.png")
pygame.display.flip()
pygame.display.set_icon(icono)
reloj=pygame.time.Clock()
player_pos = pygame.Vector2(110, 400)
player_pos1 = pygame.Vector2(ventana.get_width() / 2, ventana.get_height() / 2)
dt= 0

puntos1=0
puntos2=0
font2 = pygame.font.SysFont("ArialBlack", 40)#font with size of 52 and font style specified
text2= font2.render("Toque una señal: " + str(puntos1), True,(0,0,255))#text color specified to blue

font3 = pygame.font.SysFont("ArialBlack", 40)#font with size of 52 and font style specified
text3= font3.render("Toque una señal: " + str(puntos2), True,(0,0,255))#text color specified to blue

class Juego:

    def __init__(self):
        pygame.init()
        self.corriendo = True
        self.ventana = pygame.display.set_mode((1024,720))

    def Correr(self):
        while corriendo:
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
            ventana.fill(claro)
            ventana.blit(fondo, (0,-100))
            ventana.blit(text2,(20,50))
            ventana.blit(text3,(500,50))

            #colision
            for obstaculo in obstaculos:
                if rect_1.colliderect(obstaculo):
                    color= rojo
                    puntos1 = puntos1 + 1
                    obstaculos = [pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100) for i in range(4)]
                    text2 = font2.render("Puntuacion(1): " + str(puntos1), True,(255,0,0))
            for obstaculo in obstaculos:
                if rect_2.colliderect(obstaculo):
                    color= rojo
                    puntos2 = puntos2 + 1
                    obstaculos = [pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100) for i in range(4)]
                    text3 = font2.render("Puntuacion(2): " + str(puntos2), True,(255,0,0))

            # if rect_1.colliderect(obstacle_rect) :
                #text3= font3.render("Puntuacion(2): " + str(puntos2), True,(255,0,0))

            if rect_2.colliderect(obstacle_rect):
                color= rojo
                puntos2= puntos2 + 1
                #cubo=azul
                obstacle_rect = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
                obstacle_rect2 = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
                obstacle_rect3 = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
                obstacle_rect4 = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
                #text2= font2.render("Puntuacion(1): " + str(puntos1), True,(255,0,0))
                text3= font3.render("Puntuacion(2): " + str(puntos2), True,(255,0,0))

            else:
                color=claro
                
            #incorrecto colision 2
                
            if rect_1.colliderect(obstacle_rect2):
                color= rojo
                puntos1= puntos1 - 1
                #cubo=azul
                obstacle_rect2 = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
                text2= font2.render("Puntuacion(1): " + str(puntos1), True,(255,0,0))
                #text3= font3.render("Puntuacion(2): " + str(puntos2), True,(255,0,0))

            else:
                color=claro
                #cubo=generar_color_random
            if rect_2.colliderect(obstacle_rect2):
                color= rojo
                puntos2= puntos2 - 1
                #cubo=azul
                obstacle_rect2 = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
                #text2= font2.render("Puntuacion(1): " + str(puntos1), True,(255,0,0))
                text3= font3.render("Puntuacion(2): " + str(puntos2), True,(255,0,0))

            else:
                color=claro
                #cubo=generar_color_random
                
            #incorrecto colision 3
                
            if rect_1.colliderect(obstacle_rect3):
                color= rojo
                puntos1= puntos1 - 1
                #cubo=azul
                obstacle_rect3 = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
                text2= font2.render("Puntucaion(1): " + str(puntos1), True,(255,0,0))
                #text3= font3.render("Puntuacion(2): " + str(puntos2), True,(255,0,0))

            if rect_2.colliderect(obstacle_rect3):
                color= rojo
                puntos2= puntos2 - 1
                #cubo=azul
                obstacle_rect3 = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
                #text2= font2.render("Puntucaion(1): " + str(puntos1), True,(255,0,0))
                text3= font3.render("Puntuacion(2): " + str(puntos2), True,(255,0,0))

            else:
                color=claro
                
            #incorrecto colision 4
                
            if rect_1.colliderect(obstacle_rect4): #or rect_2.colliderect(obstacle_rect4):
                color= rojo
                puntos1= puntos1 - 1
                #cubo=azul
                obstacle_rect4 = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
                text2= font2.render("Puntuacion(1): " + str(puntos1), True,(255,0,0))
                #text3= font3.render("Puntuacion(2): " + str(puntos2), True,(255,0,0))

            if rect_2.colliderect(obstacle_rect4):
                color= azul
                puntos2= puntos2 - 1
                #cubo=azul
                obstacle_rect4 = pygame.Rect(random.randint(0, 900), random.randint(0, 700), 100, 100)
                #text2= font2.render("Puntuacion(1): " + str(puntos1), True,(255,0,0))
                text3= font3.render("Puntuacion(2): " + str(puntos2), True,(255,0,0))

        
            else:
                color=claro
                #cubo=generar_color_random
            #puntos
                


            pos= pygame.mouse.get_pos()
            rect_1.center = player_pos+pygame.math.Vector2(8, 15)
            rect_2.center = player_pos1+pygame.math.Vector2(8, 15)
            
            pygame.draw.rect(ventana, color, rect_1, -1)
            pygame.draw.rect(ventana, color, rect_2, -1)
            pygame.draw.rect(ventana, "red", obstacle_rect)
            pygame.draw.rect(ventana, rojo, obstacle_rect2)
            pygame.draw.rect(ventana, rojo, obstacle_rect3)
            pygame.draw.rect(ventana, rojo, obstacle_rect4)
            ventana.blit(señal1, obstacle_rect)

            ventana.blit(jugador1, player_pos1)
            ventana.blit(jugador, player_pos)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                player_pos.y -= 30 * dt
            if keys[pygame.K_s]:
                player_pos.y += 30 * dt
            if keys[pygame.K_a]:
                player_pos.x -= 30 * dt
                jugador=pygame.image.load("recursos/jugador1invertido.png").convert_alpha()
            if keys[pygame.K_d]:
                player_pos.x += 30 * dt
                jugador=pygame.image.load("recursos/jugador1.png").convert_alpha()
            if keys[pygame.K_UP]:
                player_pos1.y -= 30 * dt
            if keys[pygame.K_DOWN]:
                player_pos1.y += 30 * dt
            if keys[pygame.K_LEFT]:
                player_pos1.x -= 30 * dt
                jugador1=pygame.image.load("recursos/jugador2invertido.png").convert_alpha()
            if keys[pygame.K_RIGHT]:
                player_pos1.x += 30 * dt
                jugador1=pygame.image.load("recursos/jugador2.png").convert_alpha()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
            pygame.display.flip()
            dt = reloj.tick(60) / 100
        pygame.quit()
