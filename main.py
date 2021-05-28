import numpy as np
import os
import time


class treeNode:
    nextNodes = []

class tree:
    firstNode = []


# Creacion del tablero
# 0 = vacio, 1 = jugador, 2 = computadora
board = np.array([
                [0,0,0], 
                [0,0,0],
                [0,0,0]])

def movesLeft():
    for row in board:
        for col in row:
            if(col == 0):
                return True
    return False

# Funcion heuristica para determinar la puntuacion por movimiento
def minMax(isMax):
    if(hasWon(1) == True):
        return 10
    
    if(hasWon(2) == True):
        return -10
    
    if(movesLeft() == False):
        return 0
    
    if(isMax == True):
        best = -1000

        i = 0
        j = 0
        for row in board:
            for col in row:
                if(board[i,j] == 0):
                    board[i,j] = 1
                    best = max(best, minMax(not isMax))
                    board[i,j] = 0

    else:
        best = 1000

        i = 0
        j = 0
        for row in board:
            for col in row:
                if(board[i,j] == 0):
                    board[i,j] = 2
                    best = min(best, minMax(not isMax))
                    board[i,j] = 0
    
    return best


def hasWon(player=1):

    # Ganada por fila
    for row in board:
        if(row[0] == row[1] == row[2] == player):
            return True

    # Ganada por columna
    for col in range(0,3):
        colIsNotValidWin = False
        for row in board:
            if(row[col] != player):
                colIsNotValidWin = True
        if not colIsNotValidWin:
            return True
    
    if(board[0,0] == board[1,1] == board[2,2] == player):
        return True
    
    if(board[0,2] == board[1,1] == board[2,0] == player):
        return True
    
    return False

# Funcion para obtener el movimiento del jugador
def getPlayerInput():
    row = input("Introduzca la fila del movimiento deseado (1-3)")
    col = input("Introduzca la columna del movimiento deseado (1-3)")
    try:
        if(board[int(row) - 1, int(col) - 1] == 0):
            board[int(row) - 1, int(col) - 1] = 1
        else:
            clearScreen()
            printBoard()
            print("Lugar en el tablero ocupado")
            getPlayerInput()
    except:
        clearScreen()
        printBoard()
        print("Fila o columna invalida")
        getPlayerInput()

def clearScreen():
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

def printBoard():
    for row in board:
        for piece in row:
            if(piece == 0):
                print("-", end='')
            elif(piece == 1):
                print("X", end='')
            elif(piece == 2):
                print("O", end='')
        print("\n")

def makeAIMove():
    if(hasWon(1) == True or hasWon(2) == True):
        print("Ganada")
        time.sleep(1)
        return

    bestVal = -1000

    
    bi = -1
    bj = -1
    i = 0
    j = 0
    for row in board:
        j = 0
        for col in row:
            if(col == 0):
                board[i,j] = 1

                moveVal = minMax(False)

                board[i,j] = 0

                if(moveVal > bestVal):
                    bestVal = moveVal
                    bi = i
                    bj = j

            j = j + 1
        i = i + 1
    
    board[bi,bj] = 2



def main():
    gameWon = False

    while(gameWon == False):
        clearScreen()
        makeAIMove()
        printBoard()
        getPlayerInput()


main()
