import random
HEIGHT = 3
WIDTH = 3

def new_board():
    board = [[None for _ in range(HEIGHT)] for _ in range(WIDTH)]
    
    return board

def render(board):
    print("  0 1 2")
    print("  -----")
    
    for row in range(WIDTH):
        print(f'{row}|', end="")
        
        for col in range(HEIGHT):
            move = board[row][col]
            if board[row][col] == None:
                move = ' '
            else:
                move = board[row][col]
                
            if col != 2:
                print(f'{move} ', end="")
            else:
                print(f'{move}|')
    print("  -----")
    
def get_move():
    row = int(input("Enter the row for your move (0, 1, or 2): "))
    col = int(input("Enter the column for your move (0, 1, or 2): "))
    print()
    
    return (row, col)

def make_move(board, coord, player):
    row = coord[0]
    col = coord[1]
    
    if is_valid_move(board, coord):
        board[row][col] = player
    else:
        print(f'Can\'t make move {coord}, square already taken!')
        move = get_move()
        make_move(board, move, player)
        
def is_valid_move(board, coord):
    row = coord[0]
    col = coord[1]
    
    if board[row][col] == None:
        return True
    else:
        return False
    
def play():
    board = new_board()
    
    while True:
        move = get_move()
        make_move(board, move, "X")
        render(board)
        
        winner = get_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        
        move = get_move()
        make_move(board, move, "O")
        render(board)
        
        winner = get_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        
    print("Game over!")
    
def get_winner(board):
    # Check rows
    for row in board:
        if row.count("X") == WIDTH:
            return "X"
        elif row.count("O") == WIDTH:
            return "O"
    
    # Check columns
    for col in range(HEIGHT):
        column = [board[row][col] for row in range(WIDTH)]
        if column.count("X") == HEIGHT:
            return "X"
        elif column.count("O") == HEIGHT:
            return "O"
    
    # Check diagonals
    diagonal1 = [board[i][i] for i in range(WIDTH)]
    diagonal2 = [board[i][WIDTH - 1 - i] for i in range(WIDTH)]
    if diagonal1.count("X") == WIDTH or diagonal2.count("X") == WIDTH:
        return "X"
    elif diagonal1.count("O") == WIDTH or diagonal2.count("O") == WIDTH:
        return "O"
    
    if all(move is not None for row in board for move in row):
        return "Tie"
    
    return None


if __name__ == "__main__":
    play()
    