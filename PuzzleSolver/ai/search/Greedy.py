'''
Created on 16-Sep-2016

@author: khush
'''
from Queue import Queue, PriorityQueue


class Uniform:  # @IndentOk
    '''
      Breath First Search  
    '''
def search(startnode):
    try:
        visitedList=[]
        evaluatedPath=[]
        maxfrontiersize=0
        maxvisitedlistsize=0
        totalnumberofnodesgenerated=0
        cost = 0
        frontierQueue=PriorityQueue()
        if startnode is  None:
            return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost
        
        #frontierQueue.put(startnode)
        frontierQueue.put((0,startnode))
        #Update Max Frontier Queue Size
        if(maxfrontiersize < frontierQueue.qsize()):
            maxfrontiersize = frontierQueue.qsize()
            
        #print "FQ : PUT : "+ startnode.printNode()
        while(frontierQueue.qsize() > 0):
            
            nodegen = frontierQueue.get();
            #Empty Queue
                
            generatedNode = nodegen[1]
            generatedNodeval = nodegen[0]
            totalnumberofnodesgenerated = totalnumberofnodesgenerated + 1            
            #print "FQ : :GEt : "+ generatedNode.printNode()  
            
            if generatedNode not in visitedList:                
                evaluatedPath.append(generatedNode)
                cost = cost + generatedNodeval                 
                if generatedNode.isgoalState():
#                     for i in evaluatedPath:
#                         print i.printNode()    
                    return evaluatedPath,maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost
            
                visitedList.append(generatedNode)
                if(maxvisitedlistsize < len(visitedList)):
                    maxvisitedlistsize = len(visitedList)

#                 print "Visited Start"
#                 for k in visitedList:
#                     print k.printNode()
#                 print "Visited End"

                for childnode in generatedNode.childnodes.keys():
                    
                    if(childnode not in visitedList):                        
                        frontierQueue.put((generatedNode.childnodes[childnode],childnode))
                        #print "FQ : "+generatedNode.printNode()+" : PUT : "+ childnode.printNode() +" "+ str(generatedNode.childnodes[childnode])
                    #Update Max Frontier Queue Size
                    if(maxfrontiersize < frontierQueue.qsize()):
                        maxfrontiersize = frontierQueue.qsize()
                        #print "FQ : PUT : "+ childnode.printNode()
                    
    except Exception,e:
        print "There is an error in provided Input"
        print(str(e))
        return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost
                     
    return [],maxfrontiersize,maxvisitedlistsize,totalnumberofnodesgenerated,cost      