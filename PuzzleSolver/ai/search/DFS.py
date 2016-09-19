'''
Created on 16-Sep-2016

@author: khush
'''
from Queue import LifoQueue
class DFS:  # @IndentOk
    '''
      Breath First Search  
    '''
def search(startnode):
    try:

        maxfrontiersize=0
        maxvisitedlistsize=0
        totalnumberofnodesgenerated=0
        
        nodestack=LifoQueue();
        if startnode is None:
            return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated

        visitedList=[]
        evaluatedPath=[]
        
        nodestack.put(startnode)
        #Update Max Frontier Queue Size
        if(maxfrontiersize < nodestack.qsize()):
            maxfrontiersize = nodestack.qsize()
        
        if(maxvisitedlistsize < len(visitedList)):
            maxvisitedlistsize = len(visitedList)

        
        while(nodestack.qsize() > 0):
            
            generatedNode = nodestack.get();
            if(generatedNode not in visitedList):
                
                totalnumberofnodesgenerated = totalnumberofnodesgenerated + 1
    #            print "FQ : GET : "+ generatedNode.printNode()            
                evaluatedPath.append(generatedNode)
                visitedList.append(generatedNode)   
                if(maxvisitedlistsize < len(visitedList)):
                    maxvisitedlistsize = len(visitedList)
         
                if generatedNode.isgoalState():
    #                 for i in evaluatedPath:
    #                     print i.printNode()                
                    return evaluatedPath,maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated
    
    #             print "Visited Start"
    #             for k in visitedList:
    #                 print k.printNode()
    #             print "Visited End"
                
                for childnode in generatedNode.childnodes:
                    if(childnode not in visitedList):
                        nodestack.put(childnode)
                    if(maxfrontiersize < nodestack.qsize()):
                        maxfrontiersize = nodestack.qsize()
                        
    #                    print "FQ : PUT : "+ childnode.printNode()
        
                    
    except Exception,e:
        print "There is an error in provided Input"
        print str(e)
    return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated
                     
                
                
            
    