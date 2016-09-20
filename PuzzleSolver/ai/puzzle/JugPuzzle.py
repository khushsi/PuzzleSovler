'''
Created on 16-Sep-2016
 
@author: khush
'''
import math
 
class JugPuzzle(object):
    '''
    classdocs
    '''
        
    def __init__(self, inputArray):
        '''
        Constructor
        '''
        maxsize = eval(inputArray[1])
        initialsize = eval(inputArray[2])
        goal = eval(inputArray[3])
         
        self.nodesList = []        
        self.maxJug1 = maxsize[0]
        self.maxJug2 = maxsize[1]
        self.addJugNode(initialsize)
        self.startNode = self.nodesList[0]
        self.goalNode = self.addJugNode(goal, True)
        self.createChildNodes();
             
                              
    def createChildNodes(self):
        allchild = False
#         ic = 0
        while(allchild != True):
#             print len(self.nodesList)
#             ic=ic+1 
#             print ic
            allchild = True
            for i in self.nodesList:
                if(not i.isgoal and len(i.childnodes) == 0):
                    allchild = False
                    i.setchildNodes(self.getChildNodes(i))
                 
             
    def getChildNodes(self, cJugNode):
         
        childnodes = []
         
        ''' Fill Jug to Max '''
        if(cJugNode.jug[0] < self.maxJug1):
            childnodes.append(self.getNode((self.maxJug1, cJugNode.jug[1])))
        if(cJugNode.jug[1] < self.maxJug2):
            childnodes.append(self.getNode((cJugNode.jug[0], self.maxJug2)))
        ''' Empty one Jug '''
        if(cJugNode.jug[0] > 0):
            childnodes.append(self.getNode((0, cJugNode.jug[1])))
        if(cJugNode.jug[1] > 0):
            childnodes.append(self.getNode((cJugNode.jug[0], 0)))
         
        '''Transfer from 1 jug to Other'''    
        if(cJugNode.jug[1] < self.maxJug2 and cJugNode.jug[0] > 0):
            if(cJugNode.jug[0] + cJugNode.jug[1] >= self.maxJug2):
                nc2 = self.maxJug2
            else:
                nc2 = cJugNode.jug[0] + cJugNode.jug[1]
            nc1 = cJugNode.jug[0] - (nc2 - cJugNode.jug[1]);    
            childnodes.append(self.getNode((nc1, nc2)))
 
        if(cJugNode.jug[0] < self.maxJug1 and cJugNode.jug[1] > 0):
            if(cJugNode.jug[0] + cJugNode.jug[1] >= self.maxJug1):
                nc1 = self.maxJug1
            else:
                nc1 = cJugNode.jug[0] + cJugNode.jug[1]
            nc2 = cJugNode.jug[1] - (nc1 - cJugNode.jug[0]);    
            childnodes.append(self.getNode((nc1, nc2)))
 
             
        return childnodes
      
    def addJugNode(self, nNodeTuple, isgoal=False):
        aNode = self.getNode(nNodeTuple)
        if isgoal:
            aNode.isgoal = True
        return aNode    
             
    def getNode(self, nNodeTuple):        
        nodeExists = False
        returnNode = None
         
        for node in self.nodesList:
            if node.jug[0] == nNodeTuple[0] and node.jug[1] == nNodeTuple[1]:
                returnNode = node
                nodeExists = True  
         
        if(nodeExists != True):
            returnNode = JugNode(nNodeTuple)
            self.nodesList.append(returnNode)
       
        return returnNode    

    def getGreedyHeuristic(self):
        greedyfn = dict()
        dist=0.0
        for nodev in self.nodesList:
            dist = (math.pow(nodev.jug[0]-self.goalNode.jug[0],2)) + math.pow((nodev.jug[1]-self.goalNode.jug[1]),2)
            greedyfn[nodev] = dist
        return greedyfn
        
               
class JugNode(object):
     
    def __init__(self, jugvalues=(0, 0), isgoal=False):
        self.jug = jugvalues  
        self.isgoal = isgoal
        self.childnodes = []
        self.childnodeswithcost = dict()
         
    def setchildNodes(self, childnodes=[]):
        self.childnodes = childnodes
        for i in childnodes:
            self.childnodeswithcost[i] = 1
             
    def printNode(self):
        return ("(" + str(self.jug[0]) + ", " + str(self.jug[1]) + ")")    
             
    def isgoalState(self):
        return self.isgoal
    #Calculate greedyHeuristic for Problem
