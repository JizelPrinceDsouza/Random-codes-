theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

def printBoard(board):
    print(board['top-L'] + '|' , board['top-M'] + '|' , board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' , board['mid-M'] + '|' , board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' , board['low-M'] + '|' , board['low-R'])

for i in range(9):
    printBoard(theBoard)
    symbol = input("Enter your symbol (X or O): ").upper()
    if symbol not in ['X', 'O']:
        print("Invalid symbol. Please enter X or O.")
        continue

    move = input("Enter the position to move : ")
    if move not in theBoard or theBoard[move] != ' ':
        print("Invalid move. Try again.")
        continue

    theBoard[move] = symbol

printBoard(theBoard)