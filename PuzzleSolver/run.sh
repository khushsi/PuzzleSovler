testcasefile=(
    "input.config"    		
    "test_jugs.config"    
)



typescriptfolder="typescriptfolder"
mkdir $typescriptfolder

for i in "${testcasefile[@]}"
do
echo "Results for testcase in File : "$i
##### Uniformed Search
script -c "python PuzzleSolver.py ${i} bfs"
mv typescript "${typescriptfolder}/typescript.${i}.bfs"
script -c "python PuzzleSolver.py ${i} dfs"
mv typescript "${typescriptfolder}/typescript.${i}.dfs"
script -c "python PuzzleSolver.py ${i} iddfs"
mv typescript "${typescriptfolder}/typescript.${i}.iddfs"
script -c "python PuzzleSolver.py ${i} uniform"
mv typescript "${typescriptfolder}/typescript.${i}.uniform"
##### informed Search - greedy 
script -c "python PuzzleSolver.py ${i} greedy euclidean"
mv typescript "${typescriptfolder}/typescript.${i}.greedy.euclidean"
script -c "python PuzzleSolver.py ${i} greedy manhattanc"
mv typescript "${typescriptfolder}/typescript.${i}.greedy dotproduct"
script -c "python PuzzleSolver.py ${i} greedy dotproduct"
mv typescript "${typescriptfolder}/typescript.${i}.greedy.dotproduct"
script -c "python PuzzleSolver.py ${i} greedy gcdjug"
mv typescript "${typescriptfolder}/typescript.${i}.greedy.gcdjug"
##### informed Search - astar 
script -c "python PuzzleSolver.py ${i} astar euclidean"
mv typescript "${typescriptfolder}/typescript.${i}.astar.euclidean"
script -c "python PuzzleSolver.py ${i} astar manhattanc"
mv typescript "${typescriptfolder}/typescript.${i}.astar.manhattan"
script -c "python PuzzleSolver.py ${i} astar dotproduct"
mv typescript "${typescriptfolder}/typescript.${i}.astar.dotproduct"
script -c "python PuzzleSolver.py ${i} astar gcdjug"
mv typescript "${typescriptfolder}/typescript.${i}.astar.gcdjug"
##### informed Search - idastar 
script -c "python PuzzleSolver.py ${i} idastar euclidean"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.euclidean"
script -c "python PuzzleSolver.py ${i} idastar manhattanc"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.manhattan"
script -c "python PuzzleSolver.py ${i} idastar dotproduct"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.dotproduct"
script -c "python PuzzleSolver.py ${i} idastar gcdjug"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.gcdjug"
done


testcasefile=(
    "cities.config"    		
    "test_cities.config"    
)

for i in "${testcasefile[@]}"
do
echo "Results for testcase in File : "$i
##### Uniformed Search
script -c "python PuzzleSolver.py ${i} bfs"
mv typescript "${typescriptfolder}/typescript.${i}.bfs"
script -c "python PuzzleSolver.py ${i} dfs"
mv typescript "${typescriptfolder}/typescript.${i}.dfs"
script -c "python PuzzleSolver.py ${i} iddfs"
mv typescript "${typescriptfolder}/typescript.${i}.iddfs"
script -c "python PuzzleSolver.py ${i} uniform"
mv typescript "${typescriptfolder}/typescript.${i}.uniform"
##### informed Search - greedy 
script -c "python PuzzleSolver.py ${i} greedy euclidean"
mv typescript "${typescriptfolder}/typescript.${i}.greedy.euclidean"
script -c "python PuzzleSolver.py ${i} greedy manhattanc"
mv typescript "${typescriptfolder}/typescript.${i}.greedy.manhattan"
script -c "python PuzzleSolver.py ${i} greedy dotproduct"
mv typescript "${typescriptfolder}/typescript.${i}.greedy.dotproduct"
##### informed Search - astar 
script -c "python PuzzleSolver.py ${i} astar euclidean"
mv typescript "${typescriptfolder}/typescript.${i}.astar.euclidean"
script -c "python PuzzleSolver.py ${i} astar manhattanc"
mv typescript "${typescriptfolder}/typescript.${i}.astar.manhattan"
script -c "python PuzzleSolver.py ${i} astar dotproduct"
mv typescript "${typescriptfolder}/typescript.${i}.astar.dotproduct"
##### informed Search - idastar 
script -c "python PuzzleSolver.py ${i} idastar euclidean"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.euclidean"
script -c "python PuzzleSolver.py ${i} idastar manhattanc"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.manhattan"
script -c "python PuzzleSolver.py ${i} idastar dotproduct"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.dotproduct"
done


