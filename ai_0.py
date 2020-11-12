from core import Player
from yote.yote_rules import YoteRules
from core import Color
from yote.yote_action import YoteActionType, YoteAction
import json
import numpy as np

class DeusExMachinaInterface(object):
    def __init__(self, state, remain_time, position):
        self.state = state
        self.remain_time = remain_time
        self.position = position

    def get_board(self):
        return json.loads(self.state.get_json_state())['board']

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
        print(self.state.get_player_info(self.position))
        # return state.

    def get_enemy_info(self):
        print(self.state.get_player_info( -1 * self.position ))
        # return state.

    def get_json_state(self):
        return [tuple(cell) for cell in np.argwhere(self.get_board())]
        # print(self.state.get_json_state())
        # return state.

    def add_piece(self, to):
        print(self.remain_time)
        # return state.

    def move_piece(self, moveFrom, to):
        print(self.remain_time)
        # return state.


    def steal_from_board(self, at):
        print(self.remain_time)
        # return state.


    def steal_from_hand(self):
        print(self.remain_time)
        # return state.


class AI(Player):

    name = "Deus Ex Machina"

    def __init__(self, color):
        super(AI, self).__init__(color)
        self.position = color.value
        self.start_game = False

    def play(self, state, remain_time):
        gameInfos = DeusExMachinaInterface(state, remain_time, self.position)
        # gameInfos.get_board()
        
        print(gameInfos.get_json_state())
        return YoteRules.random_play(state, self.position)
