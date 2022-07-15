from pygame import *
from Board import Board

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 680
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
REFRESH_RATE = 60

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

init()
screen = display.set_mode(SIZE)
display.set_caption("Pong")
display.set_mode(SIZE)
clock = time.Clock()
board = Board(screen)
board.draw()
display.flip()

finish = False

while not finish:
    for e in event.get():
        if e.type == QUIT:
            finish = True
        elif board.is_game_paused() and e.type == KEYDOWN:
            board.resume_game()
    keys = key.get_pressed()
    if keys[K_w]:
        board.move_player1(UP)
    if keys[K_s]:
        board.move_player1(DOWN)
    if keys[K_UP]:
        board.move_player2(UP)
    if keys[K_DOWN]:
        board.move_player2(DOWN)

    board.move_ball()
    board.check_ball_direction()
    board.draw()

    display.flip()
    clock.tick(REFRESH_RATE)
