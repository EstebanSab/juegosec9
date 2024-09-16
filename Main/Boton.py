
import pygame

class Boton(pygame.sprite.Sprite):
    def __init__(self, texto, posicion, tamano, callback) -> None:
        super().__init__()
        self.posicion = posicion
        self.tamano = tamano
        self.callback = callback

        self.cliqueado = False
        self.listo = False

        self.image = pygame.Surface(tamano)
        self.image.fill("black")
        self.rectangulo = self.image.get_rect()

        superficie_texto = font.render(texto, True, fg)
        rectangulo_texto = superficie_texto.get_rect(center = self.rectangulo.center)
        self.image.blit(superficie_texto, rectangulo_texto)
        self.rect.center = posicion

    def actualizar(self):
        posicion_mouse = pygame.mouse.get_pos()
        boton_izq, *_ = pygame.mouse.get_pressed()
        colision = self.rect.collidepoint(mouse_pos)
        # Detecta si cliqueó, y si hay colisión (mouse encima del botón),
        # deja en un estado de "listo para llamar a la función".
        if boton_izq and not self.cliqueado:
            self.cliqueado = True
            if colision:
                self.listo = True
            elif not colision:
                self.listo = False

        # Si estaba "listo", quiere decir que dejó de cliquear, así que llama al callback.
        if not boton_izq:
            self.cliqueado = False
            if colision and self.listo:
                self.callback()
            self.listo = False
