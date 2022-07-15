from pygame import *

HORIZONTAL_VELOCITY = 10
VERTICAL_VELOCITY = 10


class Ball:
    def __init__(self, screen, x, y, ball_radius):
        super(Ball, self).__init__()
        self.__container = screen
        self.__pos_x = x
        self.__pos_y = y
        self.__vx = -HORIZONTAL_VELOCITY
        self.__vy = VERTICAL_VELOCITY
        self.__radius = ball_radius

    def reset(self):
        self.__pos_x = 500
        self.__pos_y = 340

    def draw(self):
        draw.circle(self.__container, (51, 204, 255), [self.__pos_x, self.__pos_y], self.__radius)

    def ball_hit(self):
        self.set_velocity(-self.__vx, -self.__vy)

    def set_velocity(self, vx, vy):
        self.__vx = vx
        self.__vy = vy

    def move(self):
        self.__pos_x += self.__vx
        self.__pos_y += self.__vy

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def get_velocity(self):
        return self.__vx, self.__vy
