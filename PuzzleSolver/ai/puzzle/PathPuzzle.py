'''
Created on 16-Sep-2016

@author: khush
'''
from ai.puzzle.LocationNode import LocationNode
import math


class PathPuzzle(object):
    '''
    Path Puzzle
    '''
           
    def __init__(self,inputArray):
        '''
        Constructor
        '''
        self.nodesList=[]
        inputnodelist = eval(inputArray[1])
        for i in inputnodelist:
            self.addNode(i[0],(i[1],i[2]))
        
        self.startNode =  self.getNode(str(inputArray[2].replace('"', '')))
        
        self.goalNode = self.getNode(inputArray[3].replace('"', ''))
        
        if(self.goalNode):
            self.goalNode.isgoal= True
        self.createChildNodes(inputArray[4:]);
            
                             
    def createChildNodes(self,inputArray):        
        for i in inputArray:
            edge = eval(i)
            node1 = self.getNode(edge[0])
            node2 = self.getNode(edge[1])
            distance = edge[2]
            
            node1.childnodes.append(node2)
            node2.childnodes.append(node1)
            
            node1.childnodeswithcost[node2]=distance
            node2.childnodeswithcost[node1]=distance
    
    def getChildNodes(self,cNode):        
        return cNode.childnodes
    
    def addNode(self,LocationName, location, isgoal=False):        
        
        returnNode = LocationNode(LocationName, location, isgoal=False)
        self.nodesList.append(returnNode)
        return returnNode    
       
    def getNode(self,LocationName):      
        
        for i in self.nodesList:
            if(i.name == LocationName):
                return i
        return None
    
    #Calculate greedyHeuristic for Problem
    def getEuclideanHeuristic(self):
        greedyfn = dict()
        dist=0.0
        for nodev in self.nodesList:
            dist = math.sqrt(((math.pow(nodev.location[0]-self.goalNode.location[0],2)) + math.pow((nodev.location[1]-self.goalNode.location[1]),2)))
            greedyfn[nodev] = dist
        return greedyfn
        
    def getManhattanHeuristic(self):
        greedyfn = dict()
        dist=0.0
        for nodev in self.nodesList:
            dist = abs(nodev.location[0]-self.goalNode.location[0]) + abs(nodev.location[1]-self.goalNode.location[1])
            greedyfn[nodev] = dist
        return greedyfn
        
    
    