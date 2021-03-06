'''
Created on 16-Sep-2016

@author: khush
'''
import sys

from ai.puzzle.JugPuzzle import JugPuzzle
from ai.puzzle.PathPuzzle import PathPuzzle
from ai.puzzle.PancakePuzzle import PancakePuzzle
from ai.search import BFS, IDDFS, Uniform, DFS, Greedy, Astar, IDAstar, UniformQ, DFSV, GreedyQ
from ai.search import AstarV
import signal

def handler(signum, frame):
    print "Cant solve in 30 minutes so timed out"
    raise Exception("EOP")

if __name__ == '__main__':

    signal.signal(signal.SIGALRM, handler)
    signal.alarm( 1800 )

#     signal.signal(signal.SIGABRT, handler)
#     signal.alarm(30 * 60)
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
                cPuzzle.heuristicf = cPuzzle.getEuclideanHeuristic
            elif(heuristic == "manhattan"):
                cPuzzle.heuristicf = cPuzzle.getManhattanHeuristic
            elif(heuristic == "pancake"):
                cPuzzle.heuristicf = cPuzzle.getPancakeHeuristic
            elif(heuristic == "pancakes"):
                cPuzzle.heuristicf = cPuzzle.getPancakeHeuristicSimple
            elif(heuristic == "flips"):
                cPuzzle.heuristicf = cPuzzle.getflipsHeuristic
            elif(heuristic == "dist-flips"):
                cPuzzle.heuristicf = cPuzzle.getdistpanHeuristic
            elif(heuristic == "dotproduct"):
                cPuzzle.heuristicf = cPuzzle.getDotProductHeuristic
            elif(heuristic == "gcdjug"):
                cPuzzle.heuristicf = cPuzzle.getGcdHeuristic
            
                
            if(searchalgo.lower() == "bfs"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost = BFS.search(cPuzzle)
            elif (searchalgo.lower() == "dfs"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost = DFS.search(cPuzzle)
            elif (searchalgo.lower() == "iddfs"):
                cSearch,maxstoredquesize, maxvisitedlistsize,totalnumberofnodesgenerated,maxdepth = IDDFS.search(cPuzzle)
            elif (searchalgo.lower() == "uniform"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost = UniformQ.search(cPuzzle)
            elif (searchalgo.lower() == "greedy"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost = GreedyQ.search(cPuzzle)
            elif (searchalgo.lower() == "astar"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost =  Astar.search(cPuzzle)
            elif (searchalgo.lower() == "idastar"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated,cost,cutoff =  IDAstar.search(cPuzzle)
            elif (searchalgo.lower() == "dfsv"):
                cSearch,maxstoredquesize,maxvisitedlistsize,totalnumberofnodesgenerated = DFSV.search(cPuzzle)

                
            if(searchalgo.lower() != "dfs" and searchalgo.lower() != "dfsv"):
                if(len(cSearch) == 0):
                    print( "No Solution")    
                else:
                    for evnode in cSearch:
                        print( evnode.printNode())

            print("Time Complexity:" + str(totalnumberofnodesgenerated))    
            print("Space Complexity Queue:" + str(maxstoredquesize))
            print( "Space Complexity VisitedList:" + str(maxvisitedlistsize))

            if (searchalgo.lower() not in ['bfs','dfs','dfsv','iddfs']):
                print( "PathCost:" + str(cost))
            
            if (searchalgo == "iddfs"):
                print( "Depth Iterated : " + str(maxdepth))
            elif(searchalgo == "idastar"):
                print( "Cut-off Reached : " + str(cutoff))    
    
    except:    
        print("Time out")
    
    finally:
        signal.alarm(0)
        f.close()
        
