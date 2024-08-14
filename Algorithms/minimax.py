import random

# Function to check if four characters are equal and not empty
def equal4(x, y, z, w):
    return x == y == z == w and x != ' '

# Function to check the winner of the game
def checkwinner(board):
    # Check rows for a winner
    for i in range(7):
        for j in range(4):
            if equal4(board[i][j], board[i][j + 1], board[i][j + 2], board[i][j + 3]):
                return 2 if board[i][j] == 'X' else -2

    # Check columns for a winner
    for j in range(7):
        for i in range(4):
            if equal4(board[i][j], board[i + 1][j], board[i + 2][j], board[i + 3][j]):
                return 2 if board[i][j] == 'X' else -2

    # Check main diagonals for a winner
    for i in range(4):
        for j in range(4):
            if equal4(board[i][j], board[i + 1][j + 1], board[i + 2][j + 2], board[i + 3][j + 3]):
                return 2 if board[i][j] == 'X' else -2

    # Check anti-diagonals for a winner
    for i in range(4):
        for j in range(3, 7):
            if equal4(board[i][j], board[i + 1][j - 1], board[i + 2][j - 2], board[i + 3][j - 3]):
                return 2 if board[i][j] == 'X' else -2

    # Check for a tie
    if all(board[i][j] != ' ' for i in range(7) for j in range(7)):
        return 0

    # No winner yet
    return 1

# Function to draw the board
def drawboard(board):
    for i in range(7):
        for j in range(7):
            print(f" | {board[i][j]} |", end='')
        print("\n" + "-" * 7 * 6)

# Minimax function for AI to determine the best move
def minimax(board, depth, is_max, first_time=True):
    final_score = -10 if is_max else 10
    final_i, final_j = -1, -1
    result = checkwinner(board)

    # Base case: if depth is 0 or there's a winner
    if depth == 0 or result != 1:
        return result

    if is_max:  # Maximizing for 'X'
        final_score = -10
        for i in range(7):
            for j in range(7):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth - 1, False, False)
                    board[i][j] = ' '
                    if score > final_score:
                        final_score = score
                        final_i, final_j = i, j
    else:  # Minimizing for 'O'
        final_score = 10
        for i in range(7):
            for j in range(7):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth - 1, True, False)
                    board[i][j] = ' '
                    if score < final_score:
                        final_score = score
                        final_i, final_j = i, j

    if first_time and final_i != -1 and final_j != -1:
        board[final_i][final_j] = 'X' if is_max else 'O'

    return final_score

def main():
    board = [[' ' for _ in range(7)] for _ in range(7)]
    player = 'X'
    has_winner = False

    while not has_winner:
        print(f"Player {player}'s turn.")
        if player == 'X':
            while True:
                try:
                    x, y = map(int, input("Enter row and column numbers (0-6): ").split())
                    if 0 <= x < 7 and 0 <= y < 7 and board[x][y] == ' ':
                        board[x][y] = player
                        break
                    else:
                        print("Invalid move. Please enter valid coordinates and ensure the spot is empty.")
                except ValueError:
                    print("Please enter two numbers separated by a space.")
            drawboard(board)
            result = checkwinner(board)
            if result != 1:
                has_winner = True
            else:
                player = 'O'  # Switch to AI
        else:
            minimax(board, 4, False, True)
            drawboard(board)
            result = checkwinner(board)
            if result != 1:
                has_winner = True
            player = 'X'  # Switch to player

    # Print final result
    result = checkwinner(board)
    if result == 0:
        print("Tie\nResult: 0")
    elif result == 2:
        print("X player wins\nResult: 1")
    elif result == -2:
        print("O player wins\nResult: -1")

if __name__ == "__main__":
    main()
