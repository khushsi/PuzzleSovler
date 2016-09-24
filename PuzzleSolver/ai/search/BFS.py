'''
Created on 16-Sep-2016

@author: khush
'''
from Queue import Queue
class BFS:  # @IndentOk
    '''
      Breath First Search - Water Jug  
    '''
def search(cPuzzle):
    try:
        visitedList=[]
        evaluatedPath=[]
        startnode = cPuzzle.startNode
        frontierQueue=Queue();
        maxfrontiersize=0
        maxvisitedlistsize=0
        totalnumberofnodesgenerated=0
        cost=0
        
        if startnode is  None:
            return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost
        
        frontierQueue.put(startnode)

        #Update Max Frontier Queue Size
        if(maxfrontiersize < frontierQueue.qsize()):
            maxfrontiersize = frontierQueue.qsize()
            
#       print "FQ : PUT : "+ startnode.printNode()
        while(frontierQueue.qsize() > 0):
            generatedNode = frontierQueue.get();
                         
            
            totalnumberofnodesgenerated = totalnumberofnodesgenerated + 1            
#             print "FQ : GEt : "+ generatedNode.printNode()
            if generatedNode not in visitedList:                
                
                evaluatedPath.append(generatedNode)                
                cost = cost + generatedNode.getCost()
                        
#                 print generatedNode.printNode()                
                if generatedNode.isgoalState():
                    return evaluatedPath,maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost
            
                visitedList.append(generatedNode)
                if(maxvisitedlistsize < len(visitedList)):
                    maxvisitedlistsize = len(visitedList)

                for childnode in cPuzzle.getChildNodes(generatedNode):
                    if(childnode not in visitedList):
                        frontierQueue.put(childnode)

                    #Update Max Frontier Queue Size
                    if(maxfrontiersize < frontierQueue.qsize()):
                        maxfrontiersize = frontierQueue.qsize()
#                         print "FQ : PUT : "+ childnode.printNode()
                    
    except Exception,e:
        print ("There is an error in provided Input")
        print(str(e))
        return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost
                     
    return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost      