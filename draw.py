import numpy as np

def drawBoard(board):
    rows = len(board.position)
    print(" 0  1  2  3  4  5  6  7")
    for y in range (rows):
        print(y, end='')
        for x in range (rows):
            if board.whatWillItColor(x, y, "⬜ "):
                print("⛶ ", end='')
            else:
                print(board.position[x, y].color, end='')#, flush=True
        #print([board.position[x, y].color  for y in range (rows)])
        print("")