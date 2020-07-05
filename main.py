import pygame
import random

from Scripts.MiniDef import *

pygame.init()
WIDTH = 720
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
BLOCK_LENGTH = 20
PLACE = [[0 for j in range(WIDTH // BLOCK_LENGTH)] for i in range(HEIGHT // BLOCK_LENGTH)]
PLACE[len(PLACE) // 2][len(PLACE[0]) // 2] = 1

SNAKE_STATUS = "stay"

RUN = 0  # 0 is run; 1 is when the escape was pressed;
        # 2 is game over; 3 is code error
while not RUN:
    pygame.time.delay(100)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            RUN = 1

    if maxInArray2(PLACE) == 1 and SNAKE_STATUS == "stay":
        if keys[pygame.K_UP]:
            SNAKE_STATUS = "up"
            PLACE[12][18] = 2
            PLACE[11][18] = 1
        if keys[pygame.K_RIGHT]:
            SNAKE_STATUS = "right"
            PLACE[12][18] = 2
            PLACE[12][19] = 1
        if keys[pygame.K_DOWN]:
            SNAKE_STATUS = "down"
            PLACE[12][18] = 2
            PLACE[13][18] = 1
        if keys[pygame.K_LEFT]:
            SNAKE_STATUS = "left"
            PLACE[12][18] = 2
            PLACE[12][17] = 1

    else:   # if SNAKE_STATUS != "stay":
        i_head, j_head = findXinA2(1, PLACE)
        if i_head == -1 or j_head == -1:
            print("ERROR 3")
            RUN = 3
            break
        if (SNAKE_STATUS == "right" or SNAKE_STATUS == "left") and keys[pygame.K_UP]:
            SNAKE_STATUS = "up"
        elif (SNAKE_STATUS == "up" or SNAKE_STATUS == "down") and keys[pygame.K_RIGHT]:
            SNAKE_STATUS = "right"
        elif (SNAKE_STATUS == "right" or SNAKE_STATUS == "left") and keys[pygame.K_DOWN]:
            SNAKE_STATUS = "down"
        elif (SNAKE_STATUS == "up" or SNAKE_STATUS == "down") and keys[pygame.K_LEFT]:
            SNAKE_STATUS = "left"

        if SNAKE_STATUS == "up":
            if (i_head-1) < 0:
                RUN = 2
                break
            PLACE[i_head-1][j_head] = 1
            i_head -= 1
        elif SNAKE_STATUS == "right":
            if (j_head+1) >= WIDTH//BLOCK_LENGTH:
                RUN = 2
                break
            PLACE[i_head][j_head+1] = 1
            j_head += 1
        elif SNAKE_STATUS == "down":
            if (i_head+1) >= HEIGHT//BLOCK_LENGTH:
                RUN = 2
                break
            PLACE[i_head+1][j_head] = 1
            i_head += 1
        elif SNAKE_STATUS == "left":
            if (j_head-1) < 0:
                RUN = 2
                break
            PLACE[i_head][j_head-1] = 1
            j_head -= 1

        for i in range(HEIGHT//BLOCK_LENGTH):
            for j in range(WIDTH//BLOCK_LENGTH):
                if PLACE[i][j] > 0:
                    PLACE[i][j] += 1
        PLACE[i_head][j_head] = 1
        i_head, j_head = findXinA2(maxInArray2(PLACE), PLACE)
        PLACE[i_head][j_head] = 0

    window.fill((0, 0, 0))
    for i in range(len(PLACE)):
        for j in range(len(PLACE[0])):
            color = (0, 0, 0)
            if PLACE[i][j] > 0:
                color = (0, 255, 0)
            elif PLACE[i][j] == -1:
                color = (255, 0, 0)
            pygame.draw.rect(window, color, (j * BLOCK_LENGTH, i * BLOCK_LENGTH, 50, 50))

    pygame.display.update()
    #printArray(PLACE)

pygame.quit()
