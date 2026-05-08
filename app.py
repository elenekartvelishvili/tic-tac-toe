import math

board = [" " for _ in range(9)]

wins = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

# ---------------- PRINT BOARD ----------------
def print_board():
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

# ---------------- CHECK WIN ----------------
def check_winner(board):
    for a, b1, c in wins:
        if board[a] == board[b1] == board[c] != " ":
            return board[a]
    return None

# ---------------- DRAW ----------------
def is_draw():
    return " " not in board and check_winner(board) is None

# ---------------- MINIMAX ----------------
def minimax(is_max):

    winner = check_winner(board)

    if winner == "X":
        return 10
    if winner == "O":
        return -10
    if is_draw():
        return 0

    if is_max:  # AI (X)
        best = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)

        return best

    else:  # Human (O)
        best = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)

        return best

# ---------------- BEST MOVE ----------------
def best_move():

    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "X"

# ---------------- GAME LOOP ----------------
while True:

    best_move()
    print("AI move:")
    print_board()

    if check_winner(board) == "X":
        print("AI wins")
        break

    if is_draw():
        print("Draw")
        break

    move = int(input("Your move (0-8): "))
    if board[move] != " ":
        print("Invalid move")
        continue

    board[move] = "O"
    print_board()

    if check_winner(board) == "O":
        print("You win")
        break
