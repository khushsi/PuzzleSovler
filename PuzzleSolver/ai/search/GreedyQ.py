'''
Created on 16-Sep-2016

@author: khush
'''
from Queue import  PriorityQueue
import copy

from ai.utility.PriorityQueueE import PriorityQueueE


class GreedyQ:  # @IndentOk
    '''
      Breath First Search  
    '''
def search(cPuzzle):
    try:
        heuristicfn = cPuzzle.heuristicf
        
        parentNode=[]
        startnode = cPuzzle.startNode 
        maxfrontiersize=0
        totalnumberofnodesgenerated=0
        cost=0
        frontierQueue=PriorityQueueE()
        
        if startnode is  None:
            return [],maxfrontiersize,0,totalnumberofnodesgenerated,cost
        
        #frontierQueue.put(startnode)
        frontierQueue.put((heuristicfn(startnode),[startnode]))
        
        #Update Max Frontier Queue Size
        if(maxfrontiersize < frontierQueue.qsize()):
            maxfrontiersize = frontierQueue.qsize()
            
#         print "FQ : PUT : "+ startnode.printNode()
        while(frontierQueue.qsize() > 0):
            nodegen=[]
            nodegen = copy.copy(frontierQueue.get());

            #Empty Queue
            generatedNode = nodegen[1][len(nodegen[1])-1]
            
            if generatedNode.isgoalState():
                    newlist = copy.copy(nodegen[1])
                    
            else:
                if generatedNode not in parentNode:
                    totalnumberofnodesgenerated = totalnumberofnodesgenerated + 1                
                    c=0                        
                    for childnode in cPuzzle.getChildNodes(generatedNode):
                        
                        if(childnode not in parentNode):
                            c=c+1
                            cost = heuristicfn(childnode)                         
                            frontierQueue.put((cost,nodegen[1] + [childnode]))
                            
                    #Update Max Frontier Queue Size
                    if(maxfrontiersize < frontierQueue.qsize()):
                        maxfrontiersize = frontierQueue.qsize()
                    if(c > 0 and generatedNode not in parentNode):
                        parentNode.append(generatedNode)        
                    elif generatedNode in parentNode:
                        parentNode.remove(generatedNode)    

        final = frontierQueue.getPath(cPuzzle.goalNode)
        prev = None
        cost=0
        for i in final[1]:
            cost = cost + i.getCost(prev)
            prev = i 
        return final[1],maxfrontiersize,0,totalnumberofnodesgenerated,cost                  
    finally:
        abc=10
        
    return [],maxfrontiersize,0,totalnumberofnodesgenerated,cost      