import sys
from random import randint
from collections import deque #stack
import time
import node
import puzzle
import checkpuzzle
from PriorityQueue import PriorityQueue
import copy



class Astar1:
	def __init__(self,initialpuzzle):
		explored=[] # explored nodes,expanded and open
		node1 = node.Node(0,0,initialpuzzle, 0)
		node1.puzzle.printPuzzle()
		self.heuristic1(node1.puzzle)
		print self.heuristic1(node1.puzzle)
		priorityQueue=PriorityQueue()

		priorityQueue.push(node1.puzzle, self.heuristic1(node1.puzzle) + node1.puzzle.depth)
		print priorityQueue.isEmpty()

		while not priorityQueue.isEmpty():

			k = priorityQueue.pop()
			#k.printPuzzle()

			if k.checkPuzzle():
					
				print "corect"
				break
				
                
			else:
				for move in k.moves:
					aux = copy.deepcopy(k) #this is a copy of our puzzle
					aux.doMove(move)
					aux.depth += 1
					#aux.printPuzzle()
					priorityQueue.push(aux,self.heuristic1(aux))




	def heuristic1(self, puzzle):
		count=1

		wrongTiles = 0
		for y in range(0,puzzle.size):
			for x in range(0,puzzle.size):
				if puzzle.puzzle[x][y]!=(count%(puzzle.size*puzzle.size)):

					wrongTiles += 1
				count+=1

		return wrongTiles