testcasefile=(
    "test_pancakes1.config"    		
    "test_pancakes2.config"    
)

for i in "${testcasefile[@]}"
do
echo "Results for testcase in File : "$i
##### Uniformed Search
script -c "python PuzzleSolver.py ${i} bfs"
mv typescript "${typescriptfolder}/typescript.${i}.bfs"
script -c "python PuzzleSolver.py ${i} dfs"
mv typescript "${typescriptfolder}/typescript.${i}.dfs"
script -c "python PuzzleSolver.py ${i} iddfs"
mv typescript "${typescriptfolder}/typescript.${i}.iddfs"
script -c "python PuzzleSolver.py ${i} uniform"
mv typescript "${typescriptfolder}/typescript.${i}.uniform"
##### informed Search - greedy 
script -c "python PuzzleSolver.py ${i} greedy euclidean"
mv typescript "${typescriptfolder}/typescript.${i}.greedy.euclidean"
script -c "python PuzzleSolver.py ${i} greedy manhattan"
mv typescript "${typescriptfolder}/typescript.${i}.greedy.manhattan"
script -c "python PuzzleSolver.py ${i} greedy dotproduct"
mv typescript "${typescriptfolder}/typescript.${i}.greedy.dotproduct"
script -c "python PuzzleSolver.py ${i} greedy pancake"
mv typescript "${typescriptfolder}/typescript.${i}.greedy.pancake"
script -c "python PuzzleSolver.py ${i} greedy pancakes"
mv typescript "${typescriptfolder}/typescript.${i}.greedy.pancakes"
script -c "python PuzzleSolver.py ${i} greedy flips"
mv typescript "${typescriptfolder}/typescript.${i}.greedy.flips"
script -c "python PuzzleSolver.py ${i} greedy dist-flips"
mv typescript "${typescriptfolder}/typescript.${i}.greedy.distflips"

##### informed Search - astar 
script -c "python PuzzleSolver.py ${i} astar euclidean"
mv typescript "${typescriptfolder}/typescript.${i}.astar.euclidean"
script -c "python PuzzleSolver.py ${i} astar manhattan"
mv typescript "${typescriptfolder}/typescript.${i}.astar.manhattan"
script -c "python PuzzleSolver.py ${i} astar dotproduct"
mv typescript "${typescriptfolder}/typescript.${i}.astar.dotproduct"
script -c "python PuzzleSolver.py ${i} astar pancake"
mv typescript "${typescriptfolder}/typescript.${i}.astar.pancake"
script -c "python PuzzleSolver.py ${i} astar pancakes"
mv typescript "${typescriptfolder}/typescript.${i}.astar.pancakes"
script -c "python PuzzleSolver.py ${i} astar flips"
mv typescript "${typescriptfolder}/typescript.${i}.astar.flips"
script -c "python PuzzleSolver.py ${i} astar dist-flips"
mv typescript "${typescriptfolder}/typescript.${i}.astar.distflips"


##### informed Search - idastar 
script -c "python PuzzleSolver.py ${i} idastar euclidean"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.euclidean"
script -c "python PuzzleSolver.py ${i} idastar manhattan"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.manhattan"
script -c "python PuzzleSolver.py ${i} idastar dotproduct"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.dotproduct"
script -c "python PuzzleSolver.py ${i} idastar pancake"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.pancake"
script -c "python PuzzleSolver.py ${i} idastar pancakes"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.pancakes"
script -c "python PuzzleSolver.py ${i} idastar flips"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.flips"
script -c "python PuzzleSolver.py ${i} idastar dist-flips"
mv typescript "${typescriptfolder}/typescript.${i}.idastar.distflips"

done
