from typing import List

class TicTacToe:

    @staticmethod
    def detect_path_win(board: List, path: List) -> bool:
        """
        :param board: Tic tac toe board (2d matrix of letters)
        :param path: triplet of cells
        :return: True if a win on path detected
        """
        cell = []
        for i in range(3):
            cell.append(board[path[i][0]][path[i][1]])
        if cell[0] != "" and (cell[0] == cell[1] == cell[2]):
            return True
        else:
            return False

    @staticmethod
    def detect_board_win(board: List) -> bool:
        # See if either player has won, given the board
        # To make it faster I will use a helper method count(board, letter)
        #   if both counts are <3 there can be no winner
        # Otherwise iterate thru all 8 paths and check each one for a win
        if TicTacToe.count(board, "X") < 3 and TicTacToe.count(board, "O") < 3:
            return False

    @staticmethod
    def initialize_board():
        board = [[""] * 3 for i in range(3)]
        return board

    @staticmethod
    def count(board, letter) -> int:
        """
        :param board:
        :param letter:
        :return: count of letter in board
        """
        count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == letter:
                    count+= 1
        return count
