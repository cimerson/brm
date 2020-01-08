import pygame

pygame.init()

display_w = 800
display_h = 600

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_w,display_h))
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green

pygame.draw.line(gameDisplay, white, (100, 200), (300, 450), 5)

pygame.draw.rect(gameDisplay, red, (400, 400, 50 ,25))

pygame.draw.circle(gameDisplay, blue, (150, 150), 86)

pygame.draw.polygon(gameDisplay, green, ((345,78),(23,89), (787,8), (86,321), (45,90)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
    pygame.display.update()