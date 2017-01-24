import random
import sys

class Board():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = self.fillBoard()
        self.game = self.fillBoard()

    def fillBoard(self):
        board =[]
        for elemCellX in range(self.height):
            eachRow = []
            for elemCellY in range(self.width):
                eachRow.append(0)
            board.append(eachRow)
        return board

    def placeMines(self, mines):
        numOfCells = self.width * self.height
        for elemCell in range(mines):
            coorOfMine = random.randint(0, numOfCells-1)
            coorYInBoard = (coorOfMine / self.width) + 1
            coorXInBoard = (coorOfMine % self.width) + 1
            self.board[coorXInBoard-1][coorYInBoard-1] = 'M'

    def getMineNum(self, coorX, coorY):
        countMines = 0
        if self.board[coorX + 1][coorY + 1] == 'M':
            countMines += 1
        if self.board[coorX - 1][coorY - 1] == 'M':
             countMines += 1
        if self.board[coorX + 1][coorY - 1] == 'M':
            countMines += 1
        if self.board[coorX - 1][coorY + 1]== 'M':
            countMines += 1
        if self.board[coorX + 1][coorY]== 'M':
             countMines += 1
        if self.board[coorX - 1][coorY] == 'M':
            countMines += 1
        if self.board[coorX][coorY + 1] == 'M':
            countMines += 1
        if self.board[coorX][coorY - 1] == 'M':
            countMines += 1
        self.game[coorX][coorY] = countMines

    def printGame(self):
        for elemCellX in self.game:
            for elemCellY in elemCellX:
                print elemCellY ,
            print
        print

    def isBomb(self, coorX, coorY):
        if self.board[coorX][coorY] == 'M':
            return True
        return False

def playGame(coorX, coorY):
    if game.isBomb(coorX, coorY):
        return True
    else:
        game.getMineNum(coorX, coorY)
        game.printGame()


width = 10
height = 10
mines = 10
game = Board(width, height)
game.placeMines(mines)
maxPlayes = (width*height) - mines

while maxPlayes > 0:
    print "What coordinates do you want to uncover?(EX: / 4 5) "
    playerX = int(raw_input())
    playerY = int(raw_input())
    if playGame(playerX, playerY):
        print "Lost!"
    maxPlayes -= 1

if maxPlayes == 1:
   print "YOU WON!!"
