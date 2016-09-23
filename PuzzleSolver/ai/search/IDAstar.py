'''
Created on 16-Sep-2016

@author: khush
'''
#from ai.utility.PriorityQueueE import  PriorityQueueE
from Queue import PriorityQueue
import copy


class IDAstar:  # @IndentOk
    '''
      DFS  
    '''

def search(cPuzzle,heuristicfn):
    
    cutoff = 0
    maxfrontiersize=0
    maxvisitedlistsize=0
    totalnumberofnodesgenerated=0
    cost =0
    startnode = cPuzzle.startNode
    
    try:
        cutoff = heuristicfn[startnode]
        ncutoff = heuristicfn[startnode]
        while(ncutoff  >= cutoff):
            cutoff = ncutoff
#             print "outgoing DFS Count " + str(cutoff)
            evalp,maxfrontiersizer,maxvisitedlistsizer,totalnumberofnodesgeneratedr,cost,ncutoff = IDAstar(startnode,heuristicfn,cutoff,cPuzzle)
            if(maxfrontiersize < maxfrontiersizer):
                maxfrontiersize = maxfrontiersizer
            if(maxvisitedlistsize < maxvisitedlistsizer):
                maxvisitedlistsize = maxvisitedlistsizer
            totalnumberofnodesgenerated = totalnumberofnodesgenerated + totalnumberofnodesgeneratedr        
    #             print "Incoming BFS Count " + str(depth)
    #             print "Max Depth " + str(maxdepth)
            if len(evalp) > 0:
    #                 print len(evalp)
                return evalp,maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost,cutoff
        
    except Exception ,e:
        print "There is an error in provided Input"
        print str(e)
    return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost,cutoff

def IDAstar(startnode,heuristicfn,cutoff,cPuzzle):
    try:
        visitedList=[]
        nextcutoff=cutoff
        maxfrontiersize=0
        maxvisitedlistsize=0
        totalnumberofnodesgenerated=0
        cost=0
        frontierQueue=PriorityQueue()
        nextcutoff=[]
        if startnode is  None:
            return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost,cutoff
        
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
            generatednodeheuristic=heuristicfn[generatedNode]
#             print "In coming cutoff" + str(cutoff)
#             print generatednodeheuristic
            if(generatednodeheuristic <= cutoff):
                
                parentNode = None    

                if(len(nodegen[1]) > 1):
                    parentNode= nodegen[1][len(nodegen[1])-2]
                
                totalnumberofnodesgenerated = totalnumberofnodesgenerated + 1
                
                if generatedNode.isgoalState():
                        cost = nodegen[0]
                        newlist = copy.copy(nodegen[1])
                        return newlist,maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost,nextcutoff
                        
                else:
            
                    if(maxvisitedlistsize < len(visitedList)):
                        maxvisitedlistsize = len(visitedList)
    
                    currentdistance = 0
                    #print generatedNode.childnodeswithcost.size()    
                    for childnode in cPuzzle.getChildNodes(generatedNode):
                        currentdistance = generatedNode.childnodeswithcost[childnode]
                        cost = heuristicfn[childnode] + nodegen[0] + currentdistance - generatednodeheuristic
#                         print generatedNode.printNode()
#                         print "Curremt Cost : "+ str(nodegen[0])
#                         print childnode.printNode() +"hue ::" + str(heuristicfn[childnode])
#                         print "prev distance : " + str(currentdistance)
#                         print "prev parent to gen hue : " + str(generatednodeheuristic) 
#                         print "New Cost "+str(cost)
#                         print childnode.printNode()                                                    
                        frontierQueue.put((cost,nodegen[1] + [childnode]))
                        
                        if(heuristicfn[childnode] > cutoff ):
                            if(nextcutoff == 0 ):
                                nextcutoff = heuristicfn[childnode]
                            else:
                                nextcutoff = min(nextcutoff,heuristicfn[childnode])
                    #Update Max Frontier Queue Size
                    if(maxfrontiersize < frontierQueue.qsize()):
                        maxfrontiersize = frontierQueue.qsize()
                
                        #print "FQ : PUT : "+ childnode.printNode()
#         print "new cutoff : "+nextcutoff
        return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost,nextcutoff                  
    finally:
        abc=10
        
    return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost,nextcutoff      