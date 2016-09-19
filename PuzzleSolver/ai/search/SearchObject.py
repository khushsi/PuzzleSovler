'''
Created on 16-Sep-2016

@author: khush
'''
from __builtin__ import file
from ai.search.PuzzleClasses import JugPuzzle

class PuzzleSolver(object):
    '''
    classdocs
    '''        
    
    def __init__(self, params):
        '''
        Constructor
        '''
        
    def getSuccessorNode(self,node):
        succnodes=None
        return succnodes
    
    def getChildNodes(self,node):
        childnodes=[]
        return childnodes
        
    
    
class Node:
    def __init__(self,name,type):
        self.NodeName = name
        self.NodeType = type
        
    def getNodeName(self):
        print self.NodeName
        return
   
    def isGoalNode(self):
        
        return False    
        
        
    
            