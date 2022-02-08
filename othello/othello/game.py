from Board import Board
from Board import Turn
from othelloAI import OthelloAI
from OTimer import OTimer
import copy
from random import randint

'''
TODO max
'''

class Game:
    #needs to have a few more beginning options for the game.
    # initialize board conditions to game specifications.
    def __init__(self):
        self.__turn = Turn('B')
        self.__player = ''
        self.__AItoken = ''
        self.board = self.__getInit()
        self.__AI = OthelloAI(self.__AItoken, self.__player)
        self.turnCount = 4 #60


    # plays a standard game of Othello with an option to adjust the length
    # of a turn. Param: turnTime, seconds as an int.
    def playGame(self, turnTime):
        self.OTimer = OTimer(turnTime, 2, 1)

        # create thread for the AI timer
        self.OTimer.startThread()

        while(not self.board.isGameOver()):

            if(self.__player == self.__turn.getTurn()):
                print("Player's turn to move.")
                self.__playerTurn()
            else:
                print("AI's turn to move.")
                self.__runAI()

            self.__confirmMove()
            self.__turn.flip()

        # Check to see if a flag should be displayed
        wscore, bscore = self.board.getScore()
        if(wscore > bscore):
            print("And you win!")
            f = open("/Othello/flag.txt", "r")
            print(f.read())
        else:
            print("Better luck next time!")
        self.OTimer.joinThreads()


    ############################
            #PRIVATE
    ############################

    def __getInit(self):
        board = Board('w','B', 'W', 'B')
        board.printBoard()
        self.__setPlayers()
        if(self.__player == 'B'):
            board = Board(self.__player, self.__AItoken, 'W', 'B')
        return board

    # asks the user who will be white or black between the player and the AI
    # repeats unitl proper input
    def __setPlayers(self):
        player = ''
        while(not self.__validSetPlayers(player)):
            #player = raw_input("Choose token for Player (W/B): ")
            player = 'W'
            self.__player = player.upper()
            if(player == 'W' or player == 'w'):
                print("Player set to be: 'W'")
                self.__AItoken = 'B'
                print("AI set to be: 'B'")
            elif(player == 'B' or player == 'b'):
                print("Player set to be: 'B'")
                self.__AItoken = 'W'
                print("AI set to be: 'W'")


    # checks input for setting the player tokens.
    # returns true for valid input.
    def __validSetPlayers(self, player):
        if(player == 'w' or player == 'W'):
            return True
        else:
            return (player == 'B' or player == 'b')


    # logic for a player's turn using terminal inputs.
    def __playerTurn(self):
        hasMoved = False
        while not hasMoved:
            self.board.getLegalMoves()

            if(self.board.can_move() == False):
                print("Player cannot move!")
                print("AI turn to move.")
                return 

            try:
                x = int(raw_input("Enter number: "))
                y = str(raw_input("Enter character: ")).upper()

                if(x > 8):
                    x = 999 # code for no moves

                hasMoved = self.board.move(x,y)

            except:
                print "Bad inputs; please give a number and letter where it is asked"


    # asks the user for move confirmation. In the event of a dispute,
    # the board gets set to the previous state, and the current turn gets
    # replayed.
    def __confirmMove(self):
        return 

        '''
        choice = raw_input("Confirm Move.\n'q' to quit, 'r' to revert board: ")
        if(choice == 'q'):
            self.OTimer.joinThreads()
        elif(choice == 'r'):
            print "Board set to prior state."
            self.board.revertBoard()
            self.board.printBoard()
            self.__turn.flip()
        '''

    # bot for making AI moves
    def __runAI(self):
        self.OTimer.AIplayed(False)
        self.OTimer.isAIturn(True)

        x,y = self.__AI.makeMove(copy.deepcopy(self.board), self.OTimer)
        if(x != 999):
            print("AI move: " + str(x) + " " + y)
        else:
            print("no moves available to AI")

        self.OTimer.AIplayed(True)  # stops timer
        self.board.move(x,y)
        self.OTimer.isAIturn(False)


# runs the base game of Othello
if(__name__ == "__main__"):
    game = Game()
    game.playGame(10)
