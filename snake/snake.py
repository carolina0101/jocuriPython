import pygame
import random

TITLE = 'Catch the cat food'
WIDTH = 600
HEIGHT = 600
BLOCK_SIZE = 20
DELAY_TIME = 100
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'
FONT_FAMILY = 'Consolas'
FONT_SIZE = 25
SCORE_STEP = 10
RIGHT_SIDEBAR_WIDTH = 200

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (255, 166, 32)
BLUE = (0, 0, 200)
GRAY=(150,145,142)
BACKGROUND_COLOR = GRAY
BODY_COLOR = GREEN
HEAD_COLOR = BLUE
APPLE_COLOR = RED
FONT_COLOR = BLACK
BORDER_COLOR = BLACK
whiskuImage = pygame.image.load('e:\Licenta_Python\\LicentaPython\\snake\\cat.png')
crantanici = pygame.image.load('e:\Licenta_Python\\LicentaPython\\snake\\crantanele.png')

pygame.init()
screen = pygame.display.set_mode((WIDTH + RIGHT_SIDEBAR_WIDTH, HEIGHT))
pygame.font.init()
font = pygame.font.SysFont(FONT_FAMILY, FONT_SIZE)



snake = [
    {'x': WIDTH // 2, 'y': HEIGHT // 2},
    {'x': WIDTH // 2 - BLOCK_SIZE, 'y': HEIGHT // 2},
    {'x': WIDTH // 2 - 2 * BLOCK_SIZE, 'y': HEIGHT // 2},
    {'x': WIDTH // 2 - 3 * BLOCK_SIZE, 'y': HEIGHT // 2},
    {'x': WIDTH // 2 - 4 * BLOCK_SIZE, 'y': HEIGHT // 2}
]
direction = RIGHT
apple = {'x': 0, 'y': 0}
score = 0
old_tail = {'x': 0, 'y': 0}


def init_game():
    pygame.display.set_caption(TITLE)
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()



def draw_block1(block, color):
    pygame.draw.rect(
        screen,
        color,
        (
            block['x'],
            block['y'],
            BLOCK_SIZE,
            BLOCK_SIZE
        )
    )
    pygame.display.update()

def draw_whiskey_head(block ):
    screen.blit(whiskuImage,(block['x'],block['y']))
    pygame.display.flip()

def draw_crantanele(block ):
    screen.blit(crantanici,(block['x'],block['y']))
    pygame.display.flip()

def draw_snake():
    for i in snake:
        draw_whiskey_head(i)
    draw_whiskey_head(snake[0])
    pygame.display.update()


def move():
    old_tail = snake[len(snake) - 1]

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = dict(snake[i - 1])
    if direction == UP:
        snake[0]['y'] -= BLOCK_SIZE
    elif direction == DOWN:
        snake[0]['y'] += BLOCK_SIZE
    elif direction == LEFT:
        snake[0]['x'] -= BLOCK_SIZE
    elif direction == RIGHT:
        snake[0]['x'] += BLOCK_SIZE

    draw_block1(old_tail,GRAY)
    draw_whiskey_head(snake[1])
    draw_whiskey_head(snake[0])
    pygame.display.update()


def is_bite_itself():
    for i in range(1, len(snake)):
        if snake[0] == snake[i]:
            return True
    return False


def is_hit_wall():
    return (
        snake[0]['x'] == -BLOCK_SIZE or
        snake[0]['y'] == -BLOCK_SIZE or
        snake[0]['x'] == WIDTH or
        snake[0]['y'] == HEIGHT
    )


def generate_apple():
    x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
    y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
    apple['x'] = x * BLOCK_SIZE
    apple['y'] = y * BLOCK_SIZE
    draw_crantanele(apple )
    pygame.display.update()


def is_ate_apple():
    for i in snake:
        if i == apple:
            return True
    return False


def grow_up():
    snake.append(old_tail)


def display_score():
    pygame.draw.rect(
        screen,
        BACKGROUND_COLOR,
        (
            WIDTH,
            0,
            RIGHT_SIDEBAR_WIDTH,
            HEIGHT
        )
    )
    # Draw a divider between snakeboard and menu
    pygame.draw.rect(
        screen,
        BORDER_COLOR,
        (
            WIDTH,
            0,
            1,
            HEIGHT
        )
    )
    screen.blit(
        font.render(
            f'Score: {score}',
            True,
            FONT_COLOR
        ),
        (WIDTH + 10, 10)
    )
    pygame.display.update()


init_game()
draw_snake()
generate_apple()
display_score()

running = True
moved = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and moved:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT
            moved = False

    move()
    moved = True

    if is_bite_itself() or is_hit_wall():
        running = False
    elif is_ate_apple():
        score += SCORE_STEP
        display_score()
        generate_apple()
        grow_up()

    pygame.time.wait(DELAY_TIME)

pygame.quit()
