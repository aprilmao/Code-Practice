
class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = self.fillBoard()

    def fillBoard(self):
        board = []
        for eachRow in range(self.height):
            rowOfBoard = []
            for eachCol in range(self.width):
                rowOfBoard.append('*')
            board.append(rowOfBoard)
        return board

    def insertPiece(self, playerCol, player):
        rowToInsert = self.height - 1
        while rowToInsert - 1 > 0 and self.board[rowToInsert][playerCol] != '*':
            rowToInsert -= 1
        if rowToInsert == 0 and self.board[rowToInsert][playerCol] != '*':
            print "Can't place piece here!"
        else:
            self.board[rowToInsert][playerCol] = player
            return rowToInsert

    def printBoard(self):
        for eachRow in self.board:
            for eachCol in eachRow:
                print eachCol,
            print
        print

    def totalHoriz(self, playerRow, playerCol, player):
        counter = 1

        # -->
        tempCol = playerCol
        while tempCol + 1 < 7 and self.board[playerRow][tempCol + 1] == player:
            tempCol += 1
            counter += 1
        # <--
        tempCol = playerCol
        while tempCol - 1 >= 0 and self.board[playerRow][tempCol - 1] == player:
            tempCol -= 1
            counter += 1

        return counter

    def totalVert(self, playerRow, playerCol, player):
        counter = 1

        # down
        tempRow = playerRow
        while tempRow + 1 < 6 and self.board[tempRow + 1][playerCol] == player:
            tempRow += 1
            counter += 1

        return counter

    def totalDiagBT(self, playerRow, playerCol, player):
        counter = 1

        # / player to bottom left
        tempRow = playerRow
        tempCol = playerCol
        while tempRow + 1 < 6 and tempCol + 1 < 7 and self.board[tempRow + 1][tempCol + 1] == player:
            tempRow += 1
            tempCol += 1
            counter += 1

        # / player to top right
        tempRow = playerRow
        tempCol = playerCol
        while tempRow - 1 >= 0 and tempCol - 1 >= 0 and self.board[tempRow - 1][tempCol - 1] == player:
            tempRow -= 1
            tempCol -= 1
            counter += 1

        return counter

    def totalDiagTB(self, playerRow, playerCol, player):
        counter = 1

        # \ player to bottom right
        tempRow = playerRow
        tempCol = playerCol
        while tempRow + 1 < 6 and tempCol - 1 >= 0 and self.board[tempRow + 1][tempCol - 1] == player:
            tempRow += 1
            tempCol -= 1
            counter += 1

        # \ player to top left
        tempRow = playerRow
        tempCol = playerCol
        while tempRow - 1 >= 0 and tempCol + 1 < 7 and self.board[tempRow - 1][tempCol + 1] == player:
            tempRow -= 1
            tempCol += 1
            counter += 1

        return counter

def isWinner(playerRow, playerCol, player):
    countHoriz = game.totalHoriz(playerRow, playerCol, player)
    countVert = game.totalVert(playerRow, playerCol, player)
    countDiagBT = game.totalDiagBT(playerRow, playerCol, player)
    countDiagTB = game.totalDiagTB(playerRow, playerCol, player)
    if countHoriz >= 4 or countVert == 4 or countDiagBT >= 4 or countDiagTB >= 4:
        return True
    else:
        return False

boardX = 7
boardY = 6
playerR = 'R'
playerB = 'B'
player = playerR
game = Board(boardX, boardY)
game.printBoard()
totalPlays = boardX * boardY

while totalPlays > 0:
    print "Insert piece between collumns 1-7: "
    playerCol = int(raw_input())
    playerCol -= 1
    playerRow = game.insertPiece(playerCol,player)
    game.printBoard()
    if isWinner(playerRow, playerCol, player):
        print "Connect Four! " + player + " won!"
        exit()
    totalPlays -= 1
    if player == playerR:
        player = playerB
    elif player == playerB:
        player = playerR
