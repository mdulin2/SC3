



class InteriorStability:


    def __init__(self,myToken,oppToken):
        self.__myToken = myToken
        self.__oppToken = oppToken

    #gets the score of the board for InteriorStability
    def getScore(self,matrix):
        return self.__countLines(matrix)


    def __countLines(self,matrix):
        myEdgeCount = 1
        totalCount = 0
        for i in range(1,9):
            for j in range(1,9):
                if(matrix[i][j] == self.__myToken):
                    myEdgeCount += self.__isEdgePiece(matrix,i,j)
                    totalCount+=1
                elif(matrix[i][j] == self.__oppToken):
                    totalCount+=1
        return ((myEdgeCount)/ float(300))/(float(totalCount))

    # returns 1 if it's an edge piece, false otherwise
    def __isEdgePiece(self,matrix,i,j):
        '''
        left = self.__checkLeft(matrix,i,j)
        top = self.__checkTop(matrix,i,j)
        right = self.__checkRight(matrix,i,j)
        bottom = self.__checkBottom(matrix,i,j)
        if(left or top or right or bottom):
            return 1
        else:
            return 0

        '''
        return self.__checkWhole(matrix,i,j)
    #checks the left side of the chip
    def __checkLeft(self,matrix,i,j):
        if(j == 8):
            return False

        if(matrix[i-1][j-1] != '-'):
            return False
        if(matrix[i-1][j] != '-'):
            return False
        if(matrix[i-1][j+1] != '-'):
            return False
        return True

    #checks the top for chips above it
    def __checkTop(self,matrix,i,j):
        #print i,j
        if(i == 8):
            return False

        if(matrix[i-1][j-1] != '-'):
            return False
        if(matrix[i][j-1] != '-'):
            return False
        if(matrix[i+1][j-1] != '-'):
            return False
        return True

    #checks the right side for chips
    def __checkRight(self,matrix,i,j):
        if(j == 8):
            return False
        if(i == 8):
            return False

        if(matrix[i+1][j-1] != '-'):
            return False
        if(matrix[i+1][j] != '-'):
            return False
        if(matrix[i+1][j+1] != '-'):
            return False
        return True

    #checks the bottom for chips above it
    def __checkBottom(self,matrix,i,j):
        if(i == 8):
            return False
        if(j == 8):
            return False

        if(matrix[i-1][j+1] != '-'):
            return False
        if(matrix[i][j+1] != '-'):
            return False
        if(matrix[i+1][j+1] != '-'):
            return False
        return True

    #check solid pieces
    def __checkWhole(self,matrix,i,j):
        if(j != 1 and matrix[i][j-1] == '-'):
            return False
        if(j != 8 and matrix[i][j+1] == '-'):
            return False
        if(i != 1 and matrix[i-1][j] == '-'):
            return False
        if(i != 8 and matrix[i+1][j] == '-' ):
            return False

        return True
