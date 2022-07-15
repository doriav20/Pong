from pygame import *

VELOCITY = 10

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3


class PlayerBar:
    def __init__(self, screen, left_or_right):
        super(PlayerBar, self).__init__()
        self.__container = screen
        self.__width = 20
        self.__height = 110
        self.__pos = screen.get_size()[1] // 2
        self.__v = VELOCITY
        self.__side = left_or_right
        self.__lock = False

    def reset(self):
        self.__pos = self.__container.get_size()[1] // 2

    def draw(self):
        screen_width, screen_height = self.__container.get_size()
        if self.__side == LEFT:
            left = 10
        else:
            left = screen_width - 10 - self.__width
        top = self.__pos - self.__height // 2
        draw.rect(self.__container, (51, 204, 255), Rect((left, top), (self.__width, self.__height)))

    def set_velocity(self, v):
        self.__v = v

    def move(self, up_or_down):
        if self.__lock:
            return
        if up_or_down == DOWN:
            self.__pos = min(self.__container.get_size()[1] - self.__height // 2 - 10, self.__pos + self.__v)
        else:
            self.__pos = max(10 + self.__height // 2, self.__pos - self.__v)

    def get_height(self):
        return self.__height

    def get_position(self):
        return self.__pos

    def get_velocity(self):
        return self.__v
    
    def lock(self):
        self.__lock = True
        
    def unlock(self):
        self.__lock = False
