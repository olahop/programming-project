
from multiple_games import *
from serial_player import *
from random_player import *
from most_common_player import *
from historian_player import *

player1 = SerialPlayer("Kari")
player2 = RandomPlayer("Ola")
player3 = MostCommonPlayer("Per")
player4 = HistorianPlayer("Lars", 2)

battle1 = MultipleGames(player1, player2, 10)
battle2 = MultipleGames(player1, player3, 10)
battle3 = MultipleGames(player1, player4, 20)

#battle1.run_games()
#battle2.run_games()
#battle3.run_games()