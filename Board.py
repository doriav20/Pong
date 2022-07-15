from pygame import *
from Ball import Ball
from MidLines import MidLines
from Scoreboard import Scoreboard
from Player_Bar import PlayerBar

BG_COLOR = (64, 64, 64)
BALL_RADIUS = 10
BORDER_SPACE = 20
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

keep_ball_until_leave_screen_flag = False


class Board:
    def __init__(self, screen):
        self.__screen = screen
        self.__scoreboard = Scoreboard(screen)
        self.__ball = Ball(screen, 500, 340, BALL_RADIUS)
        self.__midlines = MidLines(screen, BORDER_SPACE)
        self.__player1_bar = PlayerBar(screen, LEFT)
        self.__player2_bar = PlayerBar(screen, RIGHT)
        self.__game_paused = True
        self.__pause_mode = 'Start'

    def resume_game(self):
        self.__game_paused = False
        self.__player1_bar.unlock()
        self.__player2_bar.unlock()
        global keep_ball_until_leave_screen_flag
        keep_ball_until_leave_screen_flag = False
        if self.__pause_mode == 'Start':
            self.__scoreboard.reset()

    def pause_game(self):
        self.__game_paused = True
        self.__player1_bar.reset()
        self.__player2_bar.reset()
        self.__player1_bar.lock()
        self.__player2_bar.lock()
        self.__ball.reset()

    def draw_start_text(self):
        font.init()
        myfont = font.SysFont('Sitka Text', 80)
        txt = 'Press Any Key To ' + self.__pause_mode
        text = myfont.render(txt, False, (255, 255, 255))
        if len(self.__pause_mode) > 6:
            self.__screen.blit(text, (150, 295))
        else:
            self.__screen.blit(text, (180, 295))

    def move_player1(self, up_or_down):
        self.__player1_bar.move(up_or_down)

    def move_player2(self, up_or_down):
        self.__player2_bar.move(up_or_down)

    def draw(self):
        self.__screen.fill(BG_COLOR)
        self.__midlines.draw()
        self.__scoreboard.draw()
        self.__ball.draw()
        self.__player1_bar.draw()
        self.__player2_bar.draw()
        if self.__game_paused:
            self.draw_start_text()

    def move_ball(self):
        if self.__game_paused:
            return
        self.__ball.move()

    def get_screen_size(self):
        return self.__screen.get_size()

    def check_ball_direction(self):
        if self.__game_paused:
            return
        curr_x, curr_y = self.__ball.get_position()
        curr_vx, curr_vy = self.__ball.get_velocity()
        width, height = self.get_screen_size()

        p1_y = self.__player1_bar.get_position()
        p2_y = self.__player2_bar.get_position()

        global keep_ball_until_leave_screen_flag
        if keep_ball_until_leave_screen_flag:
            if curr_x + 2 * BALL_RADIUS + 20 < 0 or curr_x - 2 * BALL_RADIUS - 20 > width:
                    if curr_x + 2 * BALL_RADIUS + 20 < 0:
                        self.__scoreboard.point_to_player2()
                    else:
                        self.__scoreboard.point_to_player1()
                    self.check_scoreboard()

        if curr_y - BALL_RADIUS <= 0 or curr_y + BALL_RADIUS >= height:
            self.__ball.set_velocity(curr_vx, -curr_vy)

        if curr_x - BALL_RADIUS < 10 + 20:
            low_bound = p1_y - self.__player1_bar.get_height() // 2
            high_bound = p1_y + self.__player1_bar.get_height() // 2
            if low_bound <= curr_y <= high_bound:
                self.__ball.set_velocity(-curr_vx, curr_vy)
            else:
                keep_ball_until_leave_screen_flag = True

        if curr_x + BALL_RADIUS > width - (10 + 20):
            low_bound = p2_y - self.__player2_bar.get_height() // 2
            high_bound = p2_y + self.__player2_bar.get_height() // 2
            if low_bound <= curr_y <= high_bound:
                self.__ball.set_velocity(-curr_vx, curr_vy)
            else:
                keep_ball_until_leave_screen_flag = True

    def check_scoreboard(self):
        p1_score, p2_score = self.__scoreboard.get_score()
        if max(p1_score, p2_score) == 5:
            self.__pause_mode = 'Start'
        else:
            self.__pause_mode = 'Continue'
        self.pause_game()

    def point_to_player1(self):
        if self.__game_paused:
            return
        self.__scoreboard.point_to_player1()

    def point_to_player2(self):
        if self.__game_paused:
            return
        self.__scoreboard.point_to_player2()

    def is_game_paused(self):
        return self.__game_paused
