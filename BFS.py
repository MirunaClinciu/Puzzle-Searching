import sys
from random import randint
import node
import puzzle
from stack import Stack
import copy
from collections import deque
import time
from PriorityQueue import PriorityQueue

class Bfs:
	def __init__(self, initialpuzzle): 
		initialtime=time.time()
		priorityQueue=PriorityQueue()
		moves=initialpuzzle.moves
		priorityQueue.push(initialpuzzle,0)

		while not priorityQueue.isEmpty():

			k = priorityQueue.pop()
			k.printPuzzle()

			if k.checkPuzzle():
					
				print "corect"
				print str(time.time() - initialtime)
				return True

			else:
				for move in moves:
					aux = copy.deepcopy(k) #this is a copy of our puzzle
					aux.doMove(move)
					aux.printPuzzle()
					priorityQueue.push(aux,0)
					print str(time.time() - initialtime)



