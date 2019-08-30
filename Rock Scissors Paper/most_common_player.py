"""Class most common player"""
from random import choice
from player import Player


class MostCommonPlayer(Player):
    """Class most common player inherits from abstract class player"""

    opponents_statistics = {}

    def get_class_name(self):
        return "Most Common"

    def action(self, opponent):
        if not self.opponents_statistics[opponent]:
            return choice(['rock', 'scissors', 'paper'])
        decision = {
            "rock": 0,
            "scissors": 0,
            "paper": 0
        }
        for previous_action in self.opponents_statistics[opponent]:
            decision[previous_action] += 1
        if (decision["rock"] >= decision["scissors"]) and (
                decision["rock"] >= decision["paper"]):
            return "paper"
        if (decision["scissors"] >= decision["rock"]) and (
                decision["scissors"] >= decision["paper"]):
            return "rock"
        return "scissors"

    def save_result(self, opponent, opponent_action):
        self.opponents_statistics[opponent].append(opponent_action)

    def add_points(self, value):
        self.points += value
