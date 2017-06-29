import pygame
from pygame.locals import *
import os
import sys

#os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
#os.putenv('SDL_FBDEV', '/dev/fb1')
#os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
#os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
#pygame.mouse.set_visible(False)
pygame.mouse.set_visible(True)

#Screen size in pixels
size=[300,300]

position = size

#Mouse Displacement (x,y)
disp = [0,0]
scale = 0.5

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0

screen = pygame.display.set_mode((size[0], size[1])) #the size of the whole panel
my_font = pygame.font.Font(None, 50)
my_buttons1 = { '1':(int(size[0]/6),int(size[1]/6))}
my_buttons2 = { '2':(int(size[0]*3/6),int(size[1]/6))}
my_buttons3 = { '3':(int(size[0]*5/6),int(size[1]/6))}
my_buttons4 = { '4':(int(size[0]/6),int(size[1]*3/6))}
my_buttons5 = { '5':(int(size[0]*3/6),int(size[1]*3/6))}
my_buttons6 = { '6':(int(size[0]*5/6),int(size[1]*3/6))}
my_buttons7 = { '7':(int(size[0]/6),int(size[1]*5/6))}
my_buttons8 = { '8':(int(size[0]*3/6),int(size[1]*5/6))}
my_buttons9 = { '9':(int(size[0]*5/6),int(size[1]*5/6))}


def drawGrid():
    screen.fill(BLACK) # Erase the Work space

    for my_text, text_pos in my_buttons1.items():
        text_surface = my_font.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)

    for my_text, text_pos in my_buttons2.items():
        text_surface = my_font.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)

    for my_text, text_pos in my_buttons3.items():
        text_surface = my_font.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)

    for my_text, text_pos in my_buttons4.items():
        text_surface = my_font.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)

    for my_text, text_pos in my_buttons5.items():
        text_surface = my_font.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)

    for my_text, text_pos in my_buttons6.items():
        text_surface = my_font.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)

    for my_text, text_pos in my_buttons7.items():
        text_surface = my_font.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)


    for my_text, text_pos in my_buttons8.items():
        text_surface = my_font.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)

    for my_text, text_pos in my_buttons9.items():
        text_surface = my_font.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)

    #q = False
    h1 = False
    h2 = False
    h3 = False
    h4 = False
    h5 = False
    h6 = False
    h7 = False
    h8 = False
    h9 = False
    return

while True:
    pygame.event.pump()
    for event in pygame.event.get():

        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()


        disp = pygame.mouse.get_rel()
	    
        if (disp[0] != 0 or disp[1] != 0):
            print('potato!')
            position[0] += int(disp[0]*scale)
            position[1] += int(disp[1]*scale)
            drawGrid()
            print(position)

            pygame.draw.circle(screen, RED, position, 5, 0)

            pygame.display.update()

        pos = pygame.mouse.get_pos()
        x,y = pos
        print ("At " + str(x) + ", " + str(y))
        if y < int(size[1]/3) and y > 0: 
            if x < int(size[0]/3) and x > 0:
                h1 = True
                print ("grid 1 is pressed")
            elif x < int(size[0]*2/3) and x > int(size[0]/3):
                h2 = True
                print ("grid 2 is pressed")
            else:
                h3 = True 
                print ("grid 3 is pressed")
        elif y < int(size[1]*2/3) and y > int(size[1]/3):
            if x < int(size[0]/3) and x > 0:
                h4 = True
                print ("grid 4 is pressed")
            elif x < int(size[0]*2/3) and x > int(size[0]/3):
                h5 = True
                print ("grid 5 is pressed")
            else:
                h6 = True
                print ("grid 6 is pressed")
        else:
            if x < int(size[0]/3) and x > 0:
                h7 = True
                print ("grid 7 is pressed")
            elif x < int(size[0]*2/3) and x > int(size[0]/3):
                h8 = True
                print ("grid 8 is pressed")
            else:
                h9 = True
                print ("grid 9 is pressed")


            
