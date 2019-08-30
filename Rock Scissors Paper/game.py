
# single RSP game
class Game():


    # involved players
    player1 = ''
    player2 = ''


    # This is where you set up the game and state the involved players
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    # This simulates the game and trigger the printing of result
    def run_game(self):
        player1_action = self.player1.action(self.player2)
        player2_action = self.player2.action(self.player1)
        result = self.winner(player1_action, player2_action)
        if(self.player1.get_class_name == ("Historian" or "Most Common")):
            self.player1.save_result(self.player2, player2_action)
        elif(self.player2.get_class_name == ("Historian" or "Most Common")):
            self.player2.save_result(self.player1, player1_action)
        self.__str__(player1_action, player2_action, result)
        
    # This is where the winner is decided
    def winner(self, player1_action, player2_action):
        if(player1_action == player2_action):
            self.player1.add_points(0.5)
            self.player2.add_points(0.5)
            return "No one"
        if(player1_action == "rock"):
            if(player2_action == "scissors"):
                self.player1.add_points(1)
                return self.player1
            else:
                self.player2.add_points(1)
                return self.player2
        elif(player1_action == "scissors"):
            if(player2_action == "paper"):
                self.player1.add_points(1)
                return self.player1
            else:
                self.player2.add_points(1)
                return self.player2
        elif(player1_action == "paper"):
            if(player2_action == "rock"):
                self.player1.add_points(1)
                return self.player1
            else:
                self.player2.add_points(1)
                return self.player2


    # This print out the result to the interface
    def __str__(self, player1_action, player2_action, result):
        print(self.player1.get_class_name() + " " + self.player1 + ": " + player1_action + ".  " +
            self.player2.get_class_name() + " " + self.player2 + ": " + player2_action + " -> " +
            result + " wins!")