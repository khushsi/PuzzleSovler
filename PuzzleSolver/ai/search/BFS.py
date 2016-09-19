'''
Created on 16-Sep-2016

@author: khush
'''
from Queue import Queue
class BFS:  # @IndentOk
    '''
      Breath First Search  
    '''
def search(startnode):
    try:
        visitedList=[]
        evaluatedPath=[]
        
        frontierQueue=Queue();
        maxfrontiersize=0
        maxvisitedlistsize=0
        totalnumberofnodesgenerated=0
        if startnode is  None:
            return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated
        
        frontierQueue.put(startnode)
        #Update Max Frontier Queue Size
        if(maxfrontiersize < frontierQueue.qsize()):
            maxfrontiersize = frontierQueue.qsize()
            
        #print "FQ : PUT : "+ startnode.printNode()
        while(frontierQueue.qsize() > 0):
            generatedNode = frontierQueue.get();
            totalnumberofnodesgenerated = totalnumberofnodesgenerated + 1            
            #print "FQ : GEt : "+ generatedNode.printNode()
            if generatedNode not in visitedList:                
                evaluatedPath.append(generatedNode)                
                if generatedNode.isgoalState():
#                     for i in evaluatedPath:
#                         print i.printNode()    
                    return evaluatedPath,maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated
            
                visitedList.append(generatedNode)
                if(maxvisitedlistsize < len(visitedList)):
                    maxvisitedlistsize = len(visitedList)

#                 print "Visited Start"
#                 for k in visitedList:
#                     print k.printNode()
#                 print "Visited End"

                for childnode in generatedNode.childnodes:
                    if(childnode not in visitedList):
                        frontierQueue.put(childnode)
                    #Update Max Frontier Queue Size
                    if(maxfrontiersize < frontierQueue.qsize()):
                        maxfrontiersize = frontierQueue.qsize()
                        #print "FQ : PUT : "+ childnode.printNode()
                    
    except Exception,e:
        print "There is an error in provided Input"
        print(str(e))
        return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated
                     
    return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated      