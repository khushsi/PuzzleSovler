'''
Created on 16-Sep-2016

@author: khush
'''
import sys

from ai.puzzle.JugPuzzle import JugPuzzle
from ai.puzzle.PathPuzzle import PathPuzzle
from ai.puzzle.PancakePuzzle import PancakePuzzle
from ai.search import BFS, IDDFS, Uniform, DFS, Greedy, Astar, IDAstar, UniformQ
from ai.search import AstarV


if __name__ == '__main__':
    
    try:        
        
        inputArray=[]
        maxstoredquesize = 0
        maxvisitedlistsize = 0
        totalnumberofnodesgenerated = 0
        cost = 0
        cPuzzle=None
        heuristic=""
        cutoff=0
        
        if __name__ == '__main__':
            inputfile = sys.argv[1]
            with open(inputfile,"r") as f:
                for line in f:
                    line = line.strip('\n')
                    inputArray.append(line)
                    
            heuristic=""        
            puzzle=inputArray[0].replace('\n', '').replace('\r', '')
            searchalgo=sys.argv[2]
            if(len(sys.argv) > 3):
                heuristic=sys.argv[3]
            
            if(str(puzzle) == "jugs"):
                cPuzzle = JugPuzzle(inputArray)
            elif(str(puzzle) == "cities" ):
                cPuzzle = PathPuzzle(inputArray)
            elif(str(puzzle) == "pancakes"):
                cPuzzle = PancakePuzzle(inputArray)
                
            heuristiclist=dict()
            
            if(heuristic == "euclidean"):
                heuristiclist = cPuzzle.getEuclideanHeuristic()
            elif(heuristic == "manhattan"):
                heuristiclist = cPuzzle.getManhattanHeuristic()
            
                
            if(searchalgo.lower() == "bfs"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost = BFS.search(cPuzzle)
            elif (searchalgo.lower() == "dfs"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated = DFS.search(cPuzzle)
            elif (searchalgo.lower() == "iddfs"):
                cSearch,maxstoredquesize
                maxvisitedlistsize,totalnumberofnodesgenerated,maxdepth = IDDFS.search(cPuzzle)
            elif (searchalgo.lower() == "uniform"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost = UniformQ.search(cPuzzle)
            elif (searchalgo.lower() == "greedy"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost = Greedy.search(cPuzzle,heuristiclist)
            elif (searchalgo.lower() == "astar"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost =  Astar.search(cPuzzle,heuristiclist)
            elif (searchalgo.lower() == "idastar"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost,cutoff =  IDAstar.search(cPuzzle,heuristiclist)
            elif (searchalgo.lower() == "uniformq"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost = UniformQ.search(cPuzzle)

                
            if(len(cSearch) == 0):
                print( "No Solution")    
            else:
                for evnode in cSearch:
                    print( evnode.printNode())
            print("Time Complexity:" + str(totalnumberofnodesgenerated))    
            print("Space Complexity Queue:" + str(maxstoredquesize))
            print( "Space Complexity VisitedList:" + str(maxvisitedlistsize))
            print( "PathCost:" + str(cost))
            if (searchalgo == "iddfs"):
                print( "Depth Iterated : " + str(maxdepth))
            elif(searchalgo == "idastar"):
                print( "Cut-off Reached : " + str(cutoff))    
                
    finally:
        f.close()
    
    
