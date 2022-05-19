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


    def test_detect_win(self):
        """
        input is a triplet of cells
        output is true (win) or false (no win)
        :param self:
        :return:
        """
        input = ((0,0),(1,1),(2,2))
        result = TicTacToe.detect_win(input)
        self.assertFalse(result)

