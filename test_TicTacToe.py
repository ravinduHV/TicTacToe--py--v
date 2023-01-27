import TicTacToe


def test_board():
    assert TicTacToe.Board([[(2,2),'X'], [(1,3), 'O']]) == """ ._1_._2_._3_.
1|___|___|___|
2|___|_X_|___|
3|_O_|___|___|
"""
    assert TicTacToe.Board([[(2,3),'X'], [(1,1), 'O'] , [(3,1),'X']]) == """ ._1_._2_._3_.
1|_O_|___|_X_|
2|___|___|___|
3|___|_X_|___|
"""

def test_my_side_wins():
    lines = TicTacToe.axis()
    moves1 = [[(2,1),'X'], [(2,2),'O'], [(2,3), "X"], [(1,3),'O'], [(3,2),'X'], [(3,1),'O']]
    assert TicTacToe.Iwins(moves1, 'O', lines) == True
    assert TicTacToe.Iwins(moves1, 'X', lines) == False
    
def test_try_to_win():
    moves1 = [[(1, 1), 'X'], [(2, 2), 'O'], [(1, 2), 'X'], [(1, 3), 'O'], [(3, 1), 'X'], [(2, 1), 'O'], [(2, 3), 'X'], [(3, 3), 'O']]
    moves2 = [[(1, 2), 'X'], [(2, 2), 'O'], [(3, 3), 'X'], [(2, 3), 'O'], [(2, 1), 'X'], [(1, 3), 'O'], [(3, 1), 'X'], [(1, 1), 'O']]
    assert TicTacToe.try_to_win(moves1, 'O', 'X', [(3,2)]) == None
    assert TicTacToe.try_to_win(moves2, 'X', 'O', [(3,2)] ) == [(3,2)]
    assert TicTacToe.try_to_win(moves2, 'O', 'X', [(3,2)] ) == None
    
