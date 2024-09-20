import sys, pygame


#Variables
width, height = 800, 600
colores = {}
colores['blanco']= 255, 255, 255 
colores['negro'] = 0,0,0
colores['rojo'] = 255, 0, 0
colores['verde'] = 0, 255, 0
colores['azul'] = 0, 0, 128

#Objetos
class Jugador():
    def __init__(self):
        self.nave = pygame.image.load("./items/nave.png").convert()
        self.nave.set_colorkey(colores['negro'])
        self.naveCord = self.nave.get_rect()
        self.naveCord.move_ip(400,400)
    
    def mover(self,x,y,direccion):
        if direccion:
            if self.naveCord.top > 0: 
                self.naveCord[1] += y
            if self.naveCord.left > 0:
                 self.naveCord[0] += x
        else:
            if self.naveCord.right < width:
               self.naveCord[0] += x
            if self.naveCord.bottom < height:
               self.naveCord[1] += y       
            
    def getCordenadas(self):
        return [self.naveCord[0],self.naveCord[1]]
    
    def getImagen(self):
        return self.nave
    
    def getRect(self):
        return self.naveCord



class Enemigo_A():
    def __init__(self,posicion,direcion):
        self.naveEnem = pygame.image.load("./items/naveEnem1.png").convert()
        self.naveEnem.set_colorkey(colores['negro'])
        self.direccion = direcion
        self.naveEnemCord = self.naveEnem.get_rect()      
        self.naveEnemCord.move_ip(posicion[0],posicion[1])  
        

    def mover(self):
        if self.naveEnemCord[0] < 0 or self.naveEnemCord[0] > (width-30):
            self.direccion[0] = -self.direccion[0]
        self.naveEnemCord[0] += self.direccion[0]
        
        if self.naveEnemCord[1] > 800:
            self.naveEnemCord[1] = -20
        self.naveEnemCord[1] += self.direccion[1]

    def getCordenadas(self):
        return [self.naveEnemCord[0],self.naveEnemCord[1]]
    
    def getImagen(self):
        return self.naveEnem
    
    def getRect(self):
        return self.naveEnemCord



class Disparo():
    def __init__(self,xy,screen,nave):
        self.screen = screen
        self.tipoNave = nave
        
        if nave:
            self.xIzq = xy[0] +55
            self.xDer = xy[0] +25
            self.y = xy[1]
            self.disparoIzq = pygame.draw.circle(self.screen,colores.get('rojo'),(self.xIzq, self.y),5)
            self.disparoDer = pygame.draw.circle(self.screen,colores.get('rojo'),(self.xDer, self.y),5)
            
        else:
            self.x = xy[0] +30
            self.y = xy[1] +50
            self.disparo = pygame.draw.circle(self.screen,colores.get('verde'),(self.x,self.y),5)
        
        sonidoDisparo = pygame.mixer.Sound("./items/laser5.ogg")
        sonidoDisparo.play()
        
    
    
    def moverArriba(self,naves):
        if self.disparoIzq[1] > 0 and self.tipoNave:
            self.disparoIzq = pygame.draw.circle(self.screen,colores.get('rojo'),(self.xIzq, self.y),5)
            self.disparoDer = pygame.draw.circle(self.screen,colores.get('rojo'),(self.xDer, self.y),5)
            self.y -= 8
            cont = -1
            for nave in naves:
                cont+=1
                if self.disparoIzq.colliderect(nave.getRect()) or self.disparoDer.colliderect(nave.getRect()):
                    return cont
            return -1


    def moverAbajo(self,nave):
        if self.disparo[1] < 650:
            self.disparo = pygame.draw.circle(self.screen,colores.get('verde'),(self.x, self.y),5)
            self.y += 8
            if self.disparo.colliderect(nave.getRect()):
                return True


class Texto():
    def escribir(self,input,tam,color,fondo):
        self.font = pygame.font.Font('freesansbold.ttf', tam)
        self.text = self.font.render(input, True,colores[color], colores[fondo])
        return self.text
    
    def getRect(self):
        return self.text.get_Rect()

