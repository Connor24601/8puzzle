We imported time and tested how long astar (using both numWrongTiles and manhattanDistance) and itdeep took on the same puzzles, scrambled randomly. As you can see, itdeep took 100s of time units longer to complete puzzles. However, both astar methods were able to usually find solutions in under a second. To compare the different astar heuristics, we did a 40 move scramble and did not even attempt to run itdeep on them. Manhattan distance was a much faster heuristic, taking 50s of time units less.

Examples:
25 move scramble
took 13 moves, astar manhattan took 0.005 sec, astar numWrong took 0.186 sec, itdeep took 48.475 sec
took 9 moves, astar manhattan took 0.003 sec, astar numWrong took 0.018 sec, itdeep took 0.732 sec
took 13 moves, astar manhattan took 0.094 sec, astar numWrong took 0.874 sec, itdeep took 23.218 sec
took 13 moves, astar manhattan took 0.163 sec, astar numWrong took 1.088 sec, itdeep took 41.088 sec
took 9 moves, astar manhattan took 0.003 sec, astar numWrong took 0.012 sec, itdeep took 0.342 sec
took 7 moves, astar manhattan took 0.001 sec, astar numWrong took 0.001 sec, itdeep took 0.044 sec

40 move scramble
took 18 moves, astar manhattan took 2.262 sec, astar numWrong took 75.486 sec
took 18 moves, astar manhattan took 2.307 sec, astar numWrong took 105.023 sec
took 20 moves, astar manhattan took 5.343 sec, astar numWrong took 142.483 sec
took 16 moves, astar manhattan took 0.279 sec, astar numWrong took 9.957 sec
took 14 moves, astar manhattan took 0.419 sec, astar numWrong took 2.611 sec
took 2 moves, astar manhattan took 0.0 sec, astar numWrong took 0.0 sec
took 16 moves, astar manhattan took 0.317 sec, astar numWrong took 2.504 sec