testcasefiles =['input.config']

for i in testcasefiles:
do
print "Results for testcase in File : "$filename
##### Uniformed Search
script -c "python PuzzleSolver.py input.config bfs"
mv typescript typescript.input.config.bfs
script -c "python PuzzleSolver.py input.config dfs"
mv typescript typescript.input.config.dfs
script -c "python PuzzleSolver.py input.config iddfs"
mv typescript typescript.input.config.iddfs
script -c "python PuzzleSolver.py input.config uniform"
mv typescript typescript.input.config.uniform
##### informed Search - greedy 
script -c "python PuzzleSolver.py input.config greedy euclidean"
mv typescript typescript.input.config.greedy.euclidean
script -c "python PuzzleSolver.py input.config greedy manhattan"
mv typescript typescript.input.config.greedy.manhattan
script -c "python PuzzleSolver.py input.config greedy dotproduct"
mv typescript typescript.input.config.greedy.dotproduct
script -c "python PuzzleSolver.py input.config greedy gcdjug"
mv typescript typescript.input.config.greedy.gcdjug
##### informed Search - astar 
script -c "python PuzzleSolver.py input.config astar euclidean"
mv typescript typescript.input.config.astar.euclidean
script -c "python PuzzleSolver.py input.config astar manhattan"
mv typescript typescript.input.config.astar.manhattan
script -c "python PuzzleSolver.py input.config astar dotproduct"
mv typescript typescript.input.config.astar.dotproduct
script -c "python PuzzleSolver.py input.config astar gcdjug"
mv typescript typescript.input.config.astar.gcdjug
##### informed Search - idastar 
script -c "python PuzzleSolver.py input.config idastar euclidean"
mv typescript typescript.input.config.idastar.euclidean
script -c "python PuzzleSolver.py input.config idastar manhattan"
mv typescript typescript.input.config.idastar.manhattan
script -c "python PuzzleSolver.py input.config idastar dotproduct"
mv typescript typescript.input.config.idastar.dotproduct
script -c "python PuzzleSolver.py input.config idastar gcdjug"
mv typescript typescript.input.config.idastar.gcdjug
done
