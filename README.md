# Project Name

Assignment 1 : Foundation of AI - Uninformed and Informed Search

## Requirements

Python 2.7.12

## Usage / Running the program - WaterJug, PathFinder and Pancake Problem

Main Folder of the project is PuzzleSolver and main file is PuzzleSolver.py

Command : Python PuzzleSolver.py testcasefile algorithm heuristic

example: To run A* (astar) algorithm on jug puzzle for euclidean heuristic 

```
python PuzzleSolver.py test_jugs.config astar euclidean
```
example: To run bfs algorithm on jug puzzle 

```
python PuzzleSolver.py test_jugs.config bfs
```

## Options

```
algorithm - bfs dfs iddfs uniform greedy astar idastar
```
```
heuristic - euclidean manhattan dotproduct gcdjug pancake flips dist-flips
```
`common heuristic to all the three puzzle`
```
heuristic - euclidean manhattan dotproduct 
```
`heuristic only for water Jug problem`
```
gcdjug
```
`hueuristic only for pancake puzzle`
```
pancake flips dist-flips
```

## Python version
`2.7.12`

## Weblinks and Resources reffered

#Waterjug ::

`https://aakritty.wordpress.com/2014/02/10/solving-the-water-jug-problem/`

#Burnt Pancakes Sorting ::
`https://en.wikipedia.org/wiki/Pancake_sorting`

`Helmert, Malte. "Landmark heuristics for the pancake problem." Third Annual Symposium on Combinatorial Search. 2010.`

#Discussions with other student
#Program problematic part
Not able to run pancake test cases on bfs, dfs in 30 minutes
##Development Environment
`Centos`
 
## All typescripts - created using script command are in folder PuzzleSolver/typescriptfolder

`Type script name convention`

``` typescript.test_cities.config.bfs``` - for bfs on test_cities.config file
``` typescript.test_cities.config.astar.dotproduct``` - for A* on test_cities.config file with heuristic dotproduct
