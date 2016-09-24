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
        self.getNode(initialsize)
        self.startNode = self.nodesList[0]
        self.goalNode = self.getNode(goal, True)
                 
             
    def getChildNodes(self, cNode):

        childnodes = []
         
        if(len(cNode.childnodes) == 0):              
            ''' Fill Jug to Max '''
            if(cNode.jug[0] < self.maxJug1):
                childnodes.append(self.getNode((self.maxJug1, cNode.jug[1])))
            if(cNode.jug[1] < self.maxJug2):
                childnodes.append(self.getNode((cNode.jug[0], self.maxJug2)))
            ''' Empty one Jug '''
            if(cNode.jug[0] > 0):
                childnodes.append(self.getNode((0, cNode.jug[1])))
            if(cNode.jug[1] > 0):
                childnodes.append(self.getNode((cNode.jug[0], 0)))
             
            '''Transfer from 1 jug to Other'''    
            if(cNode.jug[1] < self.maxJug2 and cNode.jug[0] > 0):
                if(cNode.jug[0] + cNode.jug[1] >= self.maxJug2):
                    nc2 = self.maxJug2
                else:
                    nc2 = cNode.jug[0] + cNode.jug[1]
                nc1 = cNode.jug[0] - (nc2 - cNode.jug[1]);    
                childnodes.append(self.getNode((nc1, nc2)))
     
            if(cNode.jug[0] < self.maxJug1 and cNode.jug[1] > 0):
                if(cNode.jug[0] + cNode.jug[1] >= self.maxJug1):
                    nc1 = self.maxJug1
                else:
                    nc1 = cNode.jug[0] + cNode.jug[1]
                nc2 = cNode.jug[1] - (nc1 - cNode.jug[0]);    
                childnodes.append(self.getNode((nc1, nc2)))
 
            cNode.childnodes=childnodes
        return cNode.childnodes
      
    def getCost(self):
        return 1;
          
#     def addNode(self, nNodeTuple, isgoal=False):
#         aNode = self.getNode(nNodeTuple)
#         if isgoal:
#             aNode.isgoal = True
#         return aNode    
             
    def getNode(self, nNodeTuple,isgoal=False):        
        nodeExists = False
        returnNode = None
         
        for node in self.nodesList:
            if node.jug == nNodeTuple:
                returnNode = node
                nodeExists = True  
         
        if(nodeExists != True):
            returnNode = Node(nNodeTuple,isgoal)
            self.nodesList.append(returnNode)
       
        return returnNode    

    def getEuclideanHeuristic(self):
        greedyfn = dict()
        dist=0.0
        for nodev in self.nodesList:
            dist = (math.pow(nodev.jug[0]-self.goalNode.jug[0],2)) + math.pow((nodev.jug[1]-self.goalNode.jug[1]),2)
            greedyfn[nodev] = dist
        return greedyfn

    def getManhattanHeuristic(self):
        greedyfn = dict()
        dist=0.0
        for nodev in self.nodesList:
            dist = (abs(nodev.jug[0]-self.goalNode.jug[0])) + abs((nodev.jug[1]-self.goalNode.jug[1]))
            greedyfn[nodev] = dist
        return greedyfn
        
               
class Node(object):
     
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

    def getChildNodes(self):
        return   self.childnodes
    
    def getCost(self):
        return 1
