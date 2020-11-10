from core import Player
from yote.yote_rules import YoteRules
import json


class DeusExMachinaInterface(object):
    def __init__(self, state, remain_time):
        self.state = state
        self.remain_time = remain_time

    def get_board(self):
        print(json.loads(self.state.get_json_state())['board'])

    def get_latest_player(self):
        print(self.state.get_latest_player())
        # return state.

    def get_next_player(self):
        print(self.state.get_next_player())
        # return state.

    def get_latest_move(self):
        print(self.state.get_latest_move())
        # return state.

    def get_player_info(self):
        print(self.state.get_player_info(get_latest_player()))
        # return state.

    def get_enemy_info(self):
        print(self.state.get_player_info(get_latest_player()))
        # return state.

    def get_json_state(self):
        print(self.state.get_json_state())
        # return state.


class AI(Player):

    name = "Deus Ex Machina"

    def __init__(self, color):
        super(AI, self).__init__(color)
        self.position = color.value
        self.start_game = False

    def play(self, state, remain_time):
        # print("time remain is ", remain_time, " seconds")
        gameInfos = DeusExMachinaInterface(state, remain_time)
        gameInfos.get_board()
        return YoteRules.random_play(state, self.position)
