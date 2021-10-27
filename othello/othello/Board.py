from rules import Rules
import copy
import random as rand



class Color:
    YELLOW = '\033[93m'    # Highlights chips flipped
    RED = '\033[91m'       # The move that was made by the player
    END = '\033[0m'

# turn can flip between 'W' and 'B'
class Turn:

    def __init__(self, turn='B'):
        self.turn = turn

    def flip(self):
        if(self.turn == 'W'):
            self.turn = 'B'
        else:
            self.turn = 'W'
    def getTurn(self):
        return self.turn

#Runs the scoreboard for the game.
class ScoreBoard:

    # player and AI are either 'W' or 'B'. They cannot be the same
    def __init__(self, player, AI):
        assert(player != AI)
        self.whiteScore = 0
        self.blackScore = 0
        self.player = player
        self.AI = AI

    def updateScore(self, w, b):
        self.whiteScore = w
        self.blackScore = b

    def displayScore(self):
        print "----ScoreBoard----"
        if(self.player == 'W'):
            print ("White Score: " + str(self.whiteScore))
            print ("Black Score: " + str(self.blackScore))
            print "------------------"
        else:
            print ("Black Score: " + str(self.blackScore))
            print ("White Score: " + str(self.whiteScore))
            print "------------------"

class Board:

    # Constructor for the Board. Turn defaults to Black.
    # player and AI are either 'W' or 'B'.
    # config : 'W' is for 'W' in top left start. 'B' is for
    # 'B' starting in the top left.
    def __init__(self, player, AI, config, turn='B'):
        # initialize scoreboard with correct player names
        self.scoreboard = ScoreBoard(player, AI)
        # import rules of Othello
        self.rules = Rules()
        #making the board matrix
        self.matrixB = self.__initMatrix(9,9)
        # init previous matrix
        self.__prevMatrix = copy.deepcopy(self.matrixB)
        #whose turn it is; 'B' for black and 'W' for white.
        self.turn = Turn(turn)
        # set up the game and initial Board
        self.__gameSetUp(config)

    #red represents the move made.
    #highlights the changes that were made in the previous move
    def highLightPrint(self,x,y,oldMatrix):
        for i in range(0,9):
            for j in range(0,9):
                if(i ==x and j == y):
                    print(Color.RED + "'" + self.matrixB[i][j] + "'" + Color.END),
                elif(self.matrixB[i][j] != oldMatrix[i][j]):
                    print(Color.YELLOW + "'" + self.matrixB[i][j] + "'" + Color.END ),

                else:
                    print "'" + str(self.matrixB[i][j]) + "'",
            print
        print
        self.scoreboard.displayScore()


    #this print function will display the contents of the board, matrixB
    def printBoard(self):
        for i in range(0,9):
            for j in range(0,9):
                print "'"+str(self.matrixB[i][j])+ "'",
            print
        print
        self.scoreboard.displayScore()


    #returns the value of turn, either B for black or W for white.
    def getTurn(self):
        return self.turn.getTurn()


    # Can make a move or not?
    def can_move(self):
        return self.rules.getCanMove(self.matrixB,self.turn.getTurn())

    #x and y are the coordinate points that correspond to the matrix.
    #The ____move____s alternate so it's easy to have two people, or one and an A.I. play
    def move(self,x,y):
        # if x is 999, no move was made
        if(x == 999):
            self.turn.flip()
            return True

        #in the situation where the player cannot move
        if(self.rules.getCanMove(self.matrixB,self.turn.getTurn())==False):
            print "Player",self.turn.getTurn(),"has no moves to make."
            raw_input("Press any key to continue")
            self.turn.flip()
            return True

        #where the player can move
        if(self.__isLegalMove(x,y)):
            y = self.__changeY(y)
            oldMatrix = copy.deepcopy(self.matrixB)
            self.__prevMatrix = copy.deepcopy(self.matrixB)
            self.matrixB = self.rules.insertMove(self.turn.getTurn(), self.matrixB, x, y)

            #scorring the game
            wScore,bScore = self.getScore()
            self.scoreboard.updateScore(wScore,bScore)
            #prints out all of the scores
            self.highLightPrint(x,y,oldMatrix)

            #flips the turns
            self.turn.flip()
            return True
        else:
            print "Please enter a valid spot to move to."
            return False


    # returns the score as two integer returns: white score followed by black.
    def getScore(self):
        whiteScore = 0
        blackScore = 0
        for i in range(1,9):
            for j in range(1,9):

                if(self.matrixB[i][j] == 'W'):
                    whiteScore += 1
                elif(self.matrixB[i][j] == 'B'):
                    blackScore += 1

        return whiteScore,blackScore

    #displays all legal moves
    def getLegalMoves(self):
        for i in range(8):
            for j in range(8):
                tmpJ = chr(ord(chr(j+1))+64)
                if(self.__isLegalMove(i+1,tmpJ)):
                    print i+1, tmpJ

    # reverts the current board positions to the previous state.
    # this is called in the event of a dispute. Resets the
    # scoreboard and proper turn.
    def revertBoard(self):
        self.matrixB = copy.deepcopy(self.__prevMatrix)
        wScore,bScore = self.getScore()
        self.scoreboard.updateScore(wScore,bScore)
        self.turn.flip()


    # returns true if the game is over. Either the board is full or
    # neither player or AI can make a move.
    def isGameOver(self):
        if(self.turn.getTurn() =='W'):
            opp = 'B'
        else:
            opp = 'W'
        if(self.rules.isGameOver(self.matrixB) == True
         and (self.rules.getCanMove(self.matrixB,self.turn.getTurn()) == False
         and self.rules.getCanMove(self.matrixB,opp) == False)):
            return True
        return False

    ############################
            #PRIVATE
    ############################

    # initialize a game board matrix to be X by Y char arrays
    def __initMatrix(self, x, y):
        matrix = []
        for i in range(0,y):
            line = []
            for i in range(0,x):
                line.append('-')
            matrix.append(line)
        return matrix


    #Running the initial set ups for the game.
    def __gameSetUp(self, config='W'):
        self.__createBoard()
        self.__startingBoard(config)

    #adds the values onto the Othello Board for references.
    def __createBoard(self):
        self.matrixB[0][0] = '*'
        for i in range(1,9):
            self.matrixB[0][i] =  chr(ord('A')+i-1)
            if(i == 2):
                self.matrixB[0][i] =  chr(ord('a')+i-1)
        for i in range(1,9):
            self.matrixB[i][0] = i

        print "create board"


    #Sets the starting pieces to the game without toggling the turn.
    # if config == 1, begins with 'B' in top left.
    # if config == 2, begins with 'W' in top left
    def __startingBoard(self, config):
        print config

        '''
        if(config == 'W'):

            for i in range(6):
                for j in range(8):
                    tmp = rand.randint(0,2)
                    if(tmp == 2):
                        self.matrixB[i+1][j+1] = 'B'
                    else:
                        self.matrixB[i+1][j+1] = 'W'


            self.matrixB[7][1] = '-'
            self.matrixB[7][7] = '-'
            self.matrixB[7][8] = '-'
            self.matrixB[5][6] = '-'

            #self.matrixB[8,2] = 'B'


            #self.matrixB[1,3] = 'W'
            #self.matrixB[1,4] = 'B'
            #self.matrixB[2,1] = 'B'
        '''
        if(config == 'W'):
            self.matrixB[4][5] = 'B'
            self.matrixB[4][4] = 'W'
            self.matrixB[5][4] = 'B'
            self.matrixB[5][5] = 'W'

        elif(config == 'B'):
            self.matrixB[4][5] = 'W'
            self.matrixB[4][4] = 'B'
            self.matrixB[5][4] = 'W'
            self.matrixB[5][5] = 'B'

        else:
            raise Exception("startingConfig bound error")

        self.scoreboard.updateScore(2,2)



    #changes the value of the uptop letters to integers in order to
    #let the matrix have the correct input.
    def __changeY(self,y):
        #need to establish this as an integer otherwise it may cause errors
        return int(chr(ord(y)-16))

    # checks if a submitted move is legal.
    # - checks valid input characters
    # - checks if the spot is open
    # - checks if the move is Othello-legal
    def __isLegalMove(self,x,y):
        if(self.__checkInput(x,y) and self.__isSpotOpen(x,y)):
            y = self.__changeY(y)
            return self.rules.isLegalMove(x,y,self.matrixB,self.turn.getTurn())
        return False

    #Checks to make sure that the x and y input are valid characters for the board.
    #Currently not in use but I thought it would be valuable to have.
    def __checkInput(self,x,y):
        if(x < 1 or x > 8):
            print "Bad x value input; keep in the range of 1-8."
            return False
        if(y >= 'A' and y <= 'H' or y>='a' and y <= 'h'):
            return True
        else:
            print "Bad y value input; keep in the range of A-H."
            return False

    #Returns true if the spot is open, false otherwise.
    def __isSpotOpen(self,x,y):
        y = self.__changeY(y)
        return(self.matrixB[x][y] == '-')

    #Given an oldmatrix it will find the amount of differences from board to board.
    def __getNumberOfChanges(self,oldMatrix):
        count = 0
        for i in range(0,9):
            for j in range(0,9):
                if(self.matrixB[i][j] != oldMatrix[i][j]):
                    count+=1
        return count-1
