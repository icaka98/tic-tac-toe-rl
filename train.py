import random

from tqdm import tqdm

from rl_player import AIPlayer
from simulate import get_game_state
from utils import encode_board


def train(n_epochs: int = 1_000_000, name: str = "adam") -> None:
    ai_player = AIPlayer(name)
    ai_player_2 = AIPlayer("P2")

    for _ in tqdm(range(n_epochs), desc="Training games:"):
        board = [0] * 9
        ai_player.reset()
        ai_player_2.reset()

        turn = 1 if random.uniform(0, 1) < 0.5 else -1
        while True:
            if turn == 1:
                x = ai_player.pick_action(board, turn)
                board[x] = turn
                ai_player.add_state(encode_board(board))
            else:
                x = ai_player_2.pick_action(board, turn)
                board[x] = turn
                ai_player_2.add_state(encode_board(board))

            turn *= -1
            game_outcome = get_game_state(board)

            if game_outcome in (-1, 1, 2):
                if game_outcome == 1:
                    ai_player.calc_reward(1)
                    ai_player_2.calc_reward(0)
                elif game_outcome == -1:
                    ai_player.calc_reward(0)
                    ai_player_2.calc_reward(1)
                else:
                    ai_player.calc_reward(0.8)
                    ai_player_2.calc_reward(0.8)
                break

    ai_player.save_policy()
    print("The AI player was trained.")


if __name__ == "__main__":
    train(n_epochs=1_000_000, name="adam")
