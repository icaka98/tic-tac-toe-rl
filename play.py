import random

from rl_player import AIPlayer, encode_board
from simulate import ask_prompt
from utils import CELL_VELUE_PRINT, get_game_state, print_board


def play() -> None:
    board = [0] * 9
    ai_player = AIPlayer("top", epsilon=0.0)
    ai_player.load_policy()

    print_board([CELL_VELUE_PRINT[cell] for cell in board])

    board = [0] * 9
    turn = -1 if random.uniform(0, 1) < 0.5 else 1
    while True:
        if turn == -1:
            x = ask_prompt(board)
            board[x] = turn
        else:
            x = ai_player.pick_action(board, turn)
            board[x] = turn

        turn *= -1
        print_board([CELL_VELUE_PRINT[cell] for cell in board])
        game_outcome = get_game_state(board)

        if game_outcome in (-1, 1):
            print(f"Winner is: {CELL_VELUE_PRINT[game_outcome]}")
            break

        if game_outcome == 2:
            print(f"The game is a tie.")
            break


if __name__ == "__main__":
    play()
