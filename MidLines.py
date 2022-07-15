from pygame import *


class MidLines:
    def __init__(self, screen, border_space):
        self.__container = screen
        self.__border_space = border_space

    def draw(self):
        screen_width, screen_height = self.__container.get_size()
        width = 16
        height = 40
        left = screen_width // 2 - width//2

        top = self.__border_space
        while top <= screen_height - self.__border_space-height:
            draw.rect(self.__container, (51, 204, 255), Rect((left, top), (width, height)))
            top += 60
