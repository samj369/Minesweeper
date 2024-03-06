def initialise_board():
    board = ["O" for _ in range(25)]  # list of 25 Os, 5 rows of 5
    return board

def insert_mines(board, positions):
    for position in positions:
        row, column = position   # could use 5 * row + col but was saying out of bounds ??
        board_index = 5 * row + column
        board[board_index] = "X" # insert X where the mines are located in the original board


def display_board(board):
    board_copy = board[:]
    for row in range(5):
        for column in range(5):
            cell = board[row * 5 + column]
            if cell == "X":
                board_copy[row * 5 + column] = "O" # in the corresponding square of the cpy board display O not X
            else:
                adjacent_mines = count_adjacent_mines(board, row, column)
                if adjacent_mines == 0:
                    board_copy[row * 5 + column] = "O" #for squares with no adjacent mine leave as 0
                else:
                    board[row * 5 + column] = str(adjacent_mines) # display how many adjacent mines to that square
    print(board[0:5])
    print(board[5:10])
    print(board[10:15])
    print(board[15:20])
    print(board[20:25])
    print()
    print(board_copy[0:5])
    print(board_copy[5:10])
    print(board_copy[10:15])
    print(board_copy[15:20])
    print(board_copy[20:25])


def count_adjacent_mines(board, row, column):
    count = 0
    for row, column in [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]: # check above, below, left and right for each square
        if 0 <= row < 5 and 0 <= column < 5 and board[row * 5 + column] == "X": # check if within bounds of the 5x5 board and a mine is detected
            count += 1
    return count

def play_turn(board, row, column):
    board_copy = board[:]
    mine_selected = False
    if board[row * 5 + column] == "X":      # if cell contains a mine in initial board
        board_copy[row * 5 + column] = "#" # update board copy
        mine_selected = True
        #print ("True")
    else:
        adjacent_mines = count_adjacent_mines(board, row, column)
        if adjacent_mines == 0:      # if cell is O in initial board
            board_copy[row * 5 + column] = " "  # update cell in copy board to blank space
        else:
            board_copy[row * 5 + column] = str(adjacent_mines) # cell must be adjacent to a mine, so display how many mines
    return mine_selected

def check_win(board)
    board_copy = board[:]
    if cell == "O":
        return False
    return True
print(check_win(board))                 #does NOT WORJ BOTH THE FUNCTIONS DONT WORK an di im tired

#???
positions = [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]]
board = initialise_board()
insert_mines(board, positions)
play_turn(board,2,2)
display_board(board)

















