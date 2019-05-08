import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
white = (255, 255, 255)
SCREEN_SIZE = (1920, 1080)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Pygame Demo")
background = pygame.image.load("medias/fond_noir.jpg").convert()
bat_1 = pygame.image.load("medias/rectangle.jpeg").convert_alpha()
bat_2 = pygame.image.load("medias/rectangle.jpeg").convert_alpha()
ball = pygame.image.load("medias/balle.png").convert_alpha()
FONT = "medias/Minecraft.ttf"
WHITE = (255, 255, 255)
menu_background = pygame.image.load("medias/theme_menu.jpg").convert()
start_button = pygame.image.load("medias/start.jpg").convert()

ball_x, ball_y = 960, 540
x_2, y_2 = 1755, 540
x_1, y_1 = 110, 540
MOVE_RIGHT = 1
MOVE_LEFT = 2
MOVE_DOWN = 3
MOVE_UP = 4
direction_r = 0
direction_l = 0
points_player1 = 0
points_player2 = 0
x_vec = -5
y_vec = -5
menu = 1

while True:
        while (menu == 1):
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            #if event.type == MOUSEBUTTONDOWN and (pos): #button start   
            screen.blit(menu_background, (0, 0))
            screen.blit(start_button, (960, 540))
            pygame.display.update()
