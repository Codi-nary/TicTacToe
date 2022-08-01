# tic tac toe board

user = True
spots_filled = 0


def board():
    board = []
    for i in range(3):
        board.append(['_' for _ in range(3)])
    return board


def print_board(board):
    for row in board:
        for slot in row:
            print(slot + ' ', end="")
        print()


def quit(user_input):
    if user_input.lower() == 'q':
        print("Thanks for playing")
        return True
    else:
        return False


def valid_input(user_input):
    if not user_input.isnumeric():
        print("This is not a valid input")
        return False
    elif int(user_input) > 9 or int(user_input) < 1:
        print("This is not a valid input")
        return False
    else:
        return True


def coordinate(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2:
        col = int(col % 3)

    return row, col


def is_taken(cord, board):
    row = cord[0]
    col = cord[1]
    if board[row][col] != '_':
        print("Sorry! this spot is taken.")
        return True
    else:
        return False


def add_to_board(cord, board, active_user):
    row = cord[0]
    col = cord[1]
    board[row][col] = active_user


def current_user(user):
    if user:
        return 'X'
    else:
        return 'O'


def row_winner(board, user):
    row_winner = True
    for row in board:
        for spot in row:
            if spot != user:
                row_winner = False
                break
        if row_winner: return True
    return False


def col_winner(board, user):
    col_winner = True
    for col in range(3):
        for row in range(3):
            if board[row][col] != user:
                col_winner = False
                break
        if col_winner: return True
    return False


def diagonal_winner(board, user):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False


def is_winner(board, user):
    if row_winner(board, user): return True
    if col_winner(board, user): return True
    if diagonal_winner(board, user): return True
    return False


board = board()
while spots_filled < 9:
    active_user = current_user(user)
    print_board(board)
    user_input = input("Please select a number 1 to 9 or enter \"q\" to Quit ")
    if quit(user_input): break
    if not valid_input(user_input):
        print("Please Try Again")
        continue
    user_input = int(user_input) - 1
    cord = coordinate(user_input)
    if is_taken(cord, board):
        print("Please try again")
        continue
    add_to_board(cord, board, active_user)

    if is_winner(board,active_user):
        print_board(board)
        print(f"{active_user.upper()} won!")
        break

    spots_filled += 1
    if spots_filled == 9:
        print_board(board)
        print("Tie!")
    user = not user
