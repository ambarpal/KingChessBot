from rank1bot import *
from mybot import *

n = 4
board = [[0 for x in range(n + 1)] for x in range(n + 1)]
move = 1
p0 = 1, 1
p1 = n, n
def valid(i, j):
	if (i >= 1 and i <= n and j >= 1 and j <= n): return 1
	else: return 0
def validMove(i, j, player):
	if (player == 0):
		if (valid(i,j) and abs(i - p0[0]) <= 1 and abs(j - p0[1]) <= 1 and board[i][j] == 0): return 1
		else: return 0
	else:
		if (valid(i,j) and abs(i - p1[0]) <= 1 and abs(j - p1[1]) <= 1 and board[i][j] == 0): return 1
		else: return 0

won = -1
while (won == -1):
	print "Move #" + str(move)
	print "Player #0:" + str(p0[0]) + " " + str(p0[1])
	print "Player #1:" + str(p1[0]) + " " + str(p1[1])

	for i in range(1, n + 1):
		for j in range (1, n + 1):
			if p0 == (i,j): print "P",
			elif p1 == (i,j): print "A",
			else: print board[i][j],
		print

	if (move % 2 == 0):
		x,y = getnext(n, p0, board, p1)
		print "Player 0 requests: ", x, y
		if validMove(x, y, 0) == 1:
			board[p0[0]][p0[1]] = 1
			if (x, y) == p1: won = 2
			p0 = x, y
		else:
			print "Invalid"
			won = 3
	else:
		x,y = makeMove(board, p1, p0)
		print "Player 1 requests: ", x, y
		if validMove(x, y, 1) == 1:
			board[p1[0]][p1[1]] = 1
			if (x,y) == p0: won = 3
			p1 = x, y
		else:
			print "Invalid"
			won = 2
	move = move + 1

if won == 2: print "player 0 won"
elif won == 3: print "player 1 won"
else: print "drawn"
