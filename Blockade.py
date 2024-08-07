import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
DARK_BLUE = (30, 30, 60)
LIGHT_BLUE = (100, 100, 200)
GRAY = (169, 169, 169)

# Screen dimensions
DIS_WIDTH = 800
DIS_HEIGHT = 600
BORDER_WIDTH = 20

# Set up the display
DIS = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Enhanced Snake Game')

# Define the clock
CLOCK = pygame.time.Clock()
SNAKE_BLOCK = 20
SNAKE_SPEED = 10

# Define the font style
FONT_STYLE = pygame.font.SysFont("bahnschrift", 25)
SCORE_FONT = pygame.font.SysFont("comicsansms", 35)

def draw_snake(snake_block, snake_list):
    """Draws the snake on the screen using colors."""
    for x in snake_list:
        pygame.draw.rect(DIS, RED, [x[0], x[1], snake_block, snake_block])
        pygame.draw.rect(DIS, RED, [x[0]+2, x[1]+2, snake_block-4, snake_block-4])

def display_score(score):
    """Displays the current score on the screen."""
    value = SCORE_FONT.render("Your Score: " + str(score), True, YELLOW)
    DIS.blit(value, [10, 10])

def display_message(msg, color, position):
    """Displays a message on the screen."""
    mesg = FONT_STYLE.render(msg, True, color)
    DIS.blit(mesg, position)

def draw_border():
    """Draws the border around the game area."""
    pygame.draw.rect(DIS, GRAY, [0, 0, DIS_WIDTH, BORDER_WIDTH])
    pygame.draw.rect(DIS, GRAY, [0, 0, BORDER_WIDTH, DIS_HEIGHT])
    pygame.draw.rect(DIS, GRAY, [0, DIS_HEIGHT - BORDER_WIDTH, DIS_WIDTH, BORDER_WIDTH])
    pygame.draw.rect(DIS, GRAY, [DIS_WIDTH - BORDER_WIDTH, 0, BORDER_WIDTH, DIS_HEIGHT])

def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(BORDER_WIDTH, DIS_WIDTH - BORDER_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
    foody = round(random.randrange(BORDER_WIDTH, DIS_HEIGHT - BORDER_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0

    while not game_over:

        while game_close:
            DIS.fill(BLACK)
            display_message("You Lost! Press Q-Quit or C-Play Again", RED, [DIS_WIDTH / 6, DIS_HEIGHT / 3])
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= DIS_WIDTH - BORDER_WIDTH or x1 < BORDER_WIDTH or y1 >= DIS_HEIGHT - BORDER_WIDTH or y1 < BORDER_WIDTH:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        DIS.fill(BLACK)
        draw_border()
        pygame.draw.rect(DIS, GREEN, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(BORDER_WIDTH, DIS_WIDTH - BORDER_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
            foody = round(random.randrange(BORDER_WIDTH, DIS_HEIGHT - BORDER_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0
            length_of_snake += 1

        CLOCK.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Start the game
if __name__ == "__main__":
    game_loop()
