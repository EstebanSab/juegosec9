import Objetos as obj
import sys, pygame ,random


# Creamos la pantalla e iniciamos py game
pygame.init()
screen = pygame.display.set_mode([obj.width,obj.height])
pygame.display.set_caption("Galaga") 


#variables
jugador =obj.Jugador()
naves = []
disparos = []
disparosEnem = []
colision = False
texto = obj.Texto()
puntaje =0


#Fondo estrellado lista de cordenadas
list_cord = []
for i in range(20):
    x = random.randint(0,800)
    y  = random.randint(0,600)
    list_cord.append([x,y])


run = True
while run:
    pygame.time.delay(5)
    pos = (0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
    
    #Dibujo el fondo estrellado
    for cord in list_cord: 
        pygame.draw.circle(screen,obj.colores['rojo'],(cord[0],cord[1]),1)
        cord[1]+=1
        if cord[1] > 600:
            cord[1] = 0

    inicio = texto.escribir('INICIAR',50,'blanco','negro')
    screen.blit(inicio, [300,260])

    if 500 > pos[0] > 300 and 320 > pos[1] > 260:
        run = False

    pygame.display.update()




run = True
while run:
    #Zona de dibujo-----------------------------------------------
    #Dibujo el fondo
    screen.fill(obj.colores['negro'])
    for cord in list_cord: 
        pygame.draw.circle(screen,obj.colores['blanco'],(cord[0],cord[1]),1)
        cord[1]+=1
        if cord[1] > 600:
            cord[1] = 0

    #Dibujo el texto del puntaje
    punt = texto.escribir( ('Puntaje '+str(puntaje)), 32 ,'verde','negro')
    screen.blit(punt,[0,0])

    #Dibujo las naves y los jugadores
    screen.blit(jugador.getImagen(),jugador.getCordenadas())
    for nave in naves:
        screen.blit(nave.getImagen(),nave.getCordenadas())

    #Zona de dibujo-----------------------------------------------

    #Logica----------------------------------------------
    # Espero un tiempo (milisegundos)
    pygame.time.delay(15)
    
    #Eventos de cierre o tecla espacio(Disparos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        #Los Disparos de la nave principal son almacenados en la lista
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                disparos.append(obj.Disparo(jugador.getCordenadas(),screen,True))


    #Movimientos de la nave del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        jugador.mover(0, -5,True)
    if keys[pygame.K_DOWN]:
        jugador.mover(0, 5,False)
    if keys[pygame.K_LEFT]:
        jugador.mover(-5, 0,True)
    if keys[pygame.K_RIGHT]:
        jugador.mover(5, 0,False)
    
    #Movimientos de los disparos de la nave del jugador
    for disparo in disparos:
        nave = disparo.moverArriba(naves)
        if nave != -1 and type(nave) == int:
            del naves[nave] 
            puntaje += 1


    #Agrego nuevas naves enemigas a la lista cada 3 segundos
    tiempo = pygame.time.get_ticks()//100
    if tiempo % 30 == 0:
        posicion = [random.randint(0,600),-100]
        direccion = [random.randint(2,12),random.randint(2,6)]
        naves.append(obj.Enemigo_A(posicion,direccion))

    #Moviento de las naves creadas y disparos si condicion
    for nave in naves:
        nave.mover()
        if 4>(nave.getCordenadas()[0] - jugador.getCordenadas()[0]) > -4:
            disparosEnem.append(obj.Disparo(nave.getCordenadas(),screen,False))
    

    #Movimientos de los disparos de las naves enemigas
    for disparo in disparosEnem:
        colision = disparo.moverAbajo(jugador)
    
    #colision de un disparo de una nave enemiga al jugador
    if colision:
        del jugador
        break   

    
    #Actualizo la pantalla
    pygame.display.update()



#Pantalla de Game over
run = True
pygame.mixer.music.load("./items/gameover.mp3")
pygame.mixer.music.play()
while run: 
    pygame.time.delay(15)

    screen.fill(obj.colores['negro'])

    for cord in list_cord: 
        pygame.draw.circle(screen,obj.colores['blanco'],(cord[0],cord[1]),1)
        cord[1]+=1
        if cord[1] > 600:
            cord[1] = 0

    gameOver = texto.escribir('Game Over ',52,'rojo','negro')
    puntajeEnd = texto.escribir('Puntaje '+str(puntaje),32,'rojo','negro')

    screen.blit(gameOver, [260,250])
    screen.blit(puntajeEnd, [320,304])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
    pygame.display.update()

# Salgo de pygame
pygame.quit()