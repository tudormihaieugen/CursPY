"""Tic Tac Toe"""
import random

board = [' '] * 9
player = 'X'

def Draw(b):
    print('-------------------')
    print('| ', b[0], ' | ', b[1], ' | ', b[2], ' |')
    print('-------------------')
    print('| ', b[3], ' | ', b[4], ' | ', b[5], ' |')
    print('-------------------')
    print('| ', b[6], ' | ', b[7], ' | ', b[8], ' |')
    print('-------------------')

def Input(b):
    a = input("Enter a number (1-9)(0=EXIT): ")
    try:
        a = int(a)
        if 1 <= a <= 9 and b[a - 1] == ' ':
            b[a - 1] = player
        elif a == 0:
            exit()
        else:
            print("Invalid move.")
            Input(b)
    except ValueError:
        print("Invalid input.")
        Input(b)

def TogglePlayer():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

def BoardCopy(b):
    bCopy = []
    for i in b:
        bCopy.append(i)
    return bCopy

def TestWinMove(b, mark, i):
    bCopy = BoardCopy(b)
    bCopy[i] = mark
    return CheckWin(bCopy, mark)

def OptimalMove(b):
    # Check computer win moves
    for i in range(0, 9):
        if b[i] == ' ' and TestWinMove(b, 'O', i):
            return i
    # Check player win moves
    for i in range(0, 9):
        if b[i] == ' ' and TestWinMove(b, 'X', i):
            return i
    # Check computer fork opportunities
    for i in range(0, 9):
        if b[i] == ' ' and TestForkMove(b, 'O', i):
            return i
    # Check player fork opportunities, including two forks
    playerForks = 0
    tempMove = 0
    for i in range(0, 9):
        if b[i] == ' ' and TestForkMove(b, 'X', i):
            playerForks += 1
            tempMove = i
    if playerForks == 1:
        return tempMove
    elif playerForks == 2:
        for j in [1, 3, 5, 7]:
            if b[j] == ' ':
                return j
    # Play center
    if b[4] == ' ':
        return 4
    # Play a random corner
    i = random.choice([0, 2, 6, 8])
    if b[i] == ' ':
        return i
    # Play a random size
    i = random.choice([1, 3, 5, 7])
    if b[i] == ' ':
        return i

def TestForkMove(b, mark, i):
    bCopy = BoardCopy(b)
    bCopy[i] = mark
    winningMoves = 0
    for j in range(0, 9):
        if TestWinMove(bCopy, mark, j) and bCopy[j] == ' ':
            winningMoves += 1
    return winningMoves >= 2

def CheckWin(b, m):
    return ((b[0] == b[1] == b[2] == m)      # 1L
            or (b[3] == b[4] == b[5] == m)   # 2L
            or (b[6] == b[7] == b[8] == m)   # 3L
            or (b[0] == b[3] == b[6] == m)   # 1C
            or (b[1] == b[4] == b[7] == m)   # 2C
            or (b[2] == b[5] == b[8] == m)   # 3C
            or (b[0] == b[4] == b[8] == m)   # DP
            or (b[2] == b[4] == b[6] == m))  # DS

def CheckDraw(b):
    return ' ' not in b

Draw(board)
while True:
    if player == 'X':
        Input(board)
    else:
        print("CPU:")
        move = OptimalMove(board)
        board[move] = 'O'
    Draw(board)
    if CheckWin(board, player):
        if player == 'O':
            print("You lost!")
        else:
            print("You won!")
        break
    if CheckDraw(board):
        print("It's a draw!")
        break
    TogglePlayer()
