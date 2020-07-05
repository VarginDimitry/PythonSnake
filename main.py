import pygame
import random

pygame.init()

from tools import *
from scripts.Prints import *
from scripts.coordinates import *

window = pygame.display.set_mode((810, 610))
pygame.display.set_caption("Snake")
snake = Snake


RUN = 0  # 0 is run; 1 is when some button was pressed; 2 is game over
while RUN == 0:
    # цикл будет выполняться раз в Х милисекунд (1/1000 сек)
    pygame.time.delay(30)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            RUN = 1

    if ((snake.status == "stay" or snake.status == "up" or
         snake.status == "down") and keys[pygame.K_LEFT]):
        snake.status = "left"
        snake.flex_queue.append(snake.head)
    if ((snake.status == "stay" or snake.status == "up" or
         snake.status == "down") and keys[pygame.K_RIGHT]):
        snake.status = "right"
        snake.flex_queue.append(snake.head)
    if ((snake.status == "stay" or snake.status == "left" or
         snake.status == "right") and keys[pygame.K_UP]):
        snake.status = "up"
        snake.flex_queue.append(snake.head)
    if ((snake.status == "stay" or snake.status == "left" or
         snake.status == "right") and keys[pygame.K_DOWN]):
        snake.status = "down"
        snake.flex_queue.append(snake.head)

    if snake.status == "left":
        snake.head.x -= snake.speed
        if snake.head.x <= 5:
            RUN = 2
    if snake.status == "right":
        snake.head.x += snake.speed
        if snake.head.x >= 780:
            RUN = 2
    if snake.status == "up":
        snake.head.y -= snake.speed
        if snake.head.y <= 5:
            RUN = 2
    if snake.status == "down":
        snake.head.y += snake.speed
        if snake.head.y >= 580:
            RUN = 2

    if snake.flex_queue:
        if coordinatesEquality(snake.tail, snake.flex_queue[0]):
            snake.flex_queue.pop(0)
        else:
            if (snake.tail.x - snake.flex_queue[0].x) == 0:
                if (snake.tail.y - snake.flex_queue[0].y) > 0:
                    snake.tail.y -= snake.speed
                else:
                    snake.tail.y += snake.speed
            else:
                if (snake.tail.x - snake.flex_queue[0].x) > 0:
                    snake.tail.x -= snake.speed
                else:
                    snake.tail.x += snake.speed

    window.fill((0, 0, 0))
    printSnake(snake, window)

    pygame.display.update()

pygame.quit()
