import puzzle 
import sys
import BFS
import DFS
import IDS
#import UCS1
import GS1
import AStar1
import GS2
import AStar2


t=puzzle.TilePuzzle(int(sys.argv[1]))
t.permute(int(sys.argv[2]))
#t.printPuzzle()


#BFS
#search = BFS.Bfs(t)

#DFS
#search = DFS.Depthfs(t)


#IDS
search = IDS.IDepthfs(t,3)

#Greedy1
#search = GS1.Greedy(t)

#Greedy2
#search = GS2.GreedyDepth(t)

#AStar1
#search = AStar1.Astar1(t)

#AStar2
#search = AStar2.Astar2(t)

#UCS1
#search = UCS1.UCS1(t)





