import pygame
import sys


blue = (0,0,205)
white = (255,255,255)
red = (255, 0, 0)

width = 800
height = 600

pygame.display.init()
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption('goldfish')
clock = pygame.time.Clock()

badx = 0
bady = 0

myx = width/2
myy = height/2

w = False
a = False
d = False
s = False

gameloop = True

while gameloop:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                w = True
            if event.key == pygame.K_a:
                a = True
            if event.key == pygame.K_s:
                s = True
            if event.key == pygame.K_d:
                d = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                w = False
            if event.key == pygame.K_a:
                a = False
            if event.key == pygame.K_s:
                s = False
            if event.key == pygame.K_d:
                d = False

    if w:
        myy -= 5
    if a:
        myx -= 5
    if s:
        myy += 5
    if d:
        myx += 5

    if myx < 0:
        myx = 0
    if myy < 0:
        myy = 0
    if myx > 700:
        myx = 700
    if myy > 500:
        myy = 500

    if badx > myx:
        badx -= 3
    if badx < myx:
        badx += 3
    if bady > myy:
        bady -= 3
    if bady < myy:
        bady += 3

    myx,myy = pygame.mouse.get_pos()

    player = pygame.Rect(myx, myy, 30, 30)
    bad_guy = pygame.Rect(badx, bady, 30, 30)

    collide = pygame.Rect.colliderect(player, bad_guy)

    if collide:
        break

    pygame.Surface.fill(screen, white)
    pygame.draw.rect(screen ,red,(bad_guy))
    pygame.draw.rect(screen, blue, player)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()