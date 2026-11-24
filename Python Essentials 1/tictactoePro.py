from random import randrange

USE_COLORS = True  # True in VS Code / a terminal, False in consoles without ANSI support

if USE_COLORS:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    VIOLET = "\033[95m"
    CYAN = "\033[96m"
    GRAY = "\033[90m"
else:
    RESET = BOLD = RED = GREEN = YELLOW = VIOLET = CYAN = GRAY = ""


def title(text, color):
    print(f"\n{color}{BOLD}══════ {text} ══════{RESET}\n")


def colorize(value):
    if value == 'X':
        return f"{BOLD}{VIOLET}X{RESET}"
    if value == 'O':
        return f"{BOLD}{CYAN}O{RESET}"
    return f"{GRAY}{value}{RESET}"


def display_board(board):
    separator = f"{GRAY}+-------+-------+-------+{RESET}"
    bar = f"{GRAY}|{RESET}"
    empty_line = bar + (7 * " " + bar) * 3
    print(separator)
    for row in board:
        print(empty_line)
        cells = [f"   {colorize(value)}   " for value in row]
        print(bar + bar.join(cells) + bar)
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
            move = int(input(f"{CYAN}Pick your square (1-9): {RESET}"))
        except ValueError:
            print(f"{YELLOW}You must enter an integer.{RESET}")
            continue
        if move < 1 or move > 9:
            print(f"{YELLOW}The number must be between 1 and 9.{RESET}")
            continue
        row = (move - 1) // 3
        column = (move - 1) % 3
        if (row, column) not in free_fields:
            print(f"{YELLOW}That square is already occupied.{RESET}")
            continue
        board[row][column] = 'O'
        return


def victory_for(board, sign):
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)):
            return True
        if all(board[j][i] == sign for j in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)):
        return True
    if all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    row, column = free_fields[randrange(len(free_fields))]
    board[row][column] = 'X'
    print(f"{VIOLET}The computer chose square {row * 3 + column + 1}.{RESET}\n")


board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9],
]

name = input(f"{CYAN}What's your name? {RESET}").strip()
if name == "":
    name = "Player"

title("GAME START: the computer opens in the center", VIOLET)
display_board(board)

while True:
    title("YOUR TURN (O)", CYAN)
    enter_move(board)
    print()
    display_board(board)
    if victory_for(board, 'O'):
        print(f"\n{GREEN}{BOLD}You won, {name}!{RESET}")
        break

    title("COMPUTER'S TURN (X)", VIOLET)
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print(f"\n{RED}{BOLD}You lost, {name}. The computer won.{RESET}")
        break
    if not make_list_of_free_fields(board):
        print(f"\n{YELLOW}{BOLD}It's a tie!{RESET}")
        break