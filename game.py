import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
color = [255, 0, 0]  

def color_changer(pressed, color):
    if pressed:
        if color[2] <= 0 and color[1] < 255:
            color[1] += 3  
        if color[1] >= 255 and color[0] > 0:
            color[0] -= 3
        if color[0] <= 0 and color[2] < 255:
            color[2] += 3
        if color[2] >= 255 and color[1] > 0:
            color[1] -= 3
        if color[1] <= 0 and color[0] < 255:
            color[0] += 3
        if color[0] >= 255 and color[2] > 0 :
            color[2] -= 3
        
    color = tuple(color)
    screen.fill(color)

def main():
    pressed = False
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed = True
                if event.key == pygame.K_r:
                    red = True
                if event.key == pygame.K_g:
                    green = True
                if event.key == pygame.K_b:
                    blue = True
                if event.key == pygame.K_m:
                    magenta = True
                if event.key == pygame.K_c:
                    cyan = True
                if event.key == pygame.K_y:
                    yellow = True
            if event.type == pygame.KEYUP:
                pressed = False
            if event.type == pygame.QUIT:
                running = False

        color_changer(pressed, color)
        clock.tick(60)
        pygame.display.flip()

main()

pygame.quit()
quit()