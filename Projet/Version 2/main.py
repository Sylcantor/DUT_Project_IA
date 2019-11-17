from api.minimax import create_minimax_player
from api.prepare import play_games
from api.prepare import play_random_move
from games.TicTacToe.TicTacToe import TicTacToe


# from tictac.mcts import (play_game_and_reset_playouts,
#                          play_mcts_move_with_live_playouts)

play_minimax_move_randomized = create_minimax_player(True)
play_minimax_move_not_randomized = create_minimax_player(False)

game = TicTacToe()

print("Playing random vs random:")
print("-------------------------")
play_games(1000, play_random_move, play_random_move, game)
print("")

print("Playing minimax not random vs minimax random:")
print("---------------------------------------------")
play_games(1000, play_minimax_move_not_randomized,
           play_minimax_move_randomized, game)

# print("Playing random vs random:")
# print("-------------------------")
# play_games(1000, play_random_move, play_random_move)
# print("")

# print("Playing minimax not random vs minimax random:")
# print("---------------------------------------------")
# play_games(1000, play_minimax_move_not_randomized,
#            play_minimax_move_randomized)
# print("")
# print("Playing minimax random vs minimax not random:")
# print("---------------------------------------------")
# play_games(1000, play_minimax_move_randomized,
#            play_minimax_move_not_randomized)
# print("")
# print("Playing minimax not random vs minimax not random:")
# print("-------------------------------------------------")
# play_games(1000, play_minimax_move_not_randomized,
#            play_minimax_move_not_randomized)
# print("")
# print("Playing minimax random vs minimax random:")
# print("-----------------------------------------")
# play_games(1000, play_minimax_move_randomized, play_minimax_move_randomized)
# print("")

# print("Playing minimax random vs random:")
# print("---------------------------------")
# play_games(1000, play_minimax_move_randomized, play_random_move)
# print("")
# print("Playing random vs minimax random:")
# print("---------------------------------")
# play_games(1000, play_random_move, play_minimax_move_randomized)
# print("")
