import pygame

color = [255, 0, 0] 
rectangles = []

def rectangle_manager(mousex, mousey, width, height, click):
    if click:
        rectangles.append(pygame.Rect(mousex - (height / 2), mousey - (width / 2) , width, height))

def color_cycler(pressed, color):
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

def color_changer(keys):
    if keys[pygame.K_r]:
        print("r")
        color = (255, 0, 0)
        print(color)
    elif keys[pygame.K_o]:
        color = (255, 165, 0)
    elif keys [pygame.K_y]:
        color = ()


def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()

    click = False
    running = True
    width, height = 50, 50
    while running:

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed() 
        mousex, mousey = pygame.mouse.get_pos()

        if keys[pygame.K_UP] and width < 100:
            width += 3
            height += 3
        if keys[pygame.K_DOWN] and width > 10:
            width -= 3
            height -= 3

        color = color_changer(keys)
        
        #color = color_cycler(keys[pygame.K_SPACE], color)
        rectangle_manager(mousex, mousey, width, height, click)

        #draw the screen
        screen.fill((255,255,255))
        for i in rectangles:
            pygame.draw.rect(screen, color, (i))

        #update the screen
        clock.tick(90)
        pygame.display.flip()

main()

pygame.quit()
quit()