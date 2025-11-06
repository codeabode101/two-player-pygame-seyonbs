import pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
RED =  (255,0,0)
speed = 1
speed_2 = 1
character_rect = pygame.Rect((270, 270, 50, 50))
character_rect_2 = pygame.Rect((150, 150, 50, 50))    
character_rect_2.x = 67
character_rect_2.y = 67
safe_zone_rect = pygame.Rect(150, 164, 167, 67)
running = True



#main game loop setup



while running:
      for event in pygame.event.get():
             if event.type == pygame.QUIT:   
                  running = False
      keys = pygame.key.get_pressed()
      if keys[pygame.K_q]:
            running = False


#key check setup 1


      if keys[pygame.K_UP]:
            character_rect.y -= speed
      if keys[pygame.K_DOWN]:
            character_rect.y += speed
      if keys[pygame.K_LEFT]:
            character_rect.x -= speed
      if keys[pygame.K_RIGHT]:
            character_rect.x += speed

#key check setup 2      
                
      if keys[pygame.K_w]:
            character_rect_2.y -= speed_2
      if keys[pygame.K_s]:
            character_rect_2.y += speed_2
      if keys[pygame.K_a]:
            character_rect_2.x -= speed_2
      if keys[pygame.K_d]:
            character_rect_2.x += speed_2

#border_1,left and right stops


      if character_rect.x < 0:
            character_rect.x = 0
      if character_rect.x > screen.get_width() - character_rect.width:
            character_rect.x = screen.get_width() - character_rect.width

#border_1,up and down stops


      if character_rect.y < 0:
            character_rect.y = 0
      if character_rect.y > screen.get_height() - character_rect.height:
            character_rect.y = screen.get_height() -  character_rect.height

#border_2,left and right stops

      if character_rect_2.x < 0:
            character_rect_2.x = 0
      if character_rect_2.x > screen.get_width() - character_rect_2.width:
            character_rect_2.x = screen.get_width() - character_rect_2.width

#border_2,up and down stops

      if character_rect_2.y < 0:
            character_rect_2.y = 0
      if character_rect_2.y > screen.get_height() - character_rect_2.height:
            character_rect_2.y = screen.get_height() -  character_rect_2.height


      if character_rect.x == safe_zone_rect  and  character_rect.y == safe_zone_rect:
            pygame.draw.rect(screen,(255,0,0),safe_zone_rect)



            
      if character_rect.x == safe_zone_rect  and  character_rect.y == safe_zone_rect:
            pygame.draw.rect(screen,(255,54,45),safe_zone_rect)  



      screen.fill((165,234,7))
      pygame.draw.rect(screen, (0,0,255),safe_zone_rect)        
      pygame.draw.rect(screen, (180,180,180),character_rect_2)
      pygame.draw.rect(screen, (180, 180, 180), character_rect)    
      pygame.display.flip()


#game end command


pygame.quit()                   