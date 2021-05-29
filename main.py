import numpy as np
import os
import time
import random

class bestMove:
    i = 0
    j = 0
    val = 0
    alpha = 0
    beta = 0


execcount = 0


def movesLeft(board):
    
    # Ganada por fila
    for row in board:
        if(row[0] == row[1] == row[2] != 0):
            return row[0]

    # Ganada por columna
    for i in range(0,3):
        if(board[0,i] == board[1,i] == board[2,i] != 0):
            return board[0,i]
    
    if(board[0,0] == board[1,1] == board[2,2] != 0):
        return board[0,0]
    
    if(board[0,2] == board[1,1] == board[2,0] != 0):
        return board[0,2]

    for i in range(0,3):
        for j in range(0,3):
            if(board[i,j] == 0):
                return 0

def minMax(isMax, board, alpha, beta, depth = 60):


    # Si no se puede realizar ningun movimiento, devolver la evaluacion
    res = movesLeft(board)
    if res != 0 or depth == 0:
        val = simpleEvalFunc(res)
        retval = bestMove()
        retval.val = val
        return retval

    if isMax:
        maxVal = -10000
        bi, bj = 0, 0
        i = 0
        for row in board:
            j = 0
            for col in row:
                if(col == 0):
                    board[i,j] = 2
                    eval = minMax(False, board, alpha, beta, depth - 1).val
                    if(eval > maxVal):
                        bi = i
                        bj = j
                        #printBoard(board)
                        #print(str(eval) + "  " + str(maxVal))
                        #print("\n\n\n")
                    maxVal = max(maxVal, eval)
                    board[i,j] = 0

                j = j + 1
            
            i = i +1
        
        retval = bestMove()
        retval.val = maxVal
        retval.i = bi
        retval.j = bj
        return retval
    else:
        minVal = 10000
        bi, bj = 0,0
        i = 0
        for row in board:
            j = 0
            for col in row:
                if(col == 0):
                    board[i,j] = 1
                    eval = minMax(True,board, alpha, beta, depth - 1).val
                    if(eval < minVal):
                        bi = i
                        bj = j
                        #printBoard(board)
                        #print(str(eval) + "  " + str(minVal))
                        #print("\n\n\n")
                    minVal = min(minVal, eval)
                    board[i,j] = 0

                j += 1
            i += 1


        retval = bestMove()
        retval.val = minVal
        retval.i = bi
        retval.j = bj
        return retval

# Funcion heuristica para determinar la puntuacion por movimiento
def evalFunc(board):

    playerScore = 0
    pcScore = 0

    if(hasWon(1)):
        return -500     # Jugador gana
    elif(hasWon(2)):
        return 500      # Computadora gana
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

def simpleEvalFunc(board):
    global execcount
    execcount += 1
    if(board == 2):
        return 100     # Jugador gana
    elif(board == 1):
        return -100      # Computadora gana
    else:
        return 0

# Determinar si el jugador ha ganado
def hasWon(board, player=1):

    # Ganada por fila
    for row in board:
        if(row[0] == row[1] == row[2] == player):
            return True

    # Ganada por columna
    for i in range(0,3):
        if(board[0,i] == board[1,i] == board[2,i] == player):
            return True
    
    if(board[0,0] == board[1,1] == board[2,2] == player):
        return True
    
    if(board[0,2] == board[1,1] == board[2,0] == player):
        return True
    
    return False

# Funcion para obtener el movimiento del jugador
def getPlayerInput(board, player = 1):
    row = input("Introduzca la fila del movimiento deseado (1-3)")
    col = input("Introduzca la columna del movimiento deseado (1-3)")
    try:
        if(board[int(row) - 1, int(col) - 1] == 0):
            board[int(row) - 1, int(col) - 1] = player
            return [row, col]
        else:
            clearScreen()
            printBoard(board)
            print("Lugar en el tablero ocupado")
            getPlayerInput(board)
    except:
        clearScreen()
        printBoard(board)
        print("Fila o columna invalida")
        getPlayerInput(board)

# Limpiar la pantalla
def clearScreen():
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')

# Imprimir en consola el tablero
def printBoard(board):
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
    global execcount

    # Creacion del tablero
    # 0 = vacio, 1 = jugador, 2 = computadora
    board = np.array([
                    [0,0,0], 
                    [0,0,0],
                    [0,0,0]])

    emptyBoard = np.array([
                    [0,0,0], 
                    [0,0,0],
                    [0,0,0]])

    while(movesLeft(board) == 0):        
        clearScreen()
        printBoard(board)
        print(execcount)
        execcount = 0
        if(movesLeft(board) == 0):
          getPlayerInput(board)
        if(movesLeft(board) == 0):
            move = minMax(True, board, -1000, 1000, 60)
            board[move.i, move.j] = 2

    clearScreen()
    printBoard(board)
    if(hasWon(board, 1)):
        print("Ganaste!")
    elif(hasWon(board, 2)):
        print("Perdiste!")
    else:
        print("Empate")


def getExecutionTimes(board, depth = 60):
    global execcount
    f = open("exectime" + str(depth) + "dpt.csv", "w")
    for i in range(0, 100):
        execcount = 0
        print(i)
        start_time = time.time()
        minMax(True, board, -1000, 1000, depth)
        f.write(str(time.time() - start_time) + "\n")
        print(execcount)
    
    f.close()

main()




