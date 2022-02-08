from rules import Rules
#For discovering and understanding the mobility of the user
# and the opponents mobility
class MobilityH:

    def __init__(self,myToken,oppToken):
        self.__myToken = myToken
        self.__oppToken = oppToken
        self.__depth = 3
        self.rules = Rules()

    #returns the mobility score
    def getScore(self,matrix):
        return self.__getMobilityFactor(matrix)



    #######################
    #Private Section
    #####################

    
    # gets the maximum number of moves for the user
    #along with the maximum number of moves for the other player
    #It's an approximation for the opponent so I added an offset
    def __getMobilityFactor(self,matrix):
        userMoves = 0
        opponentMoves = 1
        for i in range(1,9):
            for j in range(1,9):
                if(self.rules.isLegalMove(i, j, matrix, self.__myToken)):
                    userMoves += 1

                if(self.rules.isLegalMove(i,j,matrix,self.__oppToken)):
                    opponentMoves +=1

        #not the best place to be at.So it's not a great result
        #this keep be improved if time for computation permits

        if(userMoves == opponentMoves-1):
            return .25/float(24)
        return (userMoves / float(opponentMoves))/float(24)

    # mobility factor is the number of moves normalized to
    # the maximum number of moves possible. Ranges from 0->1
    def __getUserMobilityFactor(self, matrix):
        movesPossible = 0
        for i in range(1,9):
            for j in range(1,9):
                if(self.rules.isLegalMove(i, j, matrix, self.__myToken)):
                    movesPossible += 1
        return movesPossible / float(15)

    #gets the oppenents mobility factor for a turn set
    def __getOppenentMobilityFactor(self,matrix):
        movesPossible = 0
        for i in range(1,9):
            for j in range(1,9):
                if(self.rules.isLegalMove(i, j, matrix, self.__oppToken)):
                    movesPossible += 1
        return movesPossible
