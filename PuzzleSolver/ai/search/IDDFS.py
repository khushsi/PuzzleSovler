'''
Created on 16-Sep-2016

@author: khush
'''
from Queue import Queue
class IDDFS:  # @IndentOk
    '''
      Iterative Deepening DFS  
    '''
def search(cPuzzle):
    
    depth = 0
    dfscount=0
    maxfrontiersize=0
    maxvisitedlistsize=0
    totalnumberofnodesgenerated=0
    maxdepth=0
    startnode = cPuzzle.startNode
    
    try:
        
        while(maxdepth  >= dfscount):
            dfscount = dfscount + 1
            depth = 0
#             print "outgoing DFS Count " + str(dfscount)
            evalp,maxfrontiersizer,maxvisitedlistsizer,totalnumberofnodesgeneratedr,maxdepth = inBFS(startnode,depth,dfscount,cPuzzle)
            if(maxfrontiersize < maxfrontiersizer):
                maxfrontiersize = maxfrontiersizer
            if(maxvisitedlistsize < maxvisitedlistsizer):
                maxvisitedlistsize = maxvisitedlistsizer
            totalnumberofnodesgenerated = totalnumberofnodesgenerated + totalnumberofnodesgeneratedr        
#             print "Incoming BFS Count " + str(depth)
#             print "Max Depth " + str(maxdepth)
            if len(evalp) > 0:
#                 print len(evalp)
                return evalp,maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,maxdepth
        
    except Exception ,e:
        print "There is an error in provided Input"
        print str(e)
    return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,maxdepth
                
                
def inBFS(startnode,depth,dfscount,cPuzzle):
    try:
        visitedList=[]
        evaluatedPath=[]
        frontierQueue=Queue();
        depthqueue = Queue();
        maxfrontiersize=0
        maxvisitedlistsize=0
        totalnumberofnodesgenerated=0
        maxdepth=0
        if startnode is None:
            return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,maxdepth
        
#         print "---DFS Iteration :: "+ str(dfscount)
        frontierQueue.put(startnode)
        #Update Max Frontier Queue Size
        if(maxfrontiersize < frontierQueue.qsize()):
            maxfrontiersize = frontierQueue.qsize()
        
        depthqueue.put(depth+1)
        if maxdepth < (depth+1):
            maxdepth = depth+1
            
        
        while(frontierQueue.qsize() > 0):
            
            totalnumberofnodesgenerated = totalnumberofnodesgenerated + 1
            generatedNode = frontierQueue.get();
            depth = depthqueue.get()
            if(depth > dfscount):
                return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,maxdepth
    
    #         print "---BFS Iteration for depth :: "+ str(depth)                
    #         print "FQ : GEt : "+ generatedNode.printNode()
            
                    
            if generatedNode not in visitedList:
                evaluatedPath.append(generatedNode)
    
                if generatedNode.isgoalState():
    #                 for i in evaluatedPath:
    #                     print i.printNode()                
                    return evaluatedPath,maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,maxdepth        
            
                visitedList.append(generatedNode)
                if(maxvisitedlistsize < len(visitedList)):
                    maxvisitedlistsize = len(visitedList)
                                 
                for childnode in cPuzzle.getChildNodes(generatedNode):
                    if(childnode not in visitedList):
                        frontierQueue.put(childnode)
                        depthqueue.put(depth+1)
                    if maxdepth < (depth+1):
                        maxdepth = depth+1
    
                        #Update Max Frontier Queue Size
                        if(maxfrontiersize < frontierQueue.qsize()):
                            maxfrontiersize = frontierQueue.qsize()
    
    #                     print "FQ : PUT : "+ childnode.printNode()
    except Exception,e:
        print(str(e))
        
    return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,maxdepth                