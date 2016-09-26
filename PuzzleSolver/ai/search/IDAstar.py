'''
Created on 16-Sep-2016

@author: khush
'''
from ai.utility.PriorityQueueE import  PriorityQueueE
import copy


class IDAstar:  # @IndentOk
    '''
      DFS  
    '''

def search(cPuzzle):
    
    cutoff = 0
    maxfrontiersize=0
    maxvisitedlistsize=0
    totalnumberofnodesgenerated=0
    cost =0
    startnode = cPuzzle.startNode
    heuristicfn = cPuzzle.heuristicf
    cutoff = heuristicfn(startnode)
    ncutoff = heuristicfn(startnode)
    while(ncutoff  >= cutoff):
        cutoff = ncutoff
#         print "outgoing DFS Count " + str(ncutoff)
        evalp,maxfrontiersizer,maxvisitedlistsizer,totalnumberofnodesgeneratedr,cost,ncutoff = IDAstar(startnode,heuristicfn,cutoff,cPuzzle)
        
        if(maxfrontiersize < maxfrontiersizer):
            maxfrontiersize = maxfrontiersizer
        if(maxvisitedlistsize < maxvisitedlistsizer):
            maxvisitedlistsize = maxvisitedlistsizer
        
        totalnumberofnodesgenerated = totalnumberofnodesgenerated + totalnumberofnodesgeneratedr        
#       print "Incoming BFS Count " + str(depth)
#       print "Max Depth " + str(maxdepth)
        if len(evalp) > 0:
#                 print len(evalp)
            return evalp,maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost,cutoff
    
#     except Exception ,e:
#         print "There is an error in provided Input"
#         print str(e)
    return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost,cutoff

def IDAstar(startnode,heuristicfn,cutoff,cPuzzle):
    try:
        parentNode=[]
        nextcutoff=cutoff
        maxfrontiersize=0

        totalnumberofnodesgenerated=0
        cost=0
        frontierQueue=PriorityQueueE()
        nextcutoff=[]
        
        if startnode is  None:
            return [],maxfrontiersize,0,totalnumberofnodesgenerated,cost,cutoff
        
        #frontierQueue.put(startnode)
        frontierQueue.put((heuristicfn(startnode),[startnode]))
        #Update Max Frontier Queue Size
        if(maxfrontiersize < frontierQueue.qsize()):
            maxfrontiersize = frontierQueue.qsize()
            
        #print "FQ : PUT : "+ startnode.printNode()
        while(frontierQueue.qsize() > 0):
            nodegen=[]
            nodegen = copy.copy(frontierQueue.get());
                
            generatedNode = nodegen[1][len(nodegen[1])-1]
            generatednodeheuristic=heuristicfn(generatedNode)
            if(len(nodegen[1]) > 1):
                parentNode.append(nodegen[1][len(nodegen[1])-2])

            if(generatednodeheuristic <= cutoff and generatedNode not in parentNode):

                
                totalnumberofnodesgenerated = totalnumberofnodesgenerated + 1
                
                if generatedNode.isgoalState():
                        newlist = copy.copy(nodegen[1])
                        return newlist,maxfrontiersize,0,totalnumberofnodesgenerated,cost,nextcutoff
                        
                else:
            
                    currentdistance = 0
                    #print generatedNode.childnodeswithcost.size()    
                    c=0 
                    for childnode in cPuzzle.getChildNodes(generatedNode):
                        c=c+1
                        if(heuristicfn(childnode) > cutoff ):                            
                            if(nextcutoff == 0 ):
                                nextcutoff = heuristicfn(childnode)
                            else:
                            
                                nextcutoff = min(nextcutoff,heuristicfn(childnode))
                        else:
                            currentdistance = generatedNode.getCost(childnode)
                            cost = heuristicfn(childnode) + nodegen[0] + currentdistance - generatednodeheuristic
                            frontierQueue.put((cost,nodegen[1] + [childnode]))
       
                    #Update Max Frontier Queue Size
                    if(maxfrontiersize < frontierQueue.qsize()):
                        maxfrontiersize = frontierQueue.qsize()
                
                        #print "FQ : PUT : "+ childnode.printNode()
#         print "new cutoff : "+nextcutoff
        return [],maxfrontiersize,0,totalnumberofnodesgenerated,cost,nextcutoff                  
    finally:
        abc=10
        
    return [],maxfrontiersize,0,totalnumberofnodesgenerated,cost,nextcutoff      