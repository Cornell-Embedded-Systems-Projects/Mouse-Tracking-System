#!/usr/bin/python
from pynput.mouse import Button, Controller, Listener

import sys, pygame
pygame.init()

size = width, height = 300, 300
speed = [2, 2]
black = 0, 0, 0
color = 255, 0, 0

screen = pygame.display.set_mode(size)

position=[300,300]
scale=1
DPI=300
pygame.draw.circle(screen, color, position, 5, 0)
while True:
    pygame.event.pump()
    
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    displacement=pygame.mouse.get_rel()

    if displacement[0]!=0 or displacement[1]!=0:
        position[0]+=int(displacement[0]*scale)
        position[1]+=int(displacement[1]*scale)
        print(position)
        screen.fill(black)
        pygame.draw.circle(screen, color, position, 5, 0)
        pygame.display.update()
