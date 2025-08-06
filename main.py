import pygame

pygame.init()

screen_width, screen_height = 1800, 1023
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BOUNDARIES ARE SOOOOO COOOOOOOL")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
DARKBLUE = (25, 45, 66)
LIGHTPISTACHIO = (170, 183, 183)
GREEN = (0, 255, 0)

square_size = 50
square_x = 0
square_y = 0
square_speed = 0.3

platforms = pygame.Rect(0, 150, 50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    #movment
    if keys[pygame.K_UP]:
        square_y -= square_speed
    if keys[pygame.K_DOWN]:
        square_y += square_speed
    if keys[pygame.K_LEFT]:
        square_x -= square_speed
    if keys[pygame.K_RIGHT]:
        square_x += square_speed

    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.quit()

    

    player = pygame.Rect(square_x, square_y, square_size, square_size)

    if square_x < 0:
        square_x = 0
    if square_x + square_size > screen_width:
        square_x = screen_width - square_size
    if square_y < 0:
        square_y = 0
    if square_y + square_size > screen_height:
        square_y = screen_height - square_size



    screen.fill(LIGHTPISTACHIO)
    pygame.draw.rect(screen, DARKBLUE, player, 5, border_radius= 15)
    
 
    pygame.draw.rect(screen, RED, platforms)
    

    pygame.display.flip()

pygame.quit()
