from core import Player
from yote.yote_rules import YoteRules


class AI(Player):

    name = "Ai 1"

    def __init__(self, color):
        super(AI, self).__init__(color)
        self.position = color.value

    def play(self, state, remain_time):
        print("time remain is ", remain_time, " seconds")
        return YoteRules.random_play(state, self.position)
