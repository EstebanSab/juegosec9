
import pygame

class Obstaculo(pygame.Rect):

  def __init__(self, pos: Vector2):
    super().__init__()
    self.rectangulo = pygame.Rect(random.randint(0, pos[0]), random.randint(0, pos[1]), 100, 100)
    self.esCorrecto