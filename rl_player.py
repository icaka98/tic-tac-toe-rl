import json
import random
from typing import List

from utils import encode_board


class AIPlayer:
    def __init__(self, name: str, epsilon: float = 0.3) -> None:
        self.name = name
        self.epsilon = epsilon
        self.states = []
        self.lr = 0.2
        self.decay = 0.9
        self.states_values = {}

    def pick_action(self, board: List[int], token: int) -> int:
        available_actions = [x for x in range(9) if board[x] == 0]

        if random.uniform(0, 1) <= self.epsilon:
            return random.choice(available_actions)

        mx = -1
        best_action = None

        for action in available_actions:
            interim_board = board.copy()
            interim_board[action] = token
            board_encoding = encode_board(interim_board)

            value = self.states_values.get(board_encoding, 0)

            if value >= mx:
                mx = value
                best_action = action

        return best_action

    def calc_reward(self, reward: float) -> None:
        for state in reversed(self.states):
            if not self.states_values.get(state):
                self.states_values[state] = 0

            self.states_values[state] += self.lr * (
                self.decay * reward - self.states_values[state]
            )
            reward = self.states_values[state]

    def add_state(self, state: str) -> None:
        self.states.append(state)

    def reset(self) -> None:
        self.states = []

    def reverse_states(self) -> None:
        new_states_values = {}
        for k, v in self.states_values.items():
            arr = list(map(int, k.split(",")))
            arr = [x * -1 for x in arr]
            new_states_values[encode_board(arr)] = v

        self.states_values = new_states_values

    def save_policy(self) -> None:
        with open(f"best_policy_{self.name}.json", "w") as output_file:
            json.dump(self.states_values, output_file)

    def load_policy(self) -> None:
        with open(f"best_policy_{self.name}.json", "r") as input_file:
            self.states_values = json.load(input_file)
