def initialise_board():
    board = [["O" for _ in range(5)] for _ in range(5)]  # list of 25 Os, 5 rows of 5
    return board

def insert_mines(board, positions):
    for position in positions:
        row, column = position   # could use 5 * row + col but was saying out of bounds ??
        board[row][column] = "X" # insert X where the mines are located in the original board

board = initialise_board()
positions = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
insert_mines(board, positions)

for row in board:
    print(row)
print() # space to 2 separate 2 board whill testing

board_copy = board[:]   # board shown to player


def display_board(board):
    for row in range(5):
        for column in range(5):
            square = board[row][column]
            if square == "X":
                board_copy[row][column] = "O" # in the corresponding square of the cpy board display O not X
            else:
                adjacent_mines = count_adjacent_mines(board, row, column)
                if adjacent_mines == 0:
                    board_copy[row][column] = "O" #for squares with no adjacent mine leave as 0
                else:
                    board_copy[row][column] = str(adjacent_mines) # display how many adjacent mines to that square
        #print()


def count_adjacent_mines(board, row, column):
    count = 0
    for row, column in [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]: # check above, below, left and right for each square
        if 0 <= row < 5 and 0 <= column < 5 and board[row][column] == "X": # check if within bounds of the 5x5 board and a mine is detected
            count += 1
    return count


#???
board = initialise_board()
insert_mines(board, positions)
display_board(board)
for row in board_copy:
    print(row)          #print the copy board















