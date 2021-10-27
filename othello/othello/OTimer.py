import threading
import time
import sys

'''
File:           OTimer.py
Authors:        Max Dulin, Jacob Krantz
Date:           5/7/2017
Description:    Control class for timer to be run in separate thread for
                the purpose of restraining an Othello AI to play a move
                in a given amount of time. Controlling and reading from this
                timer can be done by passing the timer object to other classes
                as necessary.

'''

class OTimer:

    # initialized with the length of time the AI gets to play,
    # the point in time the AI needs to rush,
    # the point of desperation.
    def __init__(self, turnTime, rushTime, quickTime):
        self.__AIturnTime    = turnTime
        self.__rushTime      = rushTime
        self.__QuickMoveTime = quickTime

        self.__stopTimer = False
        self.__isAIturn  = False
        self.__AIplayed  = False

        self.__isRushTime  = False
        self.__isQuickTime = False


    # creates a thread for the timer to run on
    def startThread(self):
        self.timeThread = threading.Thread(target=self.__timer, args=())
        self.timeThread.start()


    # ends timer loop, joins threads back together for game ending
    def joinThreads(self):
        self.__stopTimer = True
        self.timeThread.join()
        sys.exit()


    # boolean for whether or not the AI turn is complete
    def AIplayed(self, played):
        self.__AIplayed = played


    # boolean for whether or not the AI has begun playing
    def isAIturn(self, AIturn):
        self.__isAIturn = AIturn


    def isRushTime(self):
        return self.__isRushTime


    def isQuickMoveTime(self):
        return self.__isQuickTime

    # logic for repeating timers. Infinite loop for timer start check.
    def __timer(self):
        while(not self.__stopTimer):
            if(self.__isAIturn):
                self.__isAIturn = False
                #print "AI timer:"
                print("Waiting for AI move....")
                for i in range(self.__AIturnTime, 0, -1):
                    #print i
                    time.sleep(1)
                    if(i == 1):
                        pass
                        #print "AI did not play in time. "
                    elif(i == self.__rushTime):
                        self.__isRushTime = True
                    elif(i == self.__QuickMoveTime):
                        self.__isQuickTime

                    if(self.__AIplayed == True):
                        self.AIplayed(False)
                        self.__isRushTime = False
                        self.__isQuickTime = False
                        break

                self.__isRushTime = False # reset these at end of timer
                self.__isQuickTime = False
