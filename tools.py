import pygame


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    height = 25
    width = 25
    length = 2
    speed = 5
    status = 'stay'
    head = Point(390, 290)
    tail = Point(415, 315)
    flex_queue = []
