from typing import List

CELL_VELUE_PRINT = {-1: "O", 0: " ", 1: "X"}

NEW_LINE_DEL_STRING = "---+---+---"


def print_board(board: List[str]) -> None:
    print("*" * 11)
    print(" " + " | ".join(board[0:3]) + " ")
    print(NEW_LINE_DEL_STRING)
    print(" " + " | ".join(board[3:6]) + " ")
    print(NEW_LINE_DEL_STRING)
    print(" " + " | ".join(board[6:9]) + " ")
    print("*" * 11)


def encode_board(board: List[int]) -> str:
    return ",".join(list(map(str, board)))


def _check_rows(board: List[int]) -> int:
    for i in range(3):
        if len(set(board[i * 3 : i * 3 + 3])) == 1:
            return board[i * 3]

    return 0


def _check_cols(board: List[int]) -> int:
    for i in range(3):
        if len(set([board[i], board[i + 3], board[i + 6]])) == 1:
            return board[i]

    return 0


def _check_diag(board: List[int]) -> int:
    if len(set([board[0], board[4], board[8]])) == 1:
        return board[0]

    if len(set([board[2], board[4], board[6]])) == 1:
        return board[2]

    return 0


def get_game_state(board: List[int]) -> int:
    winner_rows = _check_rows(board)
    winner_cols = _check_cols(board)
    winner_diag = _check_diag(board)

    for winner_id in (-1, 1):
        if winner_id in (winner_rows, winner_cols, winner_diag):
            return winner_id

    if all(x != 0 for x in board):
        return 2

    return 0
