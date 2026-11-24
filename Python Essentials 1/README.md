# Tic-Tac-Toe in Python

Final project for **Python Essentials 1** (Cisco Networking Academy).

A console program that lets the user play tic-tac-toe against the computer. The computer plays `X`, the user plays `O`, and the computer's moves are chosen at random (no artificial intelligence).

---

## Problem Statement

Write a program that simulates a game of tic-tac-toe between the user and the computer, under the following simplified rules:

1. The computer plays `X` and the user plays `O`.
2. The computer makes the first move: it always places its first `X` in the center of the board.
3. The squares are numbered 1 to 9, row by row, left to right and top to bottom.
4. The user enters a move by typing the number of the chosen square. The input must be valid:
   - it must be an integer,
   - it must be between 1 and 9 (inclusive),
   - it must not point to a square that is already occupied.
5. After every move, the program checks the state of the game. The possible outcomes are:
   - the game continues,
   - the game ends in a tie,
   - the user wins,
   - the computer wins.
6. The computer responds with its own move and the check is repeated.
7. No form of artificial intelligence is implemented: the computer picks a random square among the free ones.

### Square numbering

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

---

## Technical Requirements

### Board representation

The board is stored as a list of three elements, where each element is itself a list of three elements (the rows). Every square can be accessed with:

```python
board[row][column]
```

Each square holds `'X'`, `'O'`, or the square's number (in which case it is considered free).

Initial board (with the computer's first move already made):

```python
board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9],
]
```

### Board appearance in the console

```
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
```

### Functions to implement

| Function | Description |
|---|---|
| `display_board(board)` | Takes the current state of the board and prints it to the console. |
| `enter_move(board)` | Takes the current board, asks the user for their move, validates the input, and updates the board with the user's choice. |
| `make_list_of_free_fields(board)` | Scans the board and returns a list of all free squares. Each element is a `(row, column)` tuple. |
| `victory_for(board, sign)` | Analyzes the board to determine whether the player using `'O'` or `'X'` (according to `sign`) has won the game. |
| `draw_move(board)` | Picks the computer's move at random among the free squares and updates the board. |

### Random number generation

The random choice is made with the `randrange()` function from the `random` module:

```python
from random import randrange
```

---

## Program Flow

1. The initial board is displayed, with the computer's `X` in the center.
2. The user enters a move (`O`) and the board is updated.
3. The program checks whether the user has won. If so, the game ends.
4. The computer makes its move (`X`) and the board is updated.
5. The program checks whether the computer has won or the game is a tie. If neither, go back to step 2.

---

## Example Session

```
Enter your move: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
```

The game continues this way until one of the players completes a line (row, column, or diagonal) or the board is full.

---

## How to Run

Requires Python 3.

```bash
python tictactoe.py
```

## Extras in This Implementation

- Console colors using ANSI escape codes (`X` in violet, `O` in cyan, win message in green, loss message in red).
- A `USE_COLORS` switch to turn colors off in consoles that don't support them (for example, the course platform's built-in console).
- Headers that clearly separate the user's turn from the computer's turn, and a notice of which square the computer chose.