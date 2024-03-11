import pytest
from functions_minesweeper import *
def test_count_adjacent_mines_in_corner():
    board = ['X','O','O','O','O'
             'O','O','O','O','O',
             'O','O','O','O','O',
             'O','O','O','O','O',
             'O','O','O','O','O',]

count = count_adjacent_mines(board,0,4)
assert(count == 0)

def test_insert_mines():
    board = ["O"] * 25
    positions = [(0,0),(1,1),(2,2),(3,2),(0,4)]
    insert_mines(board,positions)
    assert board == ['X','O','O','O','X',
                     'O','X','O','O','O',
                     'O','O','X','O','O',
                     'O','O','X','O','O',
                     'O','O','O','O','O',
                     ]
