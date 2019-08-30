"""Class historian player"""
from player import Player


class HistorianPlayer(Player):
    """Class random player innherets from abstract class player"""

    # previously saved results and grade of memory
    opponents_statistics = {}
    memory = None

    def __init__(self, memory):
        self.memory = memory

    def get_class_name(self):
        return "Historian"

    def action(self, opponent):
        decision = {
            "rock" : 0,
            "scissors" : 0,
            "paper" : 0
        }
        opponent_record = self.opponent_statistics[opponent]
        record_length = len(opponent_record)
        memory_lane = opponent_record[(record_length-self.memory):record_length]
        for x in range(self.memory, (record_length-self.memory)):
            if(opponent_record[(x-self.memory):x] == memory_lane):
                decision[opponent_record[x+1]] += 1
        if (decision["rock"] >= decision["scissors"]) and (
                    decision["rock"] >=decision["paper"]):
            return "paper"
        if (decision["scissors"] >= decision["rock"]) and (
                    decision["scissors"] >= decision["paper"]):
            return "rock"
        return "scissors"

    def save_result(self, opponent, opponent_action):
        self.opponents_statistics[opponent].append(opponent_action)

    def add_points(self, value):
        self.points += value