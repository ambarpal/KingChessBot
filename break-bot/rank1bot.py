mov = [[-1,0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
def ab(x):
	if x < 0:
		return -1 * x
	else:
		return x
def getnext(n, me, grid, opp):
	# print "me", me, "opp", opp, grid[5][7]
	x, y = me
	mini = 999999
	j,k = opp
	if j>x:
		if k>y:
			mov = [[1,1], [0,1], [1,0], [-1,1], [1,-1], [-1,0], [0,-1], [-1,-1]]
		elif k==y:
			mov = [[1,0], [1,1], [1,-1], [0,1], [0,-1], [-1,1], [-1,-1], [-1,0]]
		else:
			mov = [[1,-1], [1,0], [0,-1], [1,1], [-1,-1], [0,1], [-1,0], [-1,1]]
	elif j==x:
		if k>y:
			mov = [[0,1], [-1,1], [1,1], [-1,0], [1,0], [-1,-1], [1,-1], [0,-1]]
		else:
			mov = [[0,-1], [-1,-1], [1,-1], [-1,0], [1,0], [-1,1], [1,1], [0,1]]
	else:
		if k>y:
			mov = [[-1,1], [0,1], [-1,0], [1,1], [-1,-1], [1,0], [0,-1], [1,-1]]
		elif k==y:
			mov = [[-1,0], [-1,1], [-1,-1], [0,1], [0,-1], [1,1], [1,-1], [1,0]]
		else:
			mov = [[-1,-1], [-1,0], [0,-1], [-1,1], [1,-1], [0,1], [1,0], [1,1]]

	for m in mov:
		a, b = m
		# if (not (x + a < 1 or x + a > n)) and (not(y + b < 1 or y + b > n )) and (not (grid[y+b][x+a] == 1)):
		if (not (x + a < 1 or x + a > n)) and (not(y + b < 1 or y + b > n )) and (not (grid[x+a][y+b] == 1)):
			h = gethur(x + a, y + b, opp, grid, n)
			if h < mini:
				mini = h
				minim = m

	return me[0]+minim[0], me[1]+minim[1]


def gethur(x, y, opp,grid, n):
	if (x,  y) == opp:
		return 0
	elif ab(opp[0] - x) <= 1 and ab(opp[1] - y) <= 1:
		return 99
	else:
		s=0
		for m in mov:
			a,b=m
			if (not (x + a< 1 or x + a > n)) and (not(y + b < 1 or y + b >n )) and (not (grid[y+b][x+a] == 1)):
				if grid[y+b][x+a]==0 or grid[y+b][x+a]==3:
					s+=1
		if s == 0:
			return 99999
		elif s == 1:
			return 3
		elif s == 2:
			return 2
		else:
			return 1
