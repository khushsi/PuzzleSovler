'''
Created on 16-Sep-2016

@author: khush
'''
import sys

from ai.puzzle.JugPuzzle import JugPuzzle
from ai.puzzle.PathPuzzle import PathPuzzle
from ai.search import BFS, IDDFS, Uniform,DFS,Greedy



if __name__ == '__main__':
    
    try:
        
        inputArray=[]
        maxstoredquesize = 0
        maxvisitedlistsize = 0
        totalnumberofnodesgenerated = 0
        cost = 0
        cPuzzle=None
        
        if __name__ == '__main__':
            inputfile = sys.argv[1]
            with open(inputfile,"r") as f:
                for line in f:
                    line = line.strip('\n')
                    inputArray.append(line)
                    
                    
            puzzle=inputArray[0].replace('\n', '').replace('\r', '')
            searchalgo=sys.argv[2]
            
            if(str(puzzle) == "jugs"):
                cPuzzle = JugPuzzle(inputArray)
            elif(str(puzzle) == "cities" ):
                cPuzzle = PathPuzzle(inputArray)
                
                
            
                
            if(searchalgo == "BFS"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated = BFS.search(cPuzzle.startNode)
            elif (searchalgo == "DFS"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated = DFS.search(cPuzzle.startNode)
            elif (searchalgo == "IDDFS"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,maxdepth = IDDFS.search(cPuzzle.startNode)
            elif (searchalgo == "Uniform"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost = Uniform.search(cPuzzle.startNode)
            elif (searchalgo == "Greedy"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost = Greedy.search(cPuzzle.startNode,cPuzzle.getGreedyHeuristic())
                
            if(len(cSearch) == 0):
                print "No Solution"    
            else:
                for evnode in cSearch:
                    print evnode.printNode()
            print "Time Complexity:" + str(totalnumberofnodesgenerated)    
            print "Space Complexity Queue:" + str(maxstoredquesize)
            print "Space Complexity VisitedList:" + str(maxvisitedlistsize)
            print "PathCost:" + str(cost)
                
    finally:
        f.close()
    
    
