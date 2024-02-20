from game import Game
from player import Player
from player_logics import LogicAlwaysDefectBelieveTruth, LogicAlwaysCooperateBelieveTruth

player1 = Player(LogicAlwaysCooperateBelieveTruth)
player2 = Player(LogicAlwaysDefectBelieveTruth)

game = Game(player1, player2, 200)
print(game.get_players())
game.play_game()
print(game.get_game_result())
print(player1.score)
print(player2.score)