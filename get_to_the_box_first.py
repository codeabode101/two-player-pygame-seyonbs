import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
speed = 1
speed_2 = 1
character_rect = pygame.Rect((120,120,50,50))
character_rect_2 = pygame.Rect((200,200,50,50))
win_zone_rect = pygame.Rect(150, 164, 167, 167)
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

#border_1 left and right stops

    if character_rect.x < 0:
        character_rect.x = 0
    if character_rect.x > screen.get_width() - character_rect.width:
        character_rect.y = screen.get_height() -  character_rect.height

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

    if character_rect_2.y < 0:
        character_rect_2.y = 0
    if character_rect_2.y > screen.get_height() - character_rect_2.height:
        character_rect_2.y = screen.get_height() -  character_rect_2.height

# win zone check one

        
    if character_rect.x >= 150 and character_rect.x <= 267 and character_rect.y >=164 and character_rect.y <= 281:
            pygame.draw.rect(screen,(0,0,255),win_zone_rect)
            pygame.display.set_caption("player 1 won the game!!!!!!")
           
             


# win zone check two


    if character_rect_2.x >= 150 and character_rect_2.x <= 267 and character_rect_2.y >=164 and character_rect_2.y <= 281:
            pygame.draw.rect(screen,(0,0,255),win_zone_rect)
            pygame.display.set_caption("player 2 won the game!!!!!!")
          
            


#game end commands

    screen.fill((229, 184, 11))
    pygame.draw.rect(screen,(0,0,255),win_zone_rect)
    pygame.draw.rect(screen,(180,180,180),character_rect)
    pygame.draw.rect(screen,(180,180,180),character_rect_2)

    pygame.display.flip


pygame.quit()