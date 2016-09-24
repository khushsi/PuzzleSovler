'''
Created on 16-Sep-2016
 
@author: khush
'''
from Queue import Queue, LifoQueue
import copy
import math


class PancakePuzzle(object):
    '''
    classdocs
    '''
        
    def __init__(self, inputArray):
        '''
        Constructor
        '''
        self.nodesList = []        
        initialstate = list(eval(inputArray[1]))
        self.heuristicfn = dict()
        self.heuristicf = self.getPancakeHeuristic
        
        self.numberofpancakes = len(initialstate)
        goal = list(range(1,self.numberofpancakes+1))
        self.goalNode = self.addGoalNode(goal)        
        self.startNode =self.getNode(initialstate) 
        
             
    def getChildNodes(self, cNode):
        childnodes=[]
        if(len(cNode.childnodes) == 0):
            newnode=[]  
            count = 0
            prevnode = copy.copy(cNode.jug)
            for i in range(self.numberofpancakes):           
                newnode = []
                if(count == 0):
                    newnode = [(-1)*prevnode[count]]  +prevnode[count+1:]
                elif(count < self.numberofpancakes):
                    newnode = [(-1)*prevnode[count]] + prevnode[0:count] +prevnode[count+1:]
                else:
                    newnode = [(-1)*prevnode[count]] + prevnode[0:count-1] 
                prevnode = newnode
                count = count +1
                childnodes.append(self.getNode(copy.copy(newnode)))
            cNode.setchildNodes(childnodes)
        return cNode.childnodes
      
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
            self.nodesList.append(returnNode)
       
        return returnNode    

    def getPancakeHeuristic(self,nodev):
        list1 = nodev.jug
        list2 = self.goalNode.jug
        diff =  map(abs,map(int.__sub__, list1,list2))
        dist = abs(len([x for x in nodev.jug if x < 0])  + sum(diff))
        return dist

    def getflipsHeuristic(self,nodev):
        list1 = nodev.jug
        list2 = self.goalNode.jug
        diff =  map(abs,map(int.__sub__, list1,list2))
        dist = abs(len([x for x in nodev.jug if x < 0]))
        return dist

    def getdistpanHeuristic(self,nodev):
        list1 = nodev.jug
        list2 = self.goalNode.jug
        diff =  map(abs,map(int.__sub__, list1,list2))
        dist = abs(len([x for x in nodev.jug if x < 0]) - sum(diff))
        return dist

    def getEuclideanHeuristic(self,nodev):
        dist =round(math.sqrt(sum([ math.pow(x,2) for x in map(abs,map(int.__sub__,nodev.jug,self.goalNode.jug))])))
        return dist

    def getManhattanHeuristic(self,nodev):
        dist = sum(map(abs,map(int.__sub__,nodev.jug,self.goalNode.jug)))
        self.heuristicfn[nodev] = dist
        return dist
    
    def getDotProductHeuristic(self,nodev):
        dist = sum(map(abs,map(int.__mul__,nodev.jug,self.goalNode.jug)))
        self.heuristicfn[nodev] = dist
        return dist

    def getCountWrongLocation(self,nodev):
        dist = sum(map(abs,map(int.__eq__,nodev.jug,self.goalNode.jug)))
        self.heuristicfn[nodev] = dist
        return dist
               
class Node(object):
     
    def __init__(self, jugvalues, isgoal=False):
        self.jug = jugvalues  
        self.isgoal = isgoal
        self.childnodes = []
        self.childnodeswithcost = dict()
         
    def setchildNodes(self, childnodes=[]):
        self.childnodes = childnodes
        for i in childnodes:
            self.childnodeswithcost[i] = 1
             
    def printNode(self):
        return str(self.jug)    

    def getChildNodes(self):
        return   self.childnodes
             
    def isgoalState(self):
        return self.isgoal
    
    def getCost(self,tonode=None):
        return 1
    #Calculate greedyHeuristic for Problem