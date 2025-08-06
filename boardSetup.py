import numpy as np

class tile:
    def __init__(self, ypos, xpos, color):
        #self.ypos = ypos
        #self.xpos = xpos
        self.color = color

    def place(self, color):
        self.color = color

class board():
    def __init__(self, position):

         self.position = position

    def checkDirection(self, dx, dy, xpos, ypos, color, otherColor):
        tilesToChange = []
        for i in range(1, 7):
            try:
                if self.position[xpos+i*dx, ypos+i*dy].color==otherColor:
                     tilesToChange.append(self.position[xpos+dx, ypos+dy])
                     #print("found")
                elif self.position[xpos+i*dx, ypos+i*dy].color==color:
                    return tilesToChange
                else:
                    return []
            except:
                return []
        return []



    def whatWillItColor(self, xpos, ypos, color):
        #check tile is "▣ "
        if self.position[xpos, ypos].color!="▣ ":
            return []
        tilesToChange = []
        if color == "⬜ ":
            otherColor = "⬛ "
        elif color == "⬛ ":
            otherColor = "⬜ "


        tilesToChange = tilesToChange + self.checkDirection(1, 1, xpos, ypos, color, otherColor)
        tilesToChange = tilesToChange + self.checkDirection(0, 1, xpos, ypos, color, otherColor)
        tilesToChange = tilesToChange + self.checkDirection(-1, 1, xpos, ypos, color, otherColor)
        tilesToChange = tilesToChange + self.checkDirection(1, 0, xpos, ypos, color, otherColor)
        tilesToChange = tilesToChange + self.checkDirection(-1, 0, xpos, ypos, color, otherColor)
        tilesToChange = tilesToChange + self.checkDirection(1, -1, xpos, ypos, color, otherColor)
        tilesToChange = tilesToChange + self.checkDirection(0, -1, xpos, ypos, color, otherColor)
        tilesToChange = tilesToChange + self.checkDirection(-1, -1, xpos, ypos, color, otherColor)
        return tilesToChange


def setupEmptyBoard():
    """initial setup, should look like this:
1  2  3  4  5  6  7  8
0▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣
1▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣
2▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣
3▣ ▣ ▣ ⬛ ⬜ ▣ ▣ ▣
4▣ ▣ ▣ ⬜ ⬛ ▣ ▣ ▣
5▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣
6▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣
7▣ ▣ ▣ ▣ ▣ ▣ ▣ ▣ """
    grid = np.empty( (8,8), dtype=object)
    for y in range(8):
        for x in range(8):
            if x == 3 and y == 3 or x==4 and y == 4:
                grid[x, y] = tile(x, y, "⬛ ")
            elif x == 4 and y == 3 or x == 3 and y == 4:
                grid[x, y] = tile(x, y, "⬜ ")
            else:
                grid[x, y] = tile(x, y, "▣ ")# 

    return board(grid)
