'''
Team Leader: Jacob Krantz
Developer 1: Max Dulin
Assignment:  Othello
Date:        4/18/17

How to run:
    - enter on command line
        'python abPrune.py'
    - result
        nodes visited are printed out to console
'''

class ABPrune:

    # initialize datatypes
    def __init__(self):
        self.__data = {}
        self.__graph = {}
        self.__inorderVisit = []


    # populate graph and data to a given state
    def initGraph(self,graphIn,dataIn):
        self.__graph = graphIn
        self.__data = dataIn


    #node data = [value, isMax, parentChar, alpha, beta,x,y,token]
    # performs a depth-first traversal and returns the visited list
    # start is the node name to start with
    def depth_first(self,start):
        visited = []
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                children = self.__graph[vertex]
                children.reverse()
                for item in children:
                    if item not in visited:
                        stack.append(item)
        return visited


    # performs an in-order taversal and returns the visited list
    def minimax(self,start):
        children = self.__graph[start]
        nodeValue = self.__data[start][0]
        isMax     = self.__data[start][1]
        par       = self.__data[start][2]
        x         = self.__data[start][5]
        y         = self.__data[start][6]

        if par != "none":
            parAlpha =  self.__data[par][3]
            parBeta =   self.__data[par][4]

        # if is leaf node
        if len(children) == 0:
            self.__inorderVisit.append(start)

            if(isMax): # if is max
                if parBeta > nodeValue:
                    self.__data[par][0] = nodeValue # set par value
                    self.__data[par][4] = nodeValue # set par beta

                    self.__data[par][5] = x
                    self.__data[par][6] = y


            else: # is min
                if parAlpha < nodeValue:
                    self.__data[par][0] = nodeValue # set par value
                    self.__data[par][3] = nodeValue # set par alpha
                    self.__data[par][5] = x
                    self.__data[par][6] = y
            return

        else:
            # visit left first
            self.minimax(children[0])

            # visit itself
            self.__inorderVisit.append(start)

            # visit all the rest if not pruned
            if len(children) > 1:

                for i in range(1,len(children)):
                    # bubble down alpha and beta
                    self.__data[children[i]][3] = self.__data[start][3] # child alpha set to node alpha
                    self.__data[children[i]][4] = self.__data[start][4] # child beta set to node beta

                    if isMax:
                        if(self.__data[start][0] < self.__data[start][4]):  # if node value < node beta
                            self.minimax(children[i])

                    else: # is min
                        if(self.__data[start][0] > self.__data[start][3]):  # if node value > node alpha
                            self.minimax(children[i])

            # bubble up the bumbershoot
            nodeValue = self.__data[start][0]
            if par != "none":
                if(isMax): # if is max
                    if parBeta > nodeValue:
                        self.__data[par][0] = nodeValue # set par value
                        self.__data[par][4] = nodeValue # set par beta
                        self.__data[par][5] = x
                        self.__data[par][6] = y


                else: # is min
                    if parAlpha < nodeValue:
                        self.__data[par][0] = nodeValue # set par value
                        self.__data[par][3] = nodeValue # set par alpha
                        self.__data[par][5] = x
                        self.__data[par][6] = y

        return self.__inorderVisit


    #after the spanning of the tree has been done this returns the best x and y value to
    #place on the board
    def getBestPlace(self):
        return self.__data[0][5],self.__data[0][6]
