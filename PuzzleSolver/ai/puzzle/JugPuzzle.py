'''
Created on 16-Sep-2016
 
@author: khush
'''
import math
from ai.utility.Utility import gcdcount
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
        self.heuristicfn = dict()
        self.heuristicf = self.getEuclideanHeuristic
        self.nodesList = []        
        self.maxJug1 = maxsize[0]
        self.maxJug2 = maxsize[1]

        self.addGoalNode(goal)
        self.goalNode = self.getNode(goal, True)        
        self.startNode = self.getNode(initialsize)        
        
        
    def getChildNodes(self, cNode):

        childnodes = []
         
        if(len(cNode.childnodes) == 0):              
            ''' Fill Jug to Max '''
            if(cNode.jug[0] < self.maxJug1):
                tempnode = self.getNode((self.maxJug1, cNode.jug[1]))
                if tempnode is not cNode and tempnode is not self.startNode:
                    childnodes.append(tempnode)
            if(cNode.jug[1] < self.maxJug2):
                tempnode = self.getNode((cNode.jug[0], self.maxJug2))
                if(tempnode is not cNode and tempnode not in childnodes and tempnode is not self.startNode):
                    childnodes.append(tempnode)

            '''Transfer from 1 jug to Other'''    
            if(cNode.jug[1] < self.maxJug2 and cNode.jug[0] > 0):
                if(cNode.jug[0] + cNode.jug[1] >= self.maxJug2):
                    nc2 = self.maxJug2
                else:
                    nc2 = cNode.jug[0] + cNode.jug[1]
                nc1 = cNode.jug[0] - (nc2 - cNode.jug[1]);    
                tempnode = self.getNode((nc1, nc2))
                if(tempnode is not cNode and tempnode not in childnodes and tempnode is not self.startNode):
                    childnodes.append(tempnode)
     
            if(cNode.jug[0] < self.maxJug1 and cNode.jug[1] > 0):
                if(cNode.jug[0] + cNode.jug[1] >= self.maxJug1):
                    nc1 = self.maxJug1
                else:
                    nc1 = cNode.jug[0] + cNode.jug[1]
                nc2 = cNode.jug[1] - (nc1 - cNode.jug[0]);    
                tempnode = self.getNode((nc1, nc2))
                if(tempnode is not cNode and tempnode not in childnodes and tempnode is not self.startNode):
                    childnodes.append(tempnode)

            ''' Empty one Jug '''
            if(cNode.jug[0] > 0):
                tempnode = self.getNode((0, cNode.jug[1]))
                if(tempnode is not cNode and tempnode not in childnodes and tempnode is not self.startNode):
                    childnodes.append(tempnode)
                
            if(cNode.jug[1] > 0):
                tempnode=self.getNode((cNode.jug[0], 0))
                if(tempnode is not cNode and tempnode not in childnodes and tempnode is not self.startNode):
                    childnodes.append(tempnode)
             
            cNode.childnodes=childnodes
        return cNode.childnodes
      
    def getCost(self):
        return 1;
    def addGoalNode(self, nNodeTuple):        
        returnNode = Node(nNodeTuple,True)
        self.heuristicfn[returnNode]=0.0
        self.nodesList.append(returnNode)
        return returnNode    
      
    def getNode(self, nNodeTuple,isgoal=False):        
        nodeExists = False
        returnNode = None
         
        for node in self.nodesList:
            if node.jug == nNodeTuple:
                returnNode = node
                nodeExists = True  
         
        if(nodeExists != True):
            returnNode = Node(nNodeTuple,isgoal)
            self.heuristicf(returnNode)
            self.nodesList.append(returnNode)
       
        return returnNode    

    def getEuclideanHeuristic(self,nodev):
        dist=0.0
        dist = math.sqrt(math.pow(nodev.jug[0]-self.goalNode.jug[0],2) + math.pow(nodev.jug[1]-self.goalNode.jug[1],2))
        self.heuristicfn[nodev] = dist
        return dist

    def getDotProductHeuristic(self,nodev):
        dist = sum(map(abs,map(int.__mul__,nodev.jug,self.goalNode.jug)))
        self.heuristicfn[nodev] = dist
        return dist

    def getManhattanHeuristic(self,nodev=None):
        dist = (abs(nodev.jug[0]-self.goalNode.jug[0])) + abs((nodev.jug[1]-self.goalNode.jug[1]))
        self.heuristicfn[nodev] = dist
        return dist
        
    def getGcdHeuristic(self,nodev=None):
        dist = 0.0
        goal = max(self.goalNode.jug[0],self.goalNode.jug[1])
        if(nodev.isgoalState()):
            return 0
        if(nodev is self.startNode):
            return self.maxJug1 + self.maxJug2
        jug1 = nodev.jug[0]
        jug2 = nodev.jug[1]
        if(jug1 == goal or jug2 == goal):
            dist = 1
            if(jug1 != 0 or jug2 != 0):
                dist = dist +1
        if(jug1 != goal and jug2 != goal):
            dist = 1
            if(jug1 != 0 and jug2 != 0):
                dist = dist + gcdcount(gcdcount(jug1,jug2),goal)
            elif jug1 == 0 and jug2 != 0 :
                dist = dist + gcdcount(self.maxJug1,jug2)
            elif jug1 != 0 and jug2 == 0 :
#                 print gcdcount(self.maxJug2,jug1)
                dist = dist + gcdcount(self.maxJug2,jug1)
                
    
#         if(nodev.jug[0] == goal or nodev.jug[1]==goal):
#             dist = 1
#             if(nodev.jug[0] != 0 and nodev.jug[0] != goal):
#                 dist = gcdcount
#         if(nodev.jug[0] != goal and nodev.jug[1] != goal):
#             dist = 1
#             if(nodev.jug[0] != 0 and nodev.jug[1] != 0):
#                 dist = dist + gcdcount(nodev.jug[0],nodev.jug[1])
#             elif nodev.jug[1] == 0 and nodev.jug[0] != 0 :
#                 dist = dist + gcdcount(nodev.jug[0],self.maxJug2)
#             elif nodev.jug[0] == 0 :
#                 dist = dist + gcdcount(nodev.jug[1],self.maxJug1)
        
        self.heuristicfn[nodev] = dist
        return dist
               
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

    
    def getCost(self,tonode=None):
        return 1
