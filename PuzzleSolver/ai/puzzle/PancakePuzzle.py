'''
Created on 16-Sep-2016
 
@author: khush
'''
from Queue import Queue, LifoQueue
import copy
import math
from xml.dom.minicompat import NodeList


class PancakePuzzle(object):
    '''
    classdocs
    '''
        
    def __init__(self, inputArray):
        '''
        Constructor
        '''
        initialstate = list(eval(inputArray[1]))
        
        self.numberofpancakes = len(initialstate)
        goal = list(range(1,self.numberofpancakes+1))
         
        self.nodesList = []        

        self.addNode(initialstate)
        self.startNode = self.nodesList[0]
        self.goalNode = self.addNode(goal, True)
        for i in self.nodesList:
            self.getChildNodes(i)       
             
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
                childnodes.append(self.addNode(copy.copy(newnode)))
            cNode.setchildNodes(childnodes)
        return cNode.childnodes
      
    def addNode(self, nNodeTuple, isgoal=False):
        aNode = self.getNode(nNodeTuple)
        if isgoal:
            aNode.isgoal = True
        return aNode    
             
    def getNode(self, nNodeTuple):        
        nodeExists = False
        returnNode = None
         
        for node in self.nodesList:
            if node.jug == nNodeTuple: 
                returnNode = node
                nodeExists = True               
                
        if(nodeExists != True):            
            returnNode = Node(nNodeTuple)
#             print "node created " + returnNode.printNode()
            self.nodesList.append(returnNode)
       
        return returnNode    

    def getEuclideanHeuristic(self):
        greedyfn = dict()
        dist=0.0        
        for nodev in self.nodesList:
            list1 = [abs(number) for number in nodev.jug]
            list2 = self.goalNode.jug
            diff =  [abs(list1[i]-list2[i]) for i in range(self.numberofpancakes)]
            dist = len([x for x in nodev.jug if x < 0])  + sum(diff)
            greedyfn[nodev] = dist
        return greedyfn

    def getPancakeHeuristic(self):
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
    #Calculate greedyHeuristic for Problem