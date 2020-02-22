import sys
from random import randint
import node
import puzzle
from stack import Stack
import copy
import time


class IDepthfs:
	def __init__(self,initialpuzzle,depth): 
		initialtime=time.time()
		stack=Stack()
		moves=initialpuzzle.moves
		stack.push(initialpuzzle)
		explored=[]

		while not stack.isEmpty():
           
			node = stack.pop()
			explored.append(node)
			node.printPuzzle()
			if node.checkPuzzle():
				return depth

			else:
				print depth
				for move in moves:
					aux = copy.deepcopy(node) #this is a copy of our puzzle
					if aux.depth < depth:
						aux.doMove(move)
						aux.printPuzzle()
						stack.push(aux)
						depth+=1
						print depth
						print str(time.time() - initialtime)
	


