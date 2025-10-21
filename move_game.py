import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
speed = 0.1
character_rect = pygame.Rect((250, 150, 50, 50))
character_rect.x = 270
character_rect.y = 270
running = True
while running:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False
      keys = pygame.key.get_pressed()
      if keys[pygame.K_q]:
            running = False
      if keys[pygame.K_UP]:
            character_rect.y -= speed
      if keys[pygame.K_DOWN]:
            character_rect.y += speed
      if keys[pygame.K_LEFT]:
            character_rect.x -= speed
      if keys[pygame.K_RIGHT]:
            character_rect.x += speed
      
      screen.fill((165,234,7))
      pygame.draw.rect(screen, (180,180,180),character_rect,2)
      speed = 1
      character_rect_2 = pygame.Rect((250, 150, 50, 50))
      character_rect_2.x = 270
      character_rect_2.y = 270
      running = True
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False           
      if keys[pygame.K_w]:
            character_rect_2.y -= speed
      if keys[pygame.K_s]:
            character_rect_2.y += speed
      if keys[pygame.K_a]:
            character_rect_2.x -= speed
      if keys[pygame.K_a]:
            character_rect_2.x += speed
      if character_rect.x < 0:
            character_rect.x = 0
      if character_rect.x > 0:
            character_rect = 0          
      pygame.draw.rect(screen, (180,180,180),character_rect_2)      
      pygame.display.flip()                             
pygame.quit()                   