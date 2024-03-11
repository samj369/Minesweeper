def initialise_board():
    """
    Initialise the empty Minesweeper board with 25 empty cells.

    Returns:
        board (list): a list with 25 cells representing the board
        The cells are set to 'O' to represent empty cells.
    Notes:
        (precondition 1) list is of length 25.
        (precondition 2) each item in list must be the string O.
    """
    board = ["O"] * 25  # list of 25 Os
    return board
board = initialise_board()

def display_board(board):
    """
    Create a copy board to modify and display the list as a 5x5 board
    showing O, spaces and number of adjacent mines and replace hidden mines 'X' with 'O'.

    Arguments:
        board (list): a list with 25 cells representing the board
    Notes:
        (postcondition 1) creates a copy of the initial board
        (postcondition 2) modifies the copy board by replacing 'X' with 'O'
        (postcondition 3) list is displayed as 5 x 5 grid
    """
    # create a board copy to modify
    board_copy = board[:]
    for row in range(5):
        for column in range(5):
            # iterate through initial board to check for mines
            cell = board[row * 5 + column]
            if cell == "X":
                # in the corresponding square of the copy board display 'O' not 'X'
                board_copy[row * 5 + column] = "O"
    print()
    print(board_copy[0:5])
    print(board_copy[5:10])
    print(board_copy[10:15])
    print(board_copy[15:20])
    print(board_copy[20:25])

def count_adjacent_mines(board, row, column):
    """
    Count the number of adjacent mines for each cell in the board.

    Arguments:
        board(list): a list with 25 cells representing the board.
        row(int): the row index of the cell being checked.
        column(int): the column index of the cell being checked.
    Returns:
        count(int): the number of adjacent mines.
    Notes:
        (precondition 1) hidden mines are represented as 'X' in initial board.
        (postcondition 1) checks every cell around the specified cell, including diagonals.
    """
    count = 0
    # check above, below, left, right and the 4 diagonals of each cell for mines
    for row, column in [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1),
                        (row - 1, column - 1), (row - 1, column + 1), (row + 1, column + 1), (row + 1, column - 1)]:
        # check if within bounds of board and mine found
        if 0 <= row < 5 and 0 <= column < 5 and board[row * 5 + column] == "X":
            count += 1
    return count

def insert_mines(board, positions):
    """
    Insert mines at a given position in the board.

    Arguments:
        board(list): a list with 25 cells representing the board.
        positions(list of lists): a list of positions (row,col) specifying where to insert mines.
    Returns:
        board(list): the updated board with mines inserted.
    Notes:
        (precondition 1) mine positions are given as row, col.
        (postcondition 1) checks every cell
    """
    for position in positions:
        row, column = position
        board_index = 5 * row + column
        # insert 'X' where mines are located in the original board
        board[board_index] = "X"

def play_turn(board, row, column):
    """
    Plays a turn and replaces the 'O's with either ' ', '#' or how many adjacent mines
    as the player selects cells.

    Arguments:
        board(list): a list with 25 cells representing the board.
        row(int): the row index of the cell that is selected.
        column(int): the column index of the cell that is selected.
    Returns:
        board(list): the updated board with cells revealed
        (bool): True if mine selected, False otherwise
    Notes:
        (precondition 1): mine positions are given as row, col
        (postcondition 1): if selected cell is 'X' it is replaced with '#' and returns True
        (postcondition 2) if selected cell is 'O' it is replaced with '', returns False
        (postcondition 3) if selected cell has adjacent mines, update with number of adjacent mines
    """
    if board[row * 5 + column] == "X":
        # reveal hidden mine
        board[row * 5 + column] = "#"
        return board, True
    else:
        adjacent_mines = count_adjacent_mines(board, row, column)
        # reveal blank space
        if adjacent_mines == 0:
            board[row * 5 + column] = " "

        else:
            # reveal number of adjacent mines
            board[row * 5 + column] = str(adjacent_mines)  # reveal number of adjacent mines
        return board, False

def check_win(board):
    """
    Checks if the game is over.

    Arguments:
        board(list): a list with 25 cells representing the board.
    Returns:
        (bool): True if the game is won, False otherwise.
    Notes:
        (postcondition 1): check if every "0" cell in board is selected, returns True ie game is won
    """
    for cell in board:
        if cell == "O":
            return False
    return True
display_board(board)

def play_game(positions):
    """
    Plays the game and prompts user to give valid inputs.

    Arguments:
        positions(list of lists): a list of lists representing the positions of the mines.
    Notes:
        (precondition 1): mines are inserted at specified positions
        (precondition 2): user input is valid
        (postcondition 1): games continues until player hits a mine or reveals all cells without mines.
    """
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










