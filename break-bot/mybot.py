def makeMove(board, myPos, oppPos):
	c = raw_input()
	print c
	a, b = myPos
	if c == 'w': return a - 1, b
	elif c == 'a': return a, b - 1
	elif c == 's': return a + 1, b
	elif c == 'd': return a, b + 1
	elif c == 'q': return a - 1, b - 1
	elif c == 'e': return a - 1, b + 1
	elif c == 'z': return a + 1, b - 1
	elif c == 'c': return a + 1, b + 1	
	#a, b = list(map(int, raw_input().split(' ')))
	# return a, b