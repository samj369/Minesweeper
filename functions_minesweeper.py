def initialise_board():
    board = ["O"] * 25  # list of 25 Os, 5 rows of 5
    return board
board = initialise_board()

def display_board(board):
    board_copy = board[:]
    for row in range(5):
        for column in range(5):
            cell = board[row * 5 + column]
            if cell == "X":
                board_copy[row * 5 + column] = "O" # in the corresponding square of the cpy board display O not X
    print()
    print(board_copy[0:5])
    print(board_copy[5:10])
    print(board_copy[10:15])
    print(board_copy[15:20])
    print(board_copy[20:25])

def count_adjacent_mines(board, row, column):
    count = 0
    # check above, below, left, right and the 4 diagonals of cell for mines
    for row, column in [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1),
                        (row - 1, column - 1), (row - 1, column + 1), (row + 1, column + 1), (row + 1, column - 1)]:

        if 0 <= row < 5 and 0 <= column < 5 and board[row * 5 + column] == "X": # check if within bounds of the 5x5 board and a mine is detected
            count += 1
    return count

def insert_mines(board, positions):
    for position in positions:
        row, column = position   # could use 5 * row + col but was saying out of bounds ??
        board_index = 5 * row + column
        board[board_index] = "X" # insert X where the mines are located in the original board

def play_turn(board, row, column):
    if board[row * 5 + column] == "X":
        board[row * 5 + column] = "#"  # reveal hidden mine to #
        return board, True
    else:
        adjacent_mines = count_adjacent_mines(board, row, column)
        if adjacent_mines == 0:
            board[row * 5 + column] = " "  # reveal space for 01blank cell

        else:
            board[row * 5 + column] = str(adjacent_mines)  # reveal number of adjacent mines
        return board, False

def check_win(board):
    for cell in board:
        if cell == "O":
            return False
    return True
display_board(board)

def play_game(positions):
    board = initialise_board()
    insert_mines(board, positions)


    game_over = False
    while not game_over:
        try:
            user_input = input("Enter row and column (0-4) eg 2 3: ")
            row, column = map(int, user_input.split())
            if not (0 <= row < 5 and 0 <= column < 5):
                print("Invalid input,try again")
                continue
            board, hit_mine = play_turn(board, row, column)
            display_board(board)
            if hit_mine:
                print("BOOM! Game Over!")
                game_over = True
            elif check_win(board):
                print("YOU WIN!")
                game_over = True
        except ValueError:
            print("Invalid input, try again")







