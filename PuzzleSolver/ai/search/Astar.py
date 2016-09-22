'''
Created on 16-Sep-2016

@author: khush
'''
from Queue import  PriorityQueue
import copy


class Astar:  # @IndentOk
    '''
      DFS  
    '''
def search(startnode,heuristicfn):
    try:
        visitedList=[]

        maxfrontiersize=0
        maxvisitedlistsize=0
        totalnumberofnodesgenerated=0
        cost=0
        frontierQueue=PriorityQueue()
        exploredQueue=PriorityQueue()
        if startnode is  None:
            return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost
        
        #frontierQueue.put(startnode)
        frontierQueue.put((heuristicfn[startnode],[startnode]))
        #Update Max Frontier Queue Size
        if(maxfrontiersize < frontierQueue.qsize()):
            maxfrontiersize = frontierQueue.qsize()
            
        #print "FQ : PUT : "+ startnode.printNode()
        while(frontierQueue.qsize() > 0):
            nodegen=[]
            nodegen = copy.copy(frontierQueue.get());
            #Empty Queue
                
            generatedNode = nodegen[1][len(nodegen[1])-1]
            parentNode = None    
            if(len(nodegen[1]) > 1):
                parentNode= nodegen[1][len(nodegen[1])-2]
            
            totalnumberofnodesgenerated = totalnumberofnodesgenerated + 1
            
            if generatedNode.isgoalState():
                    newlist = copy.copy(nodegen[1])
                    exploredQueue.put((nodegen[0],newlist))
                    
            else:

                if(maxvisitedlistsize < len(visitedList)):
                    maxvisitedlistsize = len(visitedList)

                currentdistance = 0
                previousheuristic=heuristicfn[generatedNode]
                
                
                #print generatedNode.childnodeswithcost.size()    
                for childnode in generatedNode.childnodes:
                    if childnode is not parentNode:
                        currentdistance = generatedNode.childnodeswithcost[childnode]
                        cost = heuristicfn[childnode] + nodegen[0] + currentdistance - previousheuristic
                        frontierQueue.put((cost,nodegen[1] + [childnode]))
                    
                #Update Max Frontier Queue Size
                if(maxfrontiersize < frontierQueue.qsize()):
                    maxfrontiersize = frontierQueue.qsize()
                    #print "FQ : PUT : "+ childnode.printNode()

        final = exploredQueue.get()
        cost = final[0]
        
        return final[1],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost                  
    finally:
        abc=10
        
    return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost      