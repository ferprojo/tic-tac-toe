import numpy as np
import os

# Creacion del tablero
# 0 = vacio, 1 = jugador, 2 = computadora
board = np.array(   [[0,0,0], 
            [0,0,0],
            [0,0,0]])

# Funcion heuristica para determinar la puntuacion por movimiento
def heuristic():
    pass

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

def getAIInput():
    pass


def main():
    gameWon = False

    while(gameWon == False):
        clearScreen()
        printBoard()
        getPlayerInput()
        getAIInput()


main()
