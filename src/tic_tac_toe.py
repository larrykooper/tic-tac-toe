from typing import List

class TicTacToe:

    @staticmethod
    def detect_win(board: List, path: List) -> bool:
        cell = []
        for i in range(3):
            cell.append(board[path[i][0]][path[i][1]])
        if cell[0] != "" and (cell[0] == cell[1] == cell[2]):
            return True
        else:
            return False

    @staticmethod
    def initialize_board():
        board = [[""] * 3 for i in range(3)]
        return board