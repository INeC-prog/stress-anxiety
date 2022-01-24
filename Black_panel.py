import pygame
pygame.init()
import time
global my_timer
from pygame.locals import *
import sys
import random
import threading

def countdown():
    global my_timer
    my_timer = 2

    for x in range(2):
        my_timer = my_timer - 1
        time.sleep(1)

        for i in range(2, 0, -1):
            print(i)
            time.sleep(1)

countdown_thread = threading.Thread(target= countdown)
countdown_thread.start()

while my_timer > 0:

    class Prey:
        def __init__(self, parent_screen):
            self.parent_screen = parent_screen
            self.block = pygame.image.load("Resources/blue square.jpg").convert()
            self.direction = 'up'


        def draw(self):
           self.parent_screen.fill((0, 0, 0))

           for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[0], self.y[0]))
           pygame.display.flip()

    class Game:
        def __init__(self):
            pygame.init()
            self.surface = pygame.display.set_mode((800, 800))
            pygame.display.set_caption('INeC-Test')
            pygame.mixer.init()

    while my_timer == 0:
        print('Intertrial')

    if __name__ == "__main__":
        game = Game()












