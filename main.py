import pygame
import time
import random

pygame.init()

display_w = 800
display_h = 600

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_w,display_h))

pygame.display.set_caption('A brm brm')

clock = pygame.time.Clock()

carImg = pygame.image.load('car32.png')

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    textSurf, textRect = text_objects(text, largeText)
    textRect.center = ((display_w/2), (display_h/2))
    gameDisplay.blit(textSurf, textRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('BOOOOM')

def game_loop():
    x = (display_w * 0.45)
    y = (display_h * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_w)
    thing_starty = -600
    thing_speed = 7
    thing_width = 70
    thing_height = 90

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 32
                elif event.key == pygame.K_RIGHT:
                    x_change = 32
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            x += x_change

        gameDisplay.fill(black)

        things(thing_startx, thing_starty, thing_width, thing_height, white)
        thing_starty += thing_speed
        car(x,y)

        if x > display_w-72 or x < 0:
            crash()

        if thing_starty > display_h:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_w)

        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+72 > thing_startx and x + 72 < thing_startx + thing_width:
                crash()

        pygame.display.update()

        clock.tick(60)

game_loop()
# pygame.quit()
# quit()