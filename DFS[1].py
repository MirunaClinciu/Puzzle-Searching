
import sys
from random import randint
import node
import puzzle
from stack import Stack
import copy
import time

#########pag  88

class Depthfs:
	def __init__(self, initialpuzzle): 
		initialtime=time.time()
		stack=Stack()
		moves=initialpuzzle.moves
		stack.push(initialpuzzle)

		while not stack.isEmpty():

			k = stack.pop()
			k.printPuzzle()

			if k.checkPuzzle():
					
				print "corect"
				return True

			else:
				for move in moves:
					aux = copy.deepcopy(k) #this is a copy of our puzzle
					aux.doMove(move)
					aux.printPuzzle()
					stack.push(aux)
			print str(time.time() - initialtime)



