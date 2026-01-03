import random

# Initialize the game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"   # Player starts first
winner = None
gameRunning = True


# Function to print the board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# Function to take player input
def playerInput(board):
    while True:
        inp = int(input("Select a spot (1-9): "))
        if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
            board[inp - 1] = currentPlayer
            break
        else:
            print("Invalid move. Try again.")


# Check horizontal win
def checkHorizontal(board):
    global winner
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != "-":
            winner = board[i]
            return True
    return False


# Check vertical win
def checkVertical(board):
    global winner
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != "-":
            winner = board[i]
            return True
    return False


# Check diagonal win
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False


# Check if someone won
def checkWin(board):
    global gameRunning
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        printBoard(board)
        print(f"Winner is {winner} 🎉")
        gameRunning = False


# Check for tie
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie 🤝")
        gameRunning = False


# Switch the current player
def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"


# Computer move (random)
def computerMove(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


# Main game loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
    computerMove(board)
    checkWin(board)
    checkTie(board)
