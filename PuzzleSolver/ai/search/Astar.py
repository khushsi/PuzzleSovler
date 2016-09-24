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
def search(cPuzzle,heuristicfn):
    try:
#         visitedList=[]
        startnode=cPuzzle.startNode
        maxfrontiersize=0
#         maxvisitedlistsize=0
        totalnumberofnodesgenerated=0
        cost=0
        frontierQueue=PriorityQueueE()
        exploredQueue=PriorityQueue()
        if startnode is  None:
            return [],maxfrontiersize,0,totalnumberofnodesgenerated,cost
        
        #frontierQueue.put(startnode)
        frontierQueue.put((heuristicfn[startnode],[startnode]))
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
            parentNode = None    
            if(len(nodegen[1]) > 1):
                parentNode= nodegen[1][len(nodegen[1])-2]
            
            totalnumberofnodesgenerated = totalnumberofnodesgenerated + 1
            
            if generatedNode.isgoalState():
                    newlist = copy.copy(nodegen[1])
                    exploredQueue.put((nodegen[0],newlist))
                    
            else:


                currentdistance = 0
                previousheuristic=heuristicfn[generatedNode]
                
#                 print len(nodegen[1])
#                 print len(generatedNode.childnodeswithcost)    
                for childnode in cPuzzle.getChildNodes(generatedNode):
                    if childnode  not in nodegen[1]:
                        currentdistance = generatedNode.childnodeswithcost[childnode]
                        cost = heuristicfn[childnode] + nodegen[0] + currentdistance - previousheuristic
                        frontierQueue.put((cost,nodegen[1] + [childnode]))
                    
                    #Update Max Frontier Queue Size
                    if(maxfrontiersize < frontierQueue.qsize()):
                        maxfrontiersize = frontierQueue.qsize()
#                         print "FQ : PUT : "+ childnode.printNode()

        final = exploredQueue.get()
        cost = final[0]
        
        return final[1],maxfrontiersize,0,totalnumberofnodesgenerated,cost                  
    finally:
        abc=10
        
    return [],maxfrontiersize,0,totalnumberofnodesgenerated,cost      