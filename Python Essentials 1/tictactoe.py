from random import randrange


def display_board(board):
    separator = "+-------+-------+-------+"
    empty_line = "|       |       |       |"
    print(separator)
    for row in board:
        print(empty_line)
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print(empty_line)
        print(separator)


def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ('X', 'O'):
                free_fields.append((row, column))
    return free_fields


def enter_move(board):
    free_fields = make_list_of_free_fields(board)
    while True:
        try:
            move = int(input("Enter your move: "))
        except ValueError:
            print("You must enter an integer.")
            continue
        if move < 1 or move > 9:
            print("The number must be between 1 and 9.")
            continue
        row = (move - 1) // 3
        column = (move - 1) % 3
        if (row, column) not in free_fields:
            print("That square is already occupied.")
            continue
        board[row][column] = 'O'
        return


def victory_for(board, sign):
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)):  # row i
            return True
        if all(board[j][i] == sign for j in range(3)):  # column i
            return True
    if all(board[i][i] == sign for i in range(3)):      # main diagonal
        return True
    if all(board[i][2 - i] == sign for i in range(3)):  # secondary diagonal
        return True
    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    row, column = free_fields[randrange(len(free_fields))]
    board[row][column] = 'X'


board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9],
]
display_board(board)

while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("You won!")
        break

    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("The computer won!")
        break
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break