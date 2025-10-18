import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
speed = 7
character_rect = pygame.Rect((250, 150, 50, 50))
running = True
while running:
      keys = pygame.key.get_pressed()
      if character_rect[keys[pygame.K_UP]]:
        pass