import pygame
from pygame.locals import *

pygame.init()



screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('CatMouseToe')

#define vrb
line_width = 6
markers= []
clicked = False
pos = []
player = 1
game_over = False

#define colours
green = (130, 89,108)
red = (255, 0, 0)
pink =(237, 133,124)

#font
font = pygame.font.SysFont(None, 40)

#play again
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 150, 50)

def draw_grid():
    bg =(130, 89,108)
    grid = (50,50,50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen,grid, (10, x * 200), (screen_width, x * 200), line_width)
        pygame.draw.line(screen,grid, (x * 200, 10), (x * 200, screen_height), line_width)

for x in range(3):
    row = [0] * 3
    markers.append(row)

pisic = pygame.image.load('caty.png')
soricel = pygame.image.load('mouse.png')

def draw_pisic(x ,y ):
    screen.blit(pisic,(x,y))


def draw_soricel(x ,y ):
    screen.blit(soricel,(x,y))


def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                draw_pisic(x_pos*200+42,y_pos*200+42)
            if y == -1:
                draw_soricel(x_pos*200+42,y_pos*200+42)
            y_pos += 1
        x_pos += 1

def check_winner():
    global winner
    global game_over

    y_pos = 0
    for x in markers:

        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True

        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1

    if (markers[0][0] + markers [1][1] + markers[2][2]) == 3 or (markers[2][0] + markers[1][1] + markers[0][2]) == 3:
            winner = 1
            game_over = True
    if (markers[0][0] + markers [1][1] + markers[2][2]) == -3 or (markers[2][0] + markers[1][1] + markers[0][2]) == -3:
            winner = 2
            game_over = True


def draw_winner(winner):
    win_text = 'Player' + str(winner) + " Yey,wins!"
    win_img = font.render(win_text, True, pink)
    pygame.draw.rect(screen, green, (screen_width // 2 - 110, screen_height // 2- 60, 250, 50))
    screen.blit(win_img, (screen_width// 2 - 110, screen_height // 2 - 50))

    again_text = 'Play Again?'
    again_img = font.render(again_text, True, pink)
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (screen_width // 2 - 100, screen_height // 2 + 10))

run = True
while run:
    draw_grid()
    draw_markers()
    #add event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 200][cell_y // 200] == 0:
                    markers[cell_x // 200][cell_y // 200] = player
                    player *= -1
                    check_winner()
    if game_over == True:
        draw_winner(winner)
        #mouseclik again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                if again_rect.collidepoint(pos):
                    #reset vrb
                    markers= []
                    clicked = False
                    pos = []
                    player = 1
                    winner = 0
                    game_over = False
                    for x in range(3):
                        row = [0] * 3
                        markers.append(row)

    pygame.display.update()

pygame.quit()



