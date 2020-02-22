
import sys
from random import randint
import puzzle
from stack import Stack
import copy
from node import node

class UCS1:
	def __init__(self, initialpuzzle): 
		stack=Stack()
		moves=initialpuzzle.moves
		print moves
		stack.push(initialpuzzle)
		explored=set()
		while not stack.isEmpty():

			node = stack.pop()
			cost=
			if node not in explored:
				explored.add(node)

				if node == goal:
					return
				for i in node.adjacentnodes(node):
					if i not in explored:
						tcost=cost+node.cost(node,i)
						stack.push(tcost,i)


