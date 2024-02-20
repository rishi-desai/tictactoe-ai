import unittest
import engine

class TestEngine(unittest.TestCase):

    def test_new_board(self):
        board = engine.new_board()
        assert len(board) == engine.HEIGHT
        assert len(board[0]) == engine.WIDTH
        for row in board:
            for cell in row:
                assert cell == None

    def test_make_move(self):
        board = [[None, None, None], 
                 [None, None, None], 
                 [None, None, None]]
        coord = (1, 1)
        player = "X"
        engine.make_move(board, coord, player)
        assert board[coord[0]][coord[1]] == player

    def test_is_valid_move(self):
        board = [["X", "O", None], [None, "X", "O"], ["O", None, "X"]]
        assert engine.is_valid_move(board, (0, 2)) == True
        assert engine.is_valid_move(board, (1, 1)) == False
        assert engine.is_valid_move(board, (2, 0)) == False

    def test_get_winner(self):
        board = [["X", "O", None], 
                 [None, "X", "O"], 
                 ["O", None, "X"]]
        assert engine.get_winner(board) == "X"
        board = [["X", "O", None], 
                 [None, "O", "X"], 
                 [None, "O", "X"]]
        assert engine.get_winner(board) == "O"
        board = [["X", "O", None], 
                 [None, "X", "O"], 
                 ["O", None, "O"]]
        assert engine.get_winner(board) == None

    def test_get_winner_with_tie(self):
        board = [["X", "O", "X"], 
                 ["X", "O", "O"], 
                 ["O", "X", "X"]]
        assert engine.get_winner(board) == "Tie"

if __name__ == '__main__':
    unittest.main()