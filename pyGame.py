import pygame, sys
from pygame.locals import *

BLUE = (108, 226, 240)
RED = (244, 128, 66)
GREEN = (116, 255, 51)
HEIGTH = 1000
WIDTH = 1800
DISPLAY = pygame.display.set_mode((WIDTH, HEIGTH))
class Player:
    def __init__(self):
        self.circle_radius = 50
        self.wheel_distance = 100 + 2*self.circle_radius
        self.wheel1_x = self.circle_radius
        self.wheel1_y = int(HEIGTH - HEIGTH/5)-self.circle_radius
        self.wheel2_x = self.circle_radius + self.wheel_distance
        self.wheel2_y = int(HEIGTH - HEIGTH/5)-self.circle_radius

    def initialPosition(self):
        pygame.draw.circle(DISPLAY, RED, (self.wheel1_x, self.wheel1_y), self.circle_radius)
        pygame.draw.circle(DISPLAY, RED, (self.wheel2_x, self.wheel2_y), self.circle_radius)

    def movement(self):
        keypressed = pygame.key.get_pressed()
        if keypressed[K_LEFT] and self.wheel1_x - 1 >= self.circle_radius:
            self.wheel1_x = self.wheel1_x - 2
            self.wheel2_x = self.wheel2_x - 2
            pygame.draw.circle(DISPLAY, RED, (self.wheel1_x, self.wheel1_y), self.circle_radius)
            pygame.draw.circle(DISPLAY, RED, (self.wheel2_x, self.wheel2_y), self.circle_radius)

        if keypressed[K_RIGHT] and self.wheel2_x + 1 <= self.WIDTH - self.circle_radius:
            self.wheel1_x = self.wheel1_x + 2
            self.wheel2_x = self.wheel2_x + 2
            pygame.draw.circle(DISPLAY, RED, (self.wheel1_x, self.wheel1_y), self.circle_radius)
            pygame.draw.circle(DISPLAY, RED, (self.wheel2_x, self.wheel2_y), self.circle_radius)


class Board:

    def create(self):
        pygame.draw.rect(DISPLAY, GREEN, (0,HEIGTH - HEIGTH/5, WIDTH, HEIGTH/5))
        pygame.draw.rect(DISPLAY, BLUE, (0,0, WIDTH,4*HEIGTH/5),0)


    def refresh(self):
        pygame.draw.rect(DISPLAY, BLUE, (0,0, WIDTH,4*HEIGTH/5))

class GAME():

    def main_loop(self):
        pygame.init()
        player = Player()
        board = Board()
        board.create()
        player.initialPosition()
        while True:
            board.refresh()
            player.movement()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()


if __name__ == '__main__':
    x = GAME()
    x.main_loop()