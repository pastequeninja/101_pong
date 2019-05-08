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

while True:
    while (points_player1 < 5 and points_player2 < 5):
        if ball_x <= 0:
            ball_x = 960
            ball_y = 540
            points_player2 += 1
        if ball_x >= 1920 - 70:
            ball_x = 960
            ball_y = 540
            points_player1 += 1
        if ball_y == 0:
            y_vec = -y_vec
            ball_y += 5
        if ball_y >= 1018:
            y_vec = -y_vec
            ball_y -= 5
        if ball_x == 155 and ball_y >= y_1 - 34 / 2 and ball_y <= y_1 + 410 - 34 / 2:
            x_vec = -x_vec
            ball_x += 5
        if ball_x == 1700 and ball_y >= y_2 - 34 / 2 and ball_y <= y_2 + 410 - 34 / 2:
            x_vec = -x_vec
            ball_x -= 5
        if ball_y > 0 and ball_y < 1018:
            ball_x += x_vec
            ball_y += y_vec
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_z:
                    direction_l = MOVE_LEFT
                if event.key == K_UP:
                    direction_r = MOVE_UP
                if event.key == K_DOWN:
                    direction_r = MOVE_DOWN
                if event.key == K_s:
                    direction_l = MOVE_RIGHT
            elif event.type == KEYUP:
                if event.key == K_z:
                    direction_l = 0
                if event.key == K_DOWN:
                    direction_r = 0
                if event.key == K_UP:
                    direction_r = 0
                if event.key == K_s:
                    direction_l = 0
        if(direction_l == MOVE_LEFT and y_1 > 0):
            y_1-=5
        if(direction_l == MOVE_RIGHT and y_1 < 1080 - 410):
            y_1+=5
        if(direction_r == MOVE_UP and y_2 > 0):
            y_2-=5
        if(direction_r == MOVE_DOWN and y_2 < 1080 - 410):
            y_2+=5
        screen.blit(background, (0, 0))
        screen.blit(bat_1, (x_1, y_1))
        screen.blit(bat_2, (x_2, y_2))
        screen.blit(ball, (ball_x, ball_y))
        pygame.display.update()
    for event in pygame.event.get():
        if (points_player1 == 5):
            screen.blit(background, (0, 0))
            pygame.display.update()
            font = pygame.font.Font(FONT, 17)
            surface_text = font.render("PLAYER 1 WINS !!!", True, WHITE)
            text_rect = screen.get_rect()
            text_rect.midtop = (1800, 500)
            if event.type == QUIT:
                exit()
            screen.blit(surface_text, text_rect)
            pygame.display.flip()
        else:
            screen.blit(background, (0, 0))
            pygame.display.update()
            font = pygame.font.Font(FONT, 17)
            surface_text = font.render("PLAYER 2 WINS !!!", True, WHITE)
            text_rect = screen.get_rect()
            text_rect.midtop = (1800, 500)
            if event.type == QUIT:
                exit()
            screen.blit(surface_text, text_rect)
            pygame.display.flip()
