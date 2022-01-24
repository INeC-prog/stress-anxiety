import pygame
pygame.init()
import time
global my_timer
from pygame.locals import *
import random
import threading

SIZE = 40

def countdown():
    global my_timer
    my_timer = 2

    for x in range(2):
        my_timer = my_timer - 1
        time.sleep(1)
        print('Time On')

        for i in range(15, 0, -1):
            print(i)
            time.sleep(2)

    print("TEST IS NOT OVER YET")
    print('\033[0;35mPAUSE\033[m')


countdown_thread = threading.Thread(target= countdown)
countdown_thread.start()

while my_timer > 0:

    class Predator:
        def __init__(self, parent_screen, count):
            self.parent_screen = parent_screen
            self.block = pygame.image.load("Resources/circlered.jpg").convert()
            self.x = 100
            self.y = 100
            self.direction = 'down'

            self.count = count
            self.x = SIZE * count
            self.y = SIZE * count

        def increase_count(self):
            count = 0
            self.count += 1

        def walk(self):
            if self.direction == 'left':
                self.x -= 20
            if self.direction == 'right':
                self.x += 20
            if self.direction == 'up':
                self.y -= 20
            if self.direction == 'down':
                self.y += 20
            self.draw()

        def move_left(self):
            self.direction = 'left'

        def move_right(self):
            self.direction = 'right'

        def move_up(self):
            self.direction = 'up'

        def move_down(self):
            self.direction = 'down'

        def draw(self):
            for i in range(self.count):
                self.parent_screen.blit(self.block, (self.x, self.y))
            pygame.display.flip()

        def move(self):
            self.x = random.randint(0, 20) * SIZE
            self.y = random.randint(0, 20) * SIZE

    class Prey:
        def __init__(self, parent_screen, escape):
            self.parent_screen = parent_screen
            self.block = pygame.image.load("Resources/blue square.jpg").convert()
            self.x = 200
            self.y = 200
            self.direction = 'up'

            self.escape = escape
            self.x = SIZE * escape
            self.y = SIZE * escape

        escape = 0
        def increase_escape(self):
            self.escape += 1

        def walk(self):
            if self.direction == 'left':
                self.x -= 20
            if self.direction == 'right':
                self.x += 20
            if self.direction == 'up':
                self.y -= 20
            if self.direction == 'down':
                self.y += 20
            self.draw()

        def move_left(self):
            self.direction = 'left'

        def move_right(self):
            self.direction = 'right'

        def move_up(self):
            self.direction = 'up'

        def move_down(self):
            self.direction = 'down'

        def draw(self):
            self.parent_screen.fill((154, 154, 5))
            self.parent_screen.blit(self.block, (self.x, self.y))

        def move(self):
            self.x = random.randint(0, 20) * SIZE
            self.y = random.randint(0, 20) * SIZE


    class Game:
        def __init__(self):
            pygame.init()
            self.surface = pygame.display.set_mode((800, 800))
            pygame.display.set_caption('INeC-Test')
            self.predator = Predator(self.surface, 2)
            self.predator.walk()
            self.predator.draw()
            self.prey = Prey(self.surface, 2)
            self.prey.walk()
            self.prey.draw()
            pygame.display.flip()

        def reset(self):
            self.predator = Predator(self.surface, 2)
            self.prey = Prey(self.surface, 2)

        def is_collision(self, x1, y1, x2, y2):
            if x1 >= x2 and x1 <= x2 + SIZE:
                if y1 >= y2 and y1 <= y2 + SIZE:
                    return True
            return False

        def play(self):
            self.predator.walk()
            self.predator.draw()
            self.prey.walk()
            self.prey.draw()
            self.display_score()
            self.show_test_over()
            pygame.display.flip()

            if self.is_collision(self.predator.x, self.predator.y, self.prey.x, self.prey.y):
                sound = pygame.mixer.Sound("Resources/High fear.mp3")
                pygame.mixer.Sound.play(sound)
                self.predator.increase_count()
                self.prey.move()

            if not (0 <= self.predator.x <= 800 and 0 <= self.predator.y <= 800):
                self.predator.move()

            if not (0 <= self.prey.x <= 800 and 0 <= self.prey.y <= 800):
                sound = pygame.mixer.Sound("Resources/Escape.mp3")
                pygame.mixer.Sound.play(sound)
                self.prey.increase_escape()
                self.prey.move()

            for i in range(18, self.predator.count):
                if self.is_collision(self.predator.x[i], self.predator.y[i], self.predator.x, self.predator.y):
                    raise Exception("TEST_OK")

        def display_score(self):
            font = pygame.font.SysFont('arial', 20)
            line1 = font.render(f"Grid-hits:  escape {self.prey.escape-2}", True, (255, 255, 255))
            self.surface.blit(line1, (10, 20))
            line2 = font.render(f"Test: score {self.predator.count-2}", True, (255, 255, 255))
            self.surface.blit(line2, (640, 20))

        def show_test_over(self):
            font = pygame.font.SysFont('arial', 20)
            line1 = font.render(f"Test is not over yet! Score {self.predator.count-2}", True, (255, 255, 255))
            self.surface.blit(line1, (10, 720))
            line2 = font.render(f"Press Escape to exit", True, (255, 255, 255))
            self.surface.blit(line2, (610, 720))
            pygame.display.flip()

        def run(self):
            running = True
            pause = False

            while running:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                        if event.key == K_RETURN:
                             pause = False

                        if not pause:
                            if event.key == K_w:
                                self.predator.move_up()
                            elif event.key == K_a:
                                self.predator.move_left()
                            elif event.key == K_d:
                                self.predator.move_right()
                            elif event.key == K_s:
                                self.predator.move_down()

                            if event.key == K_LEFT:
                                self.prey.move_left()
                            if event.key == K_RIGHT:
                                self.prey.move_right()
                            if event.key == K_UP:
                                self.prey.move_up()
                            if event.key == K_DOWN:
                                self.prey.move_down()
                        elif event.type == QUIT:
                            running = False
                try:
                    if not pause:
                        self.play()
                    time.sleep(0.03)

                except Exception as e:
                    self.show_test_over()
                    pause = True
                    self.reset()

                with open('data_A100.txt', 'w') as f:
                    f.write(f"{self.predator.count=}"'\n')
                    f.write(f"{self.prey.escape=}")

    while my_timer == 0:
        exit()
    print("START")


    if __name__ == "__main__":
        game = Game()
        game.run()







