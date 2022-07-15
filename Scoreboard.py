from pygame import *


class Scoreboard:
    def __init__(self, screen):
        self.__container = screen
        self.__score1 = 0
        self.__score2 = 0

    def draw(self):
        font.init()
        myfont = font.SysFont('Sitka Text', 80)
        surface1 = myfont.render(str(self.__score1), False, (51, 204, 255))
        surface2 = myfont.render(str(self.__score2), False, (51, 204, 255))
        self.__container.blit(surface1, (430, 10))
        self.__container.blit(surface2, (540, 10))

    def reset(self):
        self.__score1 = 0
        self.__score2 = 0

    def set_score(self, score1, score2):
        self.__score1 = score1
        self.__score2 = score2

    def get_score(self):
        return self.__score1, self.__score2

    def point_to_player1(self):
        self.__score1 += 1

    def point_to_player2(self):
        self.__score2 += 1
