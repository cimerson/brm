import pygame
import time
import random

pygame.init()

display_w = 800
display_h = 600

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
darkGrey = (105,105,105)

gameDisplay = pygame.display.set_mode((display_w,display_h))

pygame.display.set_caption('A brm brm')

clock = pygame.time.Clock()

carImg = pygame.image.load('car32.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged ' + str(count), True, white)
    gameDisplay.blit(text, (0, 0))


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

def button(label, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
            # if action == 'play':
            #     game_loop()
            # elif action == 'quit':
            #     pygame.quit()
            #     quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(label, smallText)
    textRect.center = ((x + w/2), (y + h/2))
    gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        textSurf, textRect = text_objects('A brm brmmm', largeText)
        textRect.center = ((display_w/2), (display_h/2))
        gameDisplay.blit(textSurf, textRect)

        button('Go!', 150, 450, 100, 50, white, darkGrey, game_loop)
        button('Quit', 550, 450, 100, 50, white, darkGrey, game_quit)

        # mouse = pygame.mouse.get_pos()

        # if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
        #     pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))
        # else:
        #     pygame.draw.rect(gameDisplay, white, (150, 450, 100, 50))

        # smallText = pygame.font.Font('freesansbold.ttf', 20)
        # textSurf, textRect = text_objects('Go!', smallText)
        # textRect.center = ((150 + 100/2), (450 + 50/2))
        # gameDisplay.blit(textSurf, textRect)

        # pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))

        pygame.display.update()
        clock.tick(15)

def game_quit():
    pygame.quit()
    quit()


def game_loop():
    x = (display_w * 0.45)
    y = (display_h * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_w)
    thing_starty = -600
    thing_speed = 4
    thing_width = 70
    thing_height = 90

    dodged = 0

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
        things_dodged(dodged)

        if x > display_w-72 or x < 0:
            crash()

        if thing_starty > display_h:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_w)
            dodged += 1
            thing_speed += 0.1
            thing_width += (dodged * 1.2)


        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+72 > thing_startx and x + 72 < thing_startx + thing_width:
                crash()

        pygame.display.update()

        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()