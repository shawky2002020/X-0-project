import random

# Function to check if four characters are equal and not empty
def equal4(x, y, z, a):
    return x == y and y == z and z == a and x != ' '

# Function to check the winner of the game
def check_winner(board):
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
    tie = all(board[i][j] != ' ' for i in range(7) for j in range(7))
    if tie:
        return 0

    # No winner yet
    return 1

# Function to draw the board
def draw_board(board):
    for i in range(7):
        for j in range(7):
            print(f" | {board[i][j]} |", end="")
        print("\n" + "-" * (7 * 6))

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, is_max, alpha, beta, first_time=True):
    final_score = -1000 if is_max else 1000
    final_i, final_j = -1, -1
    result = check_winner(board)

    # Base case: if depth is 0 or there's a winner
    if depth == 0 or result != 1:
        return result

    if is_max:  # Maximizing for 'X'
        final_score = -1000
        for i in range(7):
            for j in range(7):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth - 1, False, alpha, beta, False)
                    board[i][j] = ' '
                    if score > final_score:
                        final_score = score
                        final_i, final_j = i, j
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break  # Beta cut-off
            if beta <= alpha:
                break  # Beta cut-off
    else:  # Minimizing for 'O'
        final_score = 1000
        for i in range(7):
            for j in range(7):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth - 1, True, alpha, beta, False)
                    board[i][j] = ' '
                    if score < final_score:
                        final_score = score
                        final_i, final_j = i, j
                    beta = min(beta, score)
                    if beta <= alpha:
                        break  # Alpha cut-off
            if beta <= alpha:
                break  # Alpha cut-off

    if first_time:
        if final_i != -1 and final_j != -1:
            board[final_i][final_j] = 'X' if is_max else 'O'

    return final_score

def main():
    board = [[' ' for _ in range(7)] for _ in range(7)]
    has_winner = False
    player = 'X'  # Starting player

    while not has_winner:
        # Print whose turn it is
        print(f"Player {player}'s turn.")

        if player == 'X':
            # Take player input
            x, y = map(int, input("Enter row and column (0-6): ").split())
            if 0 <= x < 7 and 0 <= y < 7 and board[x][y] == ' ':
                board[x][y] = player
                draw_board(board)
                result = check_winner(board)
                if result != 1:
                    has_winner = True
                player = 'O'  # Switch to AI
            else:
                print("The field is not empty or invalid coordinates")
        else:
            # AI's turn: Always uses minimax algorithm with Alpha-Beta Pruning
            minimax(board, 4, False, -1000, 1000, True)
            draw_board(board)
            result = check_winner(board)
            if result != 1:
                has_winner = True
            player = 'X'  # Switch to player

    # Print final result
    result = check_winner(board)
    if result == 0:
        print("Tie")
    else:
        print(f"{'X' if result == 2 else 'O'} player wins")

if __name__ == "__main__":
    main()
