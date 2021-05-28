import numpy as np
import os
import time


class bestMove:
    i = 0
    j = 0
    val = 0
    alpha = 0
    beta = 0


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

def minMax(isMax, alpha, beta):
    # Si no se puede realizar ningun movimiento, devolver la evaluacion
    if not movesLeft():
        val = evalFunc()
        retval = bestMove()
        retval.val = val
        return retval

    if isMax:
        maxVal = -1000
        bi, bj = 0, 0
        i = 0
        for row in board:
            j = 0
            for col in row:
                if(col == 0):
                    board[i,j] = 2
                    eval = minMax(False, alpha, beta).val
                    if(eval >= maxVal):
                        bi = i
                        bj = j
                    maxVal = max(maxVal, eval)
                    alpha = max(alpha, eval)
                    board[i,j] = 0

                j = j + 1
            
            i = i +1
        
        retval = bestMove()
        retval.val = maxVal
        retval.i = bi
        retval.j = bj
        return retval
    else:
        minVal = 1000
        bi, bj = 0,0
        i = 0
        for row in board:
            j = 0
            for col in row:
                if(col == 0):
                    board[i,j] = 1
                    eval = minMax(True, alpha, beta).val
                    if(eval <= minVal):
                        bi = i
                        bj = j
                    minVal = min(minVal, eval)
                    beta = min(beta, eval)
                    board[i,j] = 0

                j += 1
            i += 1


        retval = bestMove()
        retval.val = minVal
        retval.i = bi
        retval.j = bj
        return retval

# Funcion heuristica para determinar la puntuacion por movimiento
def evalFunc():

    playerScore = 0
    pcScore = 0

    if(hasWon(1)):
        return -100     # Jugador gana
    elif(hasWon(2)):
        return 100      # Computadora gana
    else:
        for row in board:
            pc = 0
            blank = 0
            player = 0
            for col in row:
                if(col == 0):
                    blank += 1
                if(col == 1):
                    player += 1
                if(col == 2):
                    pc += 1

            if(player == 0):
                if(pc == 1):
                    pcScore += 1
                elif(pc == 2):
                    pcScore += 10
            elif(pc == 0):
                if(player == 1):
                    playerScore += 1
                elif(player == 2):
                    playerScore += 10

        for col in range(0,3):
            pc = 0
            blank = 0
            player = 0
            for row in board:
                if(row[col] == 0):
                    blank += 1
                if(row[col] == 1):
                    player += 1
                if(row[col] == 2):
                    pc += 1
            
            if(player == 0):
                if(pc == 1):
                    pcScore += 1
                elif(pc == 2):
                    pcScore += 10
            elif(pc == 0):
                if(player == 1):
                    playerScore += 1
                elif(player == 2):
                    playerScore += 10
        
        blank = 0
        player = 0
        pc = 0
        for i in range(0,3):
            if(board[i,i] == 0):
                blank += 1
            if(board[i,i] == 1):
                player += 1
            if(board[i,i] == 2):
                pc += 1
        
        if(player == 0):
                if(pc == 1):
                    pcScore += 1
                elif(pc == 2):
                    pcScore += 10
        elif(pc == 0):
            if(player == 1):
                playerScore += 1
            elif(player == 2):
                playerScore += 10

        blank = 0
        player = 0
        pc = 0
        for i in range(2,-1, -1):
            if(board[2 - i,i] == 0):
                blank += 1
            if(board[2 - i,i] == 1):
                player += 1
            if(board[2 - i,i] == 2):
                pc += 1
        
        # print(str(blank) + "  " + str(player) + "   " + str(pc))

        if(player == 0):
                if(pc == 1):
                    pcScore += 1
                elif(pc == 2):
                    pcScore += 10
        elif(pc == 0):
            if(player == 1):
                playerScore += 1
            elif(player == 2):
                playerScore += 10
    return pcScore - playerScore
            

# Determinar si el jugador ha ganado
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
def getPlayerInput(player = 1):
    row = input("Introduzca la fila del movimiento deseado (1-3)")
    col = input("Introduzca la columna del movimiento deseado (1-3)")
    try:
        if(board[int(row) - 1, int(col) - 1] == 0):
            board[int(row) - 1, int(col) - 1] = player
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

# Limpiar la pantalla
def clearScreen():
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

# Imprimir en consola el tablero
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


def main():

    while(hasWon() == hasWon(2) == False and movesLeft()):
        alpha = -1000
        beta = 1000

        clearScreen()
        move = minMax(True, alpha, beta)
        board[move.i, move.j] = 2
        printBoard()
        print(evalFunc())
        getPlayerInput()

    clearScreen()
    printBoard()
    if(hasWon(1)):
        print("Ganaste!")
    elif(hasWon(2)):
        print("Perdiste!")
    else:
        print("Empate")

        
main()
