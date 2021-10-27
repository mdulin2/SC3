
class Rules:

    #this needs to check if either player cannot move
    # returns true if the game is over. false otherwise
    def isGameOver(self, matrix):
        if(self.__isFull(matrix)):
            return True
        if((not self.getCanMove(matrix, 'B')) or (not self.getCanMove(matrix, 'W'))):
            return True
        return False

    #return true if the user is able to move, false otherwise
    def getCanMove(self,matrixB,turn):
        return self.__canMove(matrixB,turn)

    #Checks to see if a move is a legal move or not.
    #x and y are the values from the matrixB
    #matrixB is the board
    #turn is the person's turn to move ('W' or 'B')
    #move is the direction that the search is attempting to go.
    def isLegalMove(self,x,y,matrixB,turn):
        if(matrixB[x][y] != '-'):
            return False
        if(self.__isLegalHelper(x,y,matrixB,turn,'U',0)):
            return True
        if(self.__isLegalHelper(x,y,matrixB,turn,'UR',0)):
            return True
        if(self.__isLegalHelper(x,y,matrixB,turn,'R',0)):
            return True
        if(self.__isLegalHelper(x,y,matrixB,turn,'DR',0)):
            return True
        if(self.__isLegalHelper(x,y,matrixB,turn,'D',0)):
            return True
        if(self.__isLegalHelper(x,y,matrixB,turn,'DL',0)):
            return True
        if(self.__isLegalHelper(x,y,matrixB,turn,'L',0)):
            return True
        if(self.__isLegalHelper(x,y,matrixB,turn,'UL',0)):
            return True
        return False

    # given a previous state matrix and coordinates for insertion,
    # makes a move and flips all necessary chips according to
    # othello rulesF
    def insertMove(self, turn, matrix, x, y):
        matrix2 = self.__makeMove(turn, matrix, x, y)
        return self.__fixBoard(matrix2, x, y,turn)

    #The possible amount of moves in a turn
    def getMoveCount(self,matrix,turn):
        count = 0
        for i in range(1,9):
            for j in range(1,9):
                if(matrix[i][j] == '-'):
                    if(self.isLegalMove(i,j,matrix,turn)):
                        count +=1
        return count

    ###########################
    # PRIVATE BELOW
    #########################


    # flips all necessary chips after a move has been made.
    # retuns resulting matrix.
    def __fixBoard(self,matrix,x,y,turn):
        return self.__flipChipString(x,y,matrix,turn)

    '''
    Flips all of the chips on the board that should be flipped in all directions.
    maxtrix B is the board
    Turn is the player that made that move to change the board
    Each line in this changes a particular path of the board, if needed.
    '''
    def __flipChipString(self,x,y,matrixB,turn):

        matrixB,score1 = self.__flipChipStringHelper(x,y,matrixB,turn,'U',0) #up

        matrixB,score2 = self.__flipChipStringHelper(x,y,matrixB,turn,'UR',0) #up right

        matrixB,score3 =self.__flipChipStringHelper(x,y,matrixB,turn,'R',0) #right

        matrixB,score4 = self.__flipChipStringHelper(x,y,matrixB,turn,'DR',0) #down right

        matrixB,score5 = self.__flipChipStringHelper(x,y,matrixB,turn,'D',0) #down

        matrixB,score6 = self.__flipChipStringHelper(x,y,matrixB,turn,'DL',0) #down left

        matrixB,score7 = self.__flipChipStringHelper(x,y,matrixB,turn,'L',0) #left

        matrixB,score8 = self.__flipChipStringHelper(x,y,matrixB,turn,'UL',0) #up left

        return matrixB

    '''
    matrixB is the board, x and y are the coordinates on the board.
    Turn is the user who played the move, move is the direction the flow is going.
    '''
    def __flipChipStringHelper(self,x,y,matrixB,turn,move,oldscore):
        #setting the oppenents name(B or W)
        if turn == "W":
            opp = "B"
        elif(turn == 'B'):
            opp = "W"

        #sets the new values of the coordinates
        x,y = self.__getCoordinate(x,y,move)

        #checks to see if the line needs to be changed.
        tmp,score = self.__lineCheck(x,y,matrixB,turn,move)
        score+=oldscore

        if(tmp):

            if(matrixB[x][y] == opp):
                #flips the actual value of the chip on the board.
                matrixB = self.__flipChip(x,y,matrixB)
                return self.__flipChipStringHelper(x,y,matrixB,turn,move,score)
            elif(matrixB[x][y] == turn):
                #returns the matrix once it is finished being altered
                return matrixB,score

            else:
                return matrixB,score
        #if no change needs to be done then send the matrix back
        return matrixB,score

    '''#checks to see if a direction of a board needs to be changed.
    x and y are the coordinates of the matrixB.
    matrixB is the board.
    turn is the person who just made the move to change the board.
    move is the direction that is being checked
    '''
    def __lineCheck(self,x,y,matrixB,turn,move):
        #each line has a particular direction that it checks
        if(move =='U'):
            return self.__lineCheckHelper(x,y,matrixB,turn,'U',0)
        elif(move == 'UR'):
            return self.__lineCheckHelper(x,y,matrixB,turn,'UR',0)
        elif(move == 'R'):
            return self.__lineCheckHelper(x,y,matrixB,turn,'R',0)
        elif(move == 'DR'):
            return self.__lineCheckHelper(x,y,matrixB,turn,'DR',0)
        elif(move == 'D'):
            return self.__lineCheckHelper(x,y,matrixB,turn,'D',0)
        elif(move == 'DL'):
            return self.__lineCheckHelper(x,y,matrixB,turn,'DL',0)
        elif(move == 'L'):
            return self.__lineCheckHelper(x,y,matrixB,turn,'L',0)
        elif(move == 'UL'):
            return self.__lineCheckHelper(x,y,matrixB,turn,'UL',0)
        return False


    '''Returns true if the line can be flipped, false otherwise.
    x,y,matrixB,turn and move are the same as the normal function
    score is the amount of chips that needs to be flipped
    '''
    def __lineCheckHelper(self,x,y,matrixB,turn,move,score):

        if turn == "W":
            opp = "B"
        elif(turn == 'B'):
            opp = "W"

        try:

            if(matrixB[x][y] == opp):
                score+=1
                x,y = self.__getCoordinate(x,y,move)
                return self.__lineCheckHelper(x,y,matrixB,turn,move,score)
            elif(matrixB[x][y] ==turn):
                return score > 0,score
            else:

                return False,score
        #if out of bounds
        except:
            return False,score


    #x and y are the values from the matrixB
    #matrixB is the board
    #turn is the person's turn to move ('W' or 'B')
    #score is the amount of chips to be fliped,if any
    #move is the direction that the search is attempting to go.
    def __isLegalHelper(self,x,y,matrixB,turn,move,score):
        if turn == "W":
            opp = "B"
        elif(turn == 'B'):
            opp = "W"

        x,y = self.__getCoordinate(x,y,move)

        try:
            if(matrixB[x][y] == opp):
                score+=1
                return self.__isLegalHelper(x,y,matrixB,turn,move,score)
            elif(matrixB[x][y] == turn):
                return score > 0
            else:
                return False
        #if out of bounds
        except:
            return False


    #returns the edited x and y coordinates for the function __isLegalHelper
    def __getCoordinate(self,x,y,move):
        if(move=='U'):
            x-=1
        elif(move == 'UR'):
            y+=1
            x-=1
        elif(move == 'R'):
            y+=1
        elif(move == 'DR'):
            x+=1
            y+=1
        elif(move == 'D'):
            x+=1
        elif(move == 'DL'):
            y-=1
            x+=1
        elif(move == 'L'):
            y-=1
        elif(move == 'UL'):
            x-=1
            y-=1
        return x,y


    def __makeMove(self,turn, matrix, x, y):
        matrix[x][y] = turn
        return matrix

    # flips the color of the chip in the x,y location of the
    # passed in matrix. returns resulting matrix
    def __flipChip(self,x,y,matrix):
        assert(matrix[x][y] != '-')

        if(matrix[x][y] == 'W'):
            matrix[x][y] = 'B'
        else:
            matrix[x][y] = 'W'

        return matrix

    # returns true if all spaces on the board are occupied
    # false otherwise. Big-O sucks.
    def __isFull(self, matrix):
        for i in range(1,9):
            for j in range(1,9):
                if(matrix[i][j] == '-'):
                    return False
        return True

#******Have not been able to test yet but the logic makes sense
    # returns true if there exists a space in which a player
    # can legally move. False otherwise.
    def __canMove(self, matrix,turn):
        for i in range(1,9):
            for j in range(1,9):
                if(matrix[i][j] == '-'):
                    if(self.isLegalMove(i,j,matrix,turn)):
                        return True
        return False
