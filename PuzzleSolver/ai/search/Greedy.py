'''
Created on 16-Sep-2016

@author: khush
'''
from Queue import  PriorityQueue
import copy


class Greedy:  # @IndentOk
    '''
      DFS Greedy  
    '''
def search(cPuzzle):
    try:
        heuristicfn = cPuzzle.heuristicfn
        parentNodes = []
        visitedList = []
        startnode = cPuzzle.startNode
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
            parentNode = None    
            generatedNode = nodegen[1][len(nodegen[1])-1]
             
            totalnumberofnodesgenerated = totalnumberofnodesgenerated + 1
            
            if generatedNode.isgoalState():
                    newlist = copy.copy(nodegen[1])
                    exploredQueue.put((nodegen[0],newlist))                    
            else:
                if generatedNode not in visitedList:                

                    visitedList.append(generatedNode)
                    if(maxvisitedlistsize < len(visitedList)):
                        maxvisitedlistsize = len(visitedList)
                        
                    #print generatedNode.childnodeswithcost.size()    
                    for childnode in cPuzzle.getChildNodes(generatedNode):

                        if(childnode not in visitedList):
                            cost = heuristicfn[childnode] + nodegen[0]                         
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