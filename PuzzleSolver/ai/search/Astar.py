'''
Created on 16-Sep-2016

@author: khush
'''
from Queue import  PriorityQueue
from ai.utility.PriorityQueueE import PriorityQueueE
import copy


class Astar:  # @IndentOk
    '''
      DFS  
    '''
def search(cPuzzle):
    try:
        
        startnode=cPuzzle.startNode
        maxfrontiersize=0
        heuristicfn = cPuzzle.heuristicf
        parentNode = []
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
#             visitedList.append(generatedNode)
             
            if(len(nodegen[1]) > 1):
                parentNode.append(nodegen[1][len(nodegen[1])-2])

            if(generatedNode not in parentNode):
           
                if generatedNode.isgoalState():
                        newlist = copy.copy(nodegen[1])
                else:
                    totalnumberofnodesgenerated = totalnumberofnodesgenerated + 1
                    currentdistance = 0
                    previousheuristic=heuristicfn(generatedNode)
                    
                    c=0    
                    for childnode in cPuzzle.getChildNodes(generatedNode):
                        if childnode  not in parentNode:
                            c=c+1
                            currentdistance = generatedNode.getCost(childnode)
                            cost = heuristicfn(childnode) + nodegen[0] + currentdistance - previousheuristic
                            frontierQueue.put((cost,nodegen[1] + [childnode]))
                        
                    #Update Max Frontier Queue Size
                    if(maxfrontiersize < frontierQueue.qsize()):
                        maxfrontiersize = frontierQueue.qsize()

                    if(c > 0 and generatedNode not in parentNode):
                        parentNode.append(generatedNode)        
                    elif generatedNode in cPuzzle.getChildNodes(parentNode[-1]):
                        parentNode.pop()
                    
#                   print "FQ : PUT : "+ childnode.printNode()

        final = frontierQueue.getPath(cPuzzle.goalNode)
        if(final is not None):
            prev = None
            cost=0
            for i in final[1]:
                cost = cost + i.getCost(prev)
                prev = i
            eval=final[1]
        else:
            eval = []       
        return eval,maxfrontiersize,0,totalnumberofnodesgenerated,cost                  
    finally:
        abc=10
        
    return [],maxfrontiersize,0,totalnumberofnodesgenerated,cost      