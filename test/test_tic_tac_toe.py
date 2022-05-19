import unittest
from src.tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):



    def test_detect_win_board(self):
        """
        See if either player has won, given the board
        :param self:
        :return:
        """
        # The prod code will iterate thru all 8 paths and check each one for a win
        #  so to test drive that


    def test_detect_win_false_1(self):
        """
        input is a triplet of cells
        returns true (win) or false (no win)
        """
        board = TicTacToe.initialize_board()
        path = [[0,0],[1,1],[2,2]]
        result = TicTacToe.detect_win(board, path)
        self.assertFalse(result)

    def test_detect_win_true(self):
        board = TicTacToe.initialize_board()
        for i in range(3):
            board[0][i] = "X"
        path=[[0,0],[0,1],[0,2]]
        result = TicTacToe.detect_win(board, path)
        self.assertTrue(result)

    def test_detect_win_false_2(self):
        board = TicTacToe.initialize_board()
        board[1][0]="X"
        board[1][1]="O"
        board[1][2]="X"
        path=[[1,0],[1,1],[1,2]]
        result = TicTacToe.detect_win(board, path)
        self.assertFalse(result)




