"""Class random player"""
from random import choice
from player import Player


class RandomPlayer(Player):
    """Class random player inherits from abstract class player"""

    def get_class_name(self):
        return "Random"

    def action(self, opponent):
        return choice(['rock', 'scissors', 'paper'])

    def save_result(self, opponent, opponent_action):
        pass

    def add_points(self, value):
        self.points += value