# if Board.py is top-level module, run main. (used only for testing)
if(__name__ == "__main__"):
    b = Board( 'W', 'B', 'W', 'B')

    print b.getTurn()
    b.move(3,'D')
    b.move(3,'C')
    b.move(4,'C')
    print(b.getTurn())
    b.move(5,'C')
    b.move(4,'B')
    b.move(2,'D')
    print(b.getTurn())
    b.move(2,'C')
    b.move(4,'A')
    b.printBoard()
    b.move(1,'D')
    b.move(2,'B')
    b.move(6,'D')
    b.move(3,'E')
    b.move(4,'F')
    b.move(2,'E')

    b.move(1,'E')

    b.move(5,'G')
    print b.getTurn()
    b.move(5,'B')
    b.move(2,'F')
    b.move(3,'G')
    b.move(6,'E')
    b.move(1,'C')
    b.move(4,'G')
    b.move(6,'H')
    b.move(1,'B')
    b.move(3,'B')
    b.move(6,'B')
    b.move(6,'C')
    b.move(2,'H')
    b.move(2,'G')
    b.move(2,'A')
    b.move(7,'E')
    b.move(6,'F')
    b.move(1,'A')
    b.move(8,'E')
    b.move(3,'A')
    b.move(5,'A')
    b.move(7,'G')
    b.move(3,'F')
    b.move(7,'C')
    b.move(1,'F')
    b.move(7,'F')
    b.move(6,'G')
    b.move(6,'A')
    b.move(8,'C')
    b.move(7,'B')
    b.move(8,'A')
    b.move(7,'D')
    b.move(7,'H')
    b.move(1,'G')
    b.move(1,'H')
    b.move(8,'H')
    b.move(8,'H')
    b.move(5,'H')
    b.move(4,'H')
    b.move(5,'F')
    b.move(8,'F')
    b.move(3,'H')
    b.move(8,'B')
    b.move(8,'G')
    b.move(8,'D')
    b.move(7,'A')
    b.move(7,'A')
    j = 1
    tmpJ = chr(ord(chr(j))+65)
    print tmpJ
    print b.getTurn()
