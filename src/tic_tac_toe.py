from typing import List

class TicTacToe:

    @staticmethod
    def detect_win(board: List, path: List) -> bool:
        cell = []
        for index, j, k in path:
           cell.append(board[path[index][0][path[index[1]]]])
        if cell[0] != "" and (cell[0] == cell[1] == cell[2]):
            return True
        else:
            return False

