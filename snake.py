import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def round_by(x):
    return round(x/ 40) *40

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake #1")

x = round_by(random.randint(5,745))
y = round_by(random.randint(5,545))

player = pygame.Rect((300,250,40,40))
border = pygame.Rect((5,5,790,590))
apple = pygame.Rect((x,y, 40,40))


clock = pygame.time.Clock()
DIRECTION = "right"
run = True
while run:

    screen.fill((255,255,255))

    pygame.draw.rect(screen,(255,215,0), apple)
    pygame.draw.rect(screen, (255,0,0), player)
    pygame.draw.rect(screen, (0,0,0), border, 1)



    #Constant movement

    if DIRECTION == "right":
        player.x += 10
    if DIRECTION == "left":
        player.x -= 10
    if DIRECTION == "up":
        player.y -= 10
    if DIRECTION == "down":
        player.y += 10


    #check for INPUTS
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True and DIRECTION != "right":
        DIRECTION = "left"
        player.y = round_by(player.y)
    if key[pygame.K_d] == True and DIRECTION != "left":
        DIRECTION = "right"
        player.y = round_by(player.y)
    if key[pygame.K_w] == True and DIRECTION != "down":
        DIRECTION = "up"
        player.x = round_by(player.x)
    if key[pygame.K_s] == True and DIRECTION != "up":
        DIRECTION = "down"
        player.x = round_by(player.x)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    
    #check for collision
    if player.x >= 755:
        player.x = 755 
    if player.x <= 5:
        player.x = 5
    if player.y >= 555:
        player.y = 555
    if player.y <= 5:
        player.y = 5

    if apple.x >= 755:
        apple.x = 755 
    if apple.x <= 5:
        apple.x = 5
    if apple.y >= 555:
        apple.y = 555
    if apple.y <= 5:
        apple.y = 5

    if player.colliderect(apple):
        apple.x = round_by(random.randint(5,745))
        apple.y = round_by(random.randint(5,545))
        
        




    pygame.display.update()
    clock.tick(60)

pygame.quit()