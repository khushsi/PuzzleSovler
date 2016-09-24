'''
Created on 16-Sep-2016

@author: khush
'''
from Queue import LifoQueue
class DFS:  # @IndentOk
    '''
      Breath First Search  
    '''
def search(cPuzzle):
    try:

        maxfrontiersize=0
        totalnumberofnodesgenerated=0
        startnode = cPuzzle.startNode
        nodestack=LifoQueue();
        if startnode is None:
            print "No Solution"
            return [],maxfrontiersize,0,totalnumberofnodesgenerated

        
        nodestack.put(startnode)
        #Update Max Frontier Queue Size
        if(maxfrontiersize < nodestack.qsize()):
            maxfrontiersize = nodestack.qsize()
        
        parentNode = []
        while(nodestack.qsize() > 0):
            
            generatedNode = nodestack.get();
                
            
            
#            print "FQ : GET : "+ generatedNode.printNode()            
            print generatedNode.printNode()            
            if( generatedNode  not in parentNode):
                if generatedNode.isgoalState():                        
                    return [],maxfrontiersize,0,totalnumberofnodesgenerated
                
                totalnumberofnodesgenerated = totalnumberofnodesgenerated + 1
                
                c=0
                for childnode in cPuzzle.getChildNodes(generatedNode):

                    if(childnode  not in parentNode):
                        c=c=+1
                        nodestack.put(childnode)
                    
                    if(maxfrontiersize < nodestack.qsize()):
                        maxfrontiersize = nodestack.qsize()
    
                if(c > 0 and generatedNode not in parentNode):
                    parentNode.append(generatedNode)        
                elif generatedNode in parentNode:
                    parentNode.remove(generatedNode)    
#                     print "FQ : PUT : "+ childnode.printNode()
                
#                 print "-----------------"
                    
    except Exception,e:
        print str(e)
        print "No Solution"
    print "No Solution"
    return [],maxfrontiersize,0,totalnumberofnodesgenerated
                     
                
                
            
    