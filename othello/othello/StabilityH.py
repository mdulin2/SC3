

#Determines the stability of the user. Checks for corners, isoceles triangles
# in corners and the edges if the corner has been taken by the user.
class StabilityH:

    def __init__(self,myToken,oppToken):
        self.__myToken = myToken
        self.__oppToken = oppToken


    #returns the total user stability score
    def getScore(self,matrix):
        return self.__getUserStability(matrix)

    #################
    #PRIVATE
    #################

    
    #checks the stability of the players move
    def __getUserStability(self,matrix):
        stabCount = 1
        #checks the top left
        stabCount+=self.__getEdgeStability(matrix,self.__myToken)
        if(self.__myToken == matrix[1][1]):
            stabCount +=1
            stabCount += self.__triangles(matrix,0)

        #checks the bottom right corner
        if(self.__myToken == matrix[8][8]):
            stabCount +=1
            stabCount += self.__triangles(matrix,1)
        #checks the top right corner
        if(self.__myToken == matrix[1][8]):
            stabCount +=1
            stabCount += self.__triangles(matrix,2)
        #checks the bottom left corner
        if(self.__myToken == matrix[8][1]):
            stabCount +=1
            stabCount += self.__triangles(matrix,3)

        stabCount+= self.__getCorners(matrix,self.__myToken)
        return stabCount/float(100)


    #gets the amount of corners for each player
    def __getCorners(self,matrix,token):
        myCorner = 0
        oppCorner = 0
        if(matrix[1][1] == self.__myToken):
            myCorner+=1
        if(matrix[1][1] == self.__oppToken):
            oppCorner+=1
        if(matrix[1][8] == self.__myToken):
            myCorner+=1
        if(matrix[1][8] == self.__oppToken):
            oppCorner+=1
        if(matrix[8][1] == self.__myToken):
            myCorner+=1
        if(matrix[8][1] == self.__oppToken):
            oppCorner+=1
        if(matrix[8][8] == self.__myToken):
            myCorner+=1
        if(matrix[8][8] == self.__oppToken):
            oppCorner+=1
        return myCorner #,oppCorner


    #returns the number of __stable chips on the board
    def __getEdgeStability(self,matrix,token):
        count = 0
        if(matrix[1][1] == token):
            count += self.__stableRight(matrix,token,0)
            count += self.__stableBottom(matrix,token,0)
            count+=1
        if(matrix[1][8] == token):
            count += self.__stableLeft(matrix,token,0)
            count += self.__stableBottom(matrix,token,1)
            count+=1
        if(matrix[8][1] == token):
            count += self.__stableTop(matrix,token,0)
            count += self.__stableRight(matrix,token,1)
            count+=1
        if(matrix[8][8] == token):
            count += self.__stableLeft(matrix,token,1)
            count += self.__stableTop(matrix,token,1)
            count+=1
        return count

    #checks the stability of left (going to the left)
    def __stableLeft(self,matrix,token,direction):
        count = 0
        if(direction == 0):
            for i in range(7,2,-1):
                if(matrix[1][i] == token):
                    count+=1
                else:
                    return count
        else:
            for i in range(7,2,-1):
                if(matrix[8][i] == token):
                    count+=1
                else:
                    return count
        return count

    #Checking the stability of the right side stability (going to the right)
    def __stableRight(self,matrix,token,direction):
        count = 0
        if(direction == 0):
            for i in range(2,9):
                if(matrix[1][i] == token):
                    count+=1
                else:
                    return count
        else:
            for i in range(2,9):
                if(matrix[8][i] == token):
                    count+=1
                else:
                    return count
        return count

    #checks the stability of the top (going on)
    def __stableTop(self,matrix,token,direction):
        count = 0
        if(direction == 0):
            for i in range(7,1,-1):
                if(matrix[i][1] == token):
                    count+=1
                else:
                    return count
        else:
            for i in range(7,1,-1):
                if(matrix[i][8] == token):
                    count+=1
                else:
                    return count
        return count

    #checks the stability of the bottom (going down)
    def __stableBottom(self,matrix,token,direction):
        count = 0
        if (direction == 0):
            for i in range(2,8):
                if(matrix[i][1] == token):
                    count+=1
                else:
                    return count
        else:
            for i in range(2,8):
                if(matrix[i][8] == token):
                    count+=1
                else:
                    return count
        return count

    #gets the stability of every corner(only one layer deep)
    def __triangles(self,matrix,typeCheck):
        count = 0
        #gets the stability of the top left corner
        if(typeCheck == 0):
            if(self.__myToken == matrix[2][1]):
                count +=1
            if(self.__myToken == matrix[1][2]):
                count +=1
            if(count ==2):
                count +=3

        #checks the bottom right corner
        elif (typeCheck == 1):
            if(self.__myToken == matrix[7][8]):
                count +=1
            if(self.__myToken == matrix[8][7]):
                count +=1
            if (count == 2):
                count +=3
        #checks the top right corner
        elif (typeCheck == 2):
            if(self.__myToken == matrix[1][7]):
                count +=1
            if(self.__myToken == matrix[2][8]):
                count +=1
            if (count == 2):
                count +=3

        #checks the bottom left corner
        elif (typeCheck == 3):
            if(self.__myToken == matrix[7][1]):
                count +=1
            if(self.__myToken == matrix[8][2]):
                count +=1
            if (count == 2):
                count +=3
        return count
