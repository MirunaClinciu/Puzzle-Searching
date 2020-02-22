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



class Astar2:
	def __init__(self,initialpuzzle):
		initialtime=time.time()
		explored=[] # explored nodes,expanded and open
		node1 = node.Node(0,0,initialpuzzle, 0)
		node1.puzzle.printPuzzle()
		self.heuristic2(node1.puzzle)
		print self.heuristic2(node1.puzzle)
		priorityQueue=PriorityQueue()

		priorityQueue.push(node1.puzzle, self.heuristic2(node1.puzzle) + node1.puzzle.depth)
		print priorityQueue.isEmpty()

		while not priorityQueue.isEmpty():

			k = priorityQueue.pop()
			#k.printPuzzle()

			if k.checkPuzzle():
					
				print "corect"
				print str(time.time() - initialtime)

				break
				
                
			else:
				for move in k.moves:
					aux = copy.deepcopy(k) #this is a copy of our puzzle
					aux.doMove(move)
					aux.depth += 1
					aux.printPuzzle()
					priorityQueue.push(aux,self.heuristic2(aux))
					print str(time.time() - initialtime)





	def heuristic2(self, puzzle):
		s=0
		for c in range(0,3):
			for r in range(0,3):
				val=puzzle.puzzle[r][c]-1
				gc=val%3
				gr=val/3
				if val == -1:
					s+=abs(2-r)+abs(2-c)
				else:
					s+=abs(gr-r)+abs(gc-c)
		return s
