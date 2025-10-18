import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
speed = 7
character_rect = pygame.Rect((250, 150, 50, 50))
character_rect.x = 2
character_rect.y = 2
running = True
while running:
      keys = pygame.key.get_pressed()
      if keys[pygame.K_UP]:
            character_rect.y +=1
      if keys[pygame.K_DOWN]:
            character_rect.y -=1
                   