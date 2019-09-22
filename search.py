# search.py


import puzzle8
from heapq import *


def numWrongTiles(state):
	'''gives number of tiles differing between given state and solution state'''
	numWrong = 0
	for i in range(0,9):
		if puzzle8.getTile(state,i) != 0 and \
			puzzle8.getTile(state,i) != puzzle8.getTile(puzzle8.solution(),i):
			numWrong += 1
	return numWrong



def findTile(state, tileNum):
	'''returns position 0-8 of a given tile for a given state. 
	helper function for manhattan distance'''
	for i in range(0,9):
		if puzzle8.getTile(state,i) == tileNum:
			return i


def manhattanDistance(state):
	'''gives sum of manhattan distance of all tiles from their
	respective places in the solution state.'''
	dist = 0
	for i in range(0,9):
		tile = puzzle8.getTile(state, i)
		if tile == 0:
			continue
		loc1 = puzzle8.xylocation(i)
		loc2 = puzzle8.xylocation(findTile(puzzle8.solution(), tile))
		dist += abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])
	return dist


def recurDeep(state, depthRemaining):
	'''searches for a path with depth given.
	   if not found, returns [-1].'''
	if state == puzzle8.solution():
		return []
	if depthRemaining <= 0:
		return [-1]

	neighbors = puzzle8.neighbors(puzzle8.blankSquare(state))
	depthRemaining -= 1
	for neighbor in neighbors:
		newState = puzzle8.moveBlank(state, neighbor)
		possiblePath = recurDeep(newState, depthRemaining)
		if -1 not in possiblePath:
			path = [neighbor] + possiblePath
			return path
	return [-1]


def itdeep(state):
	done = False
	depth = 0
	possiblePath = []
	while not done:
		possiblePath = recurDeep(state, depth)
		done = -1 not in possiblePath
		depth += 1
	return possiblePath


def astar(state, heuristic):
	queue = []
	# prevStateDict[state] = (previous state, move to get there, g)
	prevStateDict = {}
	prevStateDict[state] = (None, None, 0)
	heappush(queue, (heuristic(state), state)) 
	
	while queue:
		f, state = heappop(queue) # f is total astar cost
		
		if state == puzzle8.solution():
			prevState = prevStateDict[state]
			path = []
			#print("backtracing")
			while prevState[0]:
				path = [prevState[1]] + path
				prevState = prevStateDict[prevState[0]]
			return path

		g = f - heuristic(state) # g is cost in moves to get to current state
		neighbors = puzzle8.neighbors(puzzle8.blankSquare(state))

		for neighbor in neighbors:
			newState = puzzle8.moveBlank(state, neighbor)
			
			if newState not in prevStateDict:
				prevStateDict[newState] = (state, neighbor, g+1)
			else:
				if prevStateDict[newState][2] > g+1:
					# if we just found a cheaper path to newState, override prevStateDict
					prevStateDict[newState] = (state, neighbor, g+1)


			f = g + 1 + heuristic(newState)
			heappush(queue, (f, newState))

