from GrabSides import GrabSides

#################
#Needs some major work done to it!!!
#Playing on wedges, giving up corners is terrible.
#This needs to be much better
##################

#This calculates the values of being on specific spots on the board
class PositionH:

    def __init__(self,myToken,oppToken,positionScore):
        self.__myToken = myToken
        self.__oppToken = oppToken
        self.__positionScores = positionScore
        self.GrabSides = GrabSides(myToken,oppToken)
        self.__depth = 3

    #sets the depth of the Heuristic
    def setDepth(self,num):
        self.__depth = num

    #returns the position function score
    def getScore(self,matrix,path):
        myTotalScore,oppTotalScore,myChips,oppChips = self.__getPositionFactor(matrix,path)
        #altScore = self.alterations(matrix)
        myTotalScore =  myTotalScore / float(myChips * 44.675 * 2)
        oppTotalScore = oppTotalScore / float(oppChips * 44.675)
        if(oppTotalScore == 0):
            finalScore = (myTotalScore / 1)
        else:
            finalScore = (myTotalScore / float(oppTotalScore))

        finalScore / (float(15))
        return finalScore


    ######################
    #PRIVATE
    ######################


    # position factor judges the position the AI is in. Analyzes
    # corners, edges. How to judge against bad spaces? Cannot get this to work the way I want!
    def __getPositionFactor(self, matrix,path):
        myTotalScore = 0
        oppTotalScore = 0
        myCount = 1
        oppCount = 1
        turnCount = self.__getMovedPlayed(matrix)
        for i in range(1,9):
            for j in range(1,9):
                if(matrix[i][j] == self.__myToken):
                    value = self.__positionScores[i-1][j-1]
                    myCount+=1
                    if (value > 90):
                        myTotalScore += 50000
                        #oppTotalScore = oppTotalScore - 1000
                    #might need to alter this in order to check if the rest is okay
                    elif(self.__isViable(path,i,j,matrix)):
                        myTotalScore += 600
                    elif(self.__isWedgeSquare(i,j,matrix,self.__myToken)):
                        myTotalScore = myTotalScore -600000
                    elif(value < 11):
                        #need to really hate on this
                        myTotalScore = myTotalScore - 14000
                    else:
                        myTotalScore+= 4 *value

                elif(matrix[i][j] == self.__oppToken):
                    value = self.__positionScores[i-1][j-1]
                    oppCount +=1
                    if (value > 90):
                        oppTotalScore += 9000
                        myTotalScore =myTotalScore - 150000
                    elif(self.__isViable(path,i,j,matrix)):
                        oppTotalScore += 300
                    elif(self.__isWedgeSquare(i,j,matrix,self.__oppToken)):
                        oppTotalScore = oppTotalScore - 400
                    #elif not sure if I want to check for the Xsquares or not
                    else:
                        oppTotalScore+= 4 * value
        value = self.GrabSides.RunCheck(matrix,self.__myToken,self.__oppToken,path, self.__depth)
        myTotalScore += value
        #value = self.GrabSides.RunCheck(matrix,self.__myToken,self.__oppToken,path, self.__depth)
        #oppTotalScore +=value

        #instead of dividing here I should do something else
        if(oppTotalScore <= 0):
            oppTotalScore = 1/10
        #value = self.GrabSides.RunCheck(matrix,self.__myToken,self.__oppToken)
        #if(value > 0):
            #oppTotalScore+= 3000
        if(myTotalScore < 0):
            myTotalScore * oppTotalScore

        return myTotalScore,oppTotalScore,myCount,oppCount

    #marks whether a move is viable based on the standards of having a corner played already
    def __isViable(self,path,i,j,matrix):

        if((i ==2 and j ==1)or (i ==2 and j ==2)or (i ==1 and j ==2)):
            #if my token is the corner
            if(matrix[1][1] == self.__myToken and len(path) == self.__depth):
                #if not in path then just this flip is good; it will flip others around it
                if([1,1] in path and [i,j] in path):

                    #if contains the Xsquare as a prediction, then don't use it
                    #or if that's the move choosen
                    if(path.index([1,1]) < path.index([i,j])):
                        return True
                    else:
                        return False
                #if the matrix has the corner but doesn't have the other pieces in the path.
                #Good
                else:
                    return True
            else:
                return False

        elif(((i == 1 and j == 7) or (i ==2 and j ==7)or (i ==2 and j ==8))):
            if(matrix[1][8] == self.__myToken and len(path) == self.__depth):
                if([1,8] in path and [i,j] in path):
                    if(path.index([1,8]) < path.index([i,j])):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False
        elif(((i == 7 and j == 1) or (i ==7 and j ==2)or (i ==8 and j ==2))):
            if(matrix[8][1] == self.__myToken and len(path) == self.__depth):

                if([8,1] in path and [i,j] in path):
                    if(path.index([8,1]) < path.index([i,j])):
                        return True
                    else:
                        return False
                else:
                    return True
            return False
        elif(((i == 8 and j == 7) or (i == 7 and j ==8)or (i ==7 and j ==7))):
            if(matrix[8][8] == self.__myToken and len(path) == self.__depth):
                if([8,8] in path and [i,j] in path):
                    if(path.index([8,8]) < path.index([i,j])):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False

        return False

    #Gets if the current play is a wedge move
    def __isWedgeSquare(self,i,j,matrix,Token):
        if(i == 2 and j == 2):
            if(matrix[1][1] != Token):
                if(matrix[2][2] == Token):
                    return True
        elif(i == 2 and j == 7):
            if(matrix[1][8] != Token):
                if(matrix[2][7] == Token):
                    return True
        elif(i == 7 and j == 2):
            if(matrix[8][1] != Token):
                if(matrix[7][2] == Token):
                    return True
        elif(i == 7 and j == 7 ):
            if(matrix[8][8] != Token):
                if(matrix[7][7] == Token):
                    return True
        return False

    #return true if the value is just outside the corner on the sides
    #return false otherwise
    def __isXSquare(self,matrix,token):
        if(matrix[1][1] != Token):
            if(matrix[1][2] == Token):
                return True
            if(matrix[2][1] == Token):
                return True
        if(matrix[1][8] != Token):
            if(matrix[1][7] == Token):
                return True
            if(matrix[2][8] == Token):
                return True

        if(matrix[8][1] != Token):
            if(matrix[7][1] == Token):
                return True
            if(matrix[8][2] == Token):
                return True

        if(matrix[8][8] != Token):
            if(matrix[7][8] == Token):
                return True
            if(matrix[8][7] == Token):
                return True
        return False
    # counts all played turns on the board by looking for occupied spaces.
    def __getMovedPlayed(self, matrix):
        movesPlayed = 0
        for i in range(1,9):
            for j in range(1,9):
                if(matrix[i][j] != '-'):
                    movesPlayed += 1
        return movesPlayed
