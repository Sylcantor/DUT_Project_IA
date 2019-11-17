import random
import itertools
import numpy as np

RESULT_X_WINS = 1
RESULT_O_WINS = -1
RESULT_DRAW = 0
RESULT_NOT_OVER = 2


def play_game(x_strategy, o_strategy, game):
    board = game
    player_strategies = itertools.cycle([x_strategy, o_strategy])

    while not board.is_gameover():
        board.print_board()
        play = next(player_strategies)
        board = play(board)

    return board


def play_games(total_games, x_strategy, o_strategy, game, play_single_game=play_game):
    results = {
        RESULT_X_WINS: 0,
        RESULT_O_WINS: 0,
        RESULT_DRAW: 0
    }

    for g in range(total_games):
        end_of_game = (play_single_game(x_strategy, o_strategy, game))
        result = end_of_game.get_game_result()
        results[result] += 1

    x_wins_percent = results[RESULT_X_WINS] / total_games * 100
    o_wins_percent = results[RESULT_O_WINS] / total_games * 100
    draw_percent = results[RESULT_DRAW] / total_games * 100

    print(f"x wins: {x_wins_percent:.2f}%")
    print(f"o wins: {o_wins_percent:.2f}%")
    print(f"draw  : {draw_percent:.2f}%")


def play_random_move(board):
    move = board.get_random_valid_move_index()
    return board.play_move(move)


def is_even(value):
    return value % 2 == 0


def is_empty(values):
    return values is None or len(values) == 0
