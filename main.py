import pygame
from random import randint

pygame.init()
# Задаем дисплей
side = 30
w = 17
h = 15
FPS = 5
ball = 0
DISPLAYSURF = pygame.display.set_mode((w * side, h * side))
# Задаем цвета
K_GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 193, 6)

game_running = 0
k = 0
dirs = [pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT, pygame.K_UP]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
snake = [(7, 3), (7, 4)]
direction = 0


def place_apple():
    a = (randint(0, w - 1), randint(0, h - 1))
    while a in snake:
        a = (randint(0, w - 1), randint(0, h - 1))
    return a


def place_apple1():
    a = (randint(0, w - 1), randint(0, h - 1))
    while a in snake:
        a = (randint(0, w - 1), randint(0, h - 1))
    return a


def place_apple2():
    a = (randint(0, w - 1), randint(0, h - 1))
    while a in snake:
        a = (randint(0, w - 1), randint(0, h - 1))
    return a


apple = place_apple()
apple1 = place_apple1()
apple2 = place_apple2()


def check_collisions():
    head = snake[-1]
    for i in range(len(snake) - 1):
        if head == snake[i]:
            return 2
    if head[0] >= w or head[0] < 0:
        return 3
    if head[1] >= h or head[1] < 0:
        return 3
    if head == apple:
        return 1
        ball += 1
    if head == apple1:
        return 1
        ball += 1
    if head == apple2:
        return 1
        ball += 1
    return 0


clock = pygame.time.Clock()
f = pygame.font.SysFont('Avenir Heavy', 50, True)
text = f.render("Game Over", 1, (123, 45, 230))

while True:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            break
        if e.type == pygame.KEYDOWN:
            if game_running == 0:
                game_runnig = 1
            if e.key == pygame.K_SPACE:
                game_running = 0
                snake = [(7, 3), (7, 4)]
                direction = 0
                apple = place_apple()
                apple1 = place_apple1()
                apple2 = place_apple2()
            for i in range(4):
                if e.key == dirs[i] and direction != (i + 2) % 4:
                    direction = i
    if game_running == 2:
        DISPLAYSURF.fill(0)
        DISPLAYSURF.blit(text, (5 * side, 3 * side))
        ball = 0
        pygame.display.update()
        game_running = 3
    if game_running == 3:
        continue
    snake.append((snake[-1][0] + dx[direction], snake[-1][1] + dy[direction]))
    pygame.display.update()
    collis = check_collisions()
    if collis >= 2:
        game_running = 2
        pass
    elif collis == 1:
        apple = place_apple()
        apple1 = place_apple1()
        apple2 = place_apple2()
        ball += 1
        print(ball)
        pass
    elif collis == 0:
        snake.pop(0)
    DISPLAYSURF.fill(K_GREEN)
    for i in range(len(snake)):
        pygame.draw.rect(DISPLAYSURF, RED, pygame.Rect(snake[i][0] * side, snake[i][1] * side, side, side))
    pygame.draw.rect(DISPLAYSURF, YELLOW, pygame.Rect(apple[0] * side, apple[1] * side, side, side))
    pygame.draw.rect(DISPLAYSURF, YELLOW, pygame.Rect(apple1[0] * side, apple1[1] * side, side, side))
    pygame.draw.rect(DISPLAYSURF, YELLOW, pygame.Rect(apple2[0] * side, apple2[1] * side, side, side))
    pygame.display.update()
