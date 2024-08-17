import time
import random

# Function to check if the four characters are equal and not empty
def equal4(x, y, z, a):
    return x == y and y == z and z == a and x != ' '
# Function to check the winner of the game
def check_winner(board):
    # Check rows
    for i in range(7):
        for j in range(4):
            if equal4(board[i][j], board[i][j + 1], board[i][j + 2], board[i][j + 3]):
                return 2 if board[i][j] == 'X' else -2
    # Check columns
    for j in range(7):
        for i in range(4):
            if equal4(board[i][j], board[i + 1][j], board[i + 2][j], board[i + 3][j]):
                return 2 if board[i][j] == 'X' else -2
    # Check main diagonals
    for i in range(4):
        for j in range(4):
            if equal4(board[i][j], board[i + 1][j + 1], board[i + 2][j + 2], board[i + 3][j + 3]):
                return 2 if board[i][j] == 'X' else -2
    # Check anti-diagonals
    for i in range(4):
        for j in range(3, 7):
            if equal4(board[i][j], board[i + 1][j - 1], board[i + 2][j - 2], board[i + 3][j - 3]):
                return 2 if board[i][j] == 'X' else -2
    # Check for a tie
    tie = all(board[i][j] != ' ' for i in range(7) for j in range(7))
    if tie:
        return 0
    return 1

# Function to draw the board
def draw_board(board):
    for i in range(7):
        for j in range(7):
            print(f" | {board[i][j]} |", end="")
        print("\n" + "-" * (7 * 6))
def evaluate_board(board):
    score = 0
    # Check rows for potential wins or losses
    for i in range(7):
        for j in range(4):
            line = [board[i][j], board[i][j + 1], board[i][j + 2], board[i][j + 3]]
            score += evaluate_line(line)
    # Check columns for potential wins or losses
    for j in range(7):
        for i in range(4):
            line = [board[i][j], board[i + 1][j], board[i + 2][j], board[i + 3][j]]
            score += evaluate_line(line)
    # Check diagonals for potential wins or losses
    for i in range(4):
        for j in range(4):
            line = [board[i][j], board[i + 1][j + 1], board[i + 2][j + 2], board[i + 3][j + 3]]
            score += evaluate_line(line)
    for i in range(4):
        for j in range(3, 7):
            line = [board[i][j], board[i + 1][j - 1], board[i + 2][j - 2], board[i + 3][j - 3]]
            score += evaluate_line(line)
    return score

def evaluate_line(line):
    score = 0
    if line.count('X') == 4:  
        score += 100
    elif line.count('X') == 3 and line.count(' ') == 1:  
        score += 10
    elif line.count('X') == 2 and line.count(' ') == 2:  
        score += 5
    elif line.count('O') == 4:
        score -= 100
    elif line.count('O') == 3 and line.count(' ') == 1: 
        score -= 10
    elif line.count('O') == 2 and line.count(' ') == 2: 
        score -= 5
    return score

def minimax(board, depth, is_max, alpha, beta):
    final_score = -1000 if is_max else 1000
    final_i, final_j = -1, -1
    result = check_winner(board)
    if depth == 0 or result != 1:
        if result != 1:
            return result, final_i, final_j 
        else:
            return evaluate_board(board), final_i, final_j  
    if is_max: 
        final_score = -1000
        for i in range(7):
            for j in range(7):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score, _, _ = minimax(board, depth - 1, False, alpha, beta)
                    board[i][j] = ' '
                    if score > final_score:
                        final_score = score
                        final_i, final_j = i, j
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break  
            if beta <= alpha:
                break 
    else: 
        final_score = 1000
        for i in range(7):
            for j in range(7):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score, _, _ = minimax(board, depth - 1, True, alpha, beta)
                    board[i][j] = ' '
                    if score < final_score:
                        final_score = score
                        final_i, final_j = i, j
                    beta = min(beta, score)
                    if beta <= alpha:
                        break  
            if beta <= alpha:
                break 
    return final_score, final_i, final_j 

def iterative_deepening_minimax(board, max_depth, time_limit_ms):
    start_time = time.time()
    best_move = (-1, -1)
    best_score = None

    for depth in range(1, max_depth + 1):
        current_score, i, j = minimax(board, depth, False, -1000, 1000)
        if (time.time() - start_time) * 1000 >= time_limit_ms:
           break
        best_score = current_score
        best_move = (i, j)

    return best_move, best_score

def main():
    board = [[' ' for _ in range(7)] for _ in range(7)]
    has_winner = False
    player = 'X' 
    while not has_winner:
        print(f"Player {player}'s turn.")

        if player == 'X'
            x, y = map(int, input("Enter row and column (0-6): ").split())
            if 0 <= x < 7 and 0 <= y < 7 and board[x][y] == ' ':
                board[x][y] = player
                draw_board(board)
                result = check_winner(board)
                if result != 1:
                    has_winner = True
                player = 'O'
            else:
                print("The field is not empty or invalid coordinates")
        else:
            # AI's turn using iterative deepening with Alpha-Beta Pruning
            max_depth = 7
            time_limit_ms = 18000 
            best_move, best_score = iterative_deepening_minimax(board, max_depth, time_limit_ms)
            print(f"AI selected move: ({best_move[0]}, {best_move[1]}) with score: {best_score}")
            if best_move != (-1, -1):
                board[best_move[0]][best_move[1]] = 'O'
            draw_board(board)
            result = check_winner(board)
            if result != 1:
                has_winner = True
            player = 'X'  
    result = check_winner(board)
    if result == 0:
        print("Tie")
    else:
        print(f"{'X' if result == 2 else 'O'} player wins")

if __name__ == "__main__":
    main()

