import copy
from rules import Rules
import math
from GrabSides import GrabSides
from PositionH import PositionH
from MobilityH import MobilityH
from StabilityH import StabilityH
from InteriorStability import InteriorStability
'''
Filename:   Heuristic.py
Authors:    Max Dulin,Jacob Krantz
Date:       4/26/17
Description:
    calculates the value of a board state for a player of Othello.
    Initialized with the token to be analyzed for and called by
    function 'calculateValue'.
Heuristic factors:
- chip ratio
- mobility
- position
- stability
- particular cases
- corners
- Xsquares and Wedges
'''

class Heuristic:

    # initializes necessary data structures
    def __init__(self, myToken,oppToken):
        self.rules = Rules()
        self.__oppToken = oppToken
        self.__myToken   = myToken
        self.__depth = 3

        self.__positionScores   = [[95,10,80,75,75,80,10,95],
                                    [10,10,45,45,45,45,10,10],
                                    [65,40,70,50,50,70,40,65],
                                    [60,40,40,40,40,40,40,60],
                                    [60,40,40,40,40,40,40,60],
                                    [65,40,70,50,50,70,40,65],
                                    [10,10,45,45,45,45,10,10],
                                    [95,10,65,60,60,65,10,95]]
        self.PositionH = PositionH(myToken,oppToken,self.__positionScores)
        self.MobilityH = MobilityH(myToken,oppToken)
        self.StabilityH = StabilityH(myToken,oppToken)
        self.InteriorStability = InteriorStability(myToken,oppToken)



    # calculates the value of a given board state.
    # higher score return, the better the position.
    # factors of success:
    # - evaporation
    # - chip ratio
    # - mobility
    # - position
    # **option: add a multiplier in front of each to adjust their
    #       individual affect on the score. All are currently
    #       normalized to 0 < score < 1
    def calculateValue(self, matrix,path):
        #print path
        movesPlayed = self.getMovesPlayed(copy.deepcopy(matrix))
        score = 1
        self.PositionH.setDepth(self.__depth)

        if(movesPlayed < 17):
            stabVal = 1 # don't think i need this here
            posVal = 1
            mobilityVal = 1
            edge = 1
            #edge = self.InteriorStability.getScore(matrix)
            posVal = self.PositionH.getScore(copy.deepcopy(matrix),path)
            mobilityVal = self.MobilityH.getScore(copy.deepcopy(matrix))

            score = self.__getWeightStage1(stabVal,mobilityVal,posVal,edge)
        elif(movesPlayed >= 17 and movesPlayed <=58):
            #edge = self.InteriorStability.getScore(matrix)
            edge = 1
            stabVal = self.StabilityH.getScore(copy.deepcopy(matrix))
            mobilityVal = self.MobilityH.getScore(copy.deepcopy(matrix))
            posVal = self.PositionH.getScore(copy.deepcopy(matrix),path)
            score = self.__getWeightStage2(stabVal,mobilityVal,posVal,edge)

        else:
            #edge = self.InteriorStability.getScore(matrix)
            edge = 1
            chipCount = self.__getChipRatio(movesPlayed, copy.deepcopy(matrix))
            stabVal = self.StabilityH.getScore(copy.deepcopy(matrix))
            mobilityVal = self.MobilityH.getScore(copy.deepcopy(matrix))
            posVal = self.PositionH.getScore(copy.deepcopy(matrix),path)
            score = self.__getWeightStage3(stabVal,mobilityVal,posVal,chipCount,edge)
        #print '%.25f' % score
        return score

    #---------------------
    #  PRIVATE FUNCITONS
    #---------------------


    # counts all played turns on the board by looking for occupied spaces.
    def getMovesPlayed(self, matrix):
        movesPlayed = 0
        for i in range(1,9):
            for j in range(1,9):
                if(matrix[i][j] != '-'):
                    movesPlayed += 1
        return movesPlayed

    #Would give the weights for each of the values put in for stage 1
    def __getWeightStage1(self,stabVal,mobilityVal,posVal,edge):
        #print posVal
        stabVal = stabVal * .20
        mobilityVal = mobilityVal *.40
        posVal = posVal * .40
        #edge = edge * .01
        score = stabVal * mobilityVal * posVal
        return score

    #Would give the weights for each of the values for stage 2
    def __getWeightStage2(self,stabVal,mobilityVal,posVal,edge):
        stabVal = stabVal * .30
        mobilityVal = mobilityVal *.75
        posVal = posVal * .50
        #edge = edge * .01
        score = stabVal * mobilityVal * posVal
        return score

    #Gives the weights of the last stage of the game
    def __getWeightStage3(self,stabVal,mobilityVal,posVal,chipCount,edge):
        stabVal = stabVal * .30
        mobilityVal = mobilityVal *.20
        posVal = posVal * .1
        chipCount = chipCount * .9
        #edge = edge * .01
        score = chipCount * mobilityVal * posVal
        return score

    #sets the depth of the heuristic
    def setDepth(self,num):
        self.__depth = num

    ###############################
    #Rating the amount of chips on the board
    ###############################

    # returns the ratio of chips on the board that are myToken.
    def __getChipRatio(self, movesPlayed, matrix):
        myCount = 0
        oppCount = 3
        for i in range(0,9):
            for j in range(1,9):
                if(matrix[i][j] == self.__myToken):
                    myCount += 1
                elif(matrix[i][j] == self.__oppToken):
                    oppCount+=1

        return (myCount/float(oppCount)) / float(movesPlayed)


    # inverse of chip ratio: at beginning of game, give away
    # more spaces to improve end game chances
    def __evaporation(self,movesPlayed,matrix):
        return 1 / float(self.__getChipRatio(movesPlayed,matrix))
