import sys
from random import randint
from collections import deque #stack
import time
import node
import puzzle
import checkpuzzle
from PriorityQueue import PriorityQueue
import copy
import time



class Greedy:
	def __init__(self,initialpuzzle):
		initialtime=time.time()
		explored=[] # explored nodes,expanded and open
		node1 = node.Node(0,0,initialpuzzle, 0)
		node1.puzzle.printPuzzle()
		self.heuristic1(node1.puzzle)
		priorityQueue=PriorityQueue()

		priorityQueue.push(node1.puzzle,self.heuristic1(node1.puzzle))


		while not priorityQueue.isEmpty():
			k = priorityQueue.pop()
			#k.printPuzzle()

			if k.checkPuzzle():	
				print k.checkPuzzle
				print "corect"
				break
				  
			else:
				for move in k.moves:
					aux = copy.deepcopy(k) #this is a copy of our puzzle
					aux.doMove(move)
					aux.printPuzzle()
					priorityQueue.push(aux,self.heuristic1(aux))
					print str(time.time() - initialtime)



	def heuristic1(self, puzzle):
		count=1

		wrongTiles = 0
		for y in range(0,puzzle.size):
			for x in range(0,puzzle.size):
				if puzzle.puzzle[x][y]!=(count%(puzzle.size*puzzle.size)):

					wrongTiles += 1
				count+=1

		return wrongTiles
