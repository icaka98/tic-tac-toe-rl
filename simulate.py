import random
from typing import List

from tqdm import tqdm

from rl_player import AIPlayer
from utils import get_game_state, print_board


def ask_prompt(board: List[int]) -> int:
    print_board([str(x) if board[x] == 0 else " " for x in range(0, 9)])
    return int(input("Please deside on where to play (0-8):"))


def ask_ai_random(board: List[int]) -> int:
    return random.choice([idx for idx in range(9) if board[idx] == 0])


def simulate(n_epochs: int = 10_000) -> None:
    board = [0] * 9
    ai_player = AIPlayer("P1", epsilon=0.0)
    ai_player.load_policy()

    win_random = 0
    win_bot = 0
    draws = 0

    for i in tqdm(range(n_epochs), desc="Simulating games:"):
        board = [0] * 9
        turn = -1 if random.uniform(0, 1) < 0.5 else 1
        while True:
            if turn == -1:
                x = ask_ai_random(board)
                board[x] = turn
            else:
                x = ai_player.pick_action(board, turn)
                board[x] = turn

            turn *= -1
            game_outcome = get_game_state(board)

            if game_outcome in (-1, 1):
                if game_outcome == -1:
                    win_random += 1
                else:
                    win_bot += 1
                break

            if game_outcome == 2:
                draws += 1
                break

    print(f"RL bot wins: {win_bot}")
    print(f"Random bot wins: {win_random}")
    print(f"Draws between bots: {draws}")


if __name__ == "__main__":
    simulate(n_epochs=10_000)
