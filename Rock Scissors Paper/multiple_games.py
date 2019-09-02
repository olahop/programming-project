"""Multiple games file - arrange multiple RSP games between two players"""
from game import Game

class MultipleGames():
    """Multiple games class - involved players and number of games"""

    player1 = ''
    player2 = ''
    nr_of_games = 0

    def __init__(self, player1, player2, nr_of_games):
        """This is where you set up the game and state the involved players"""
        self.player1 = player1
        self.player2 = player2
        self.nr_of_games = nr_of_games

    def run_games(self):
        """This simulates the game and trigger the printing of result"""
        for times in range(0, self.nr_of_games):
            single_game = Game(self.player1, self.player2)
            single_game.run_game()
            self.__str__()

    def __str__(self):
        """This print out the result to the interface"""
        print("Score:\n" +
              self.player1.get_class_name() +
              " " +
              self.player1 +
              ": " +
              str(self.player1.get_points()) +
              "\n" +
              self.player2.get_class_name() +
              " " +
              self.player2 +
              ": " +
              str(self.player2.get_points()))
