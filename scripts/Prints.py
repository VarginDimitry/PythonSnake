import pygame

from tools import Point, Snake


def printSnake(snake, window):
    if snake.flex_queue:
        # pygame.draw.rect(window, (255, 255, 255), (snake.head.x, snake.head.y, snake.width, snake.height))
        
        pygame.draw.rect(window, (255, 255, 255),
                         (min(snake.head.x, snake.flex_queue[0].x), min(snake.head.y, snake.flex_queue[0].y),
                          min(abs(snake.head.x - snake.flex_queue[0].x), snake.width), min(abs(snake.head.y - snake.flex_queue[0].y), snake.height)))
        for i in range(len(snake.flex_queue) - 1):
            pygame.draw.rect(window, (255, 255, 255),
                             (min(snake.flex_queue[i].x, snake.flex_queue[i+1].x), min(snake.flex_queue[i].y, snake.flex_queue[i+1].y),
                              min(abs(snake.flex_queue[i].x - snake.flex_queue[i+1].x), snake.width), min(abs(snake.flex_queue[i].y - snake.flex_queue[i+1].y), snake.height)))
        pygame.draw.rect(window, (255, 255, 255),
                         (min(snake.tail.x, snake.flex_queue[-1].x), min(snake.tail.y, snake.flex_queue[-1].y),
                          min(abs(snake.tail.x - snake.flex_queue[-1].x), snake.width), min(abs(snake.tail.y - snake.flex_queue[-1].y), snake.height)))
    else:
        pygame.draw.rect(window, (255, 255, 255),
                         (min(snake.head.x, snake.tail.x), min(snake.head.y, snake.tail.y),
                          min(abs(snake.head.x - snake.tail.x), snake.width), min(abs(snake.head.y - snake.tail.y), snake.height)))
