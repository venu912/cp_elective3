# matrixAdd(L, M)[10 pts]
# Background: we can think of a 2d list in Python as a matrix in math. To add two matrices, L and M, they must have 
# the same dimensions. 
# Then, we loop over each row and col, and the result[row][col] is just the sum of L[row][col] and M[row][col]. For example:
# L = [ [1,  2,  3],
#       [4,  5,  6] ]
# M = [ [21, 22, 23],
#       [24, 25, 26]]
# N = [ [1+21, 2+22, 3+23],
#       [4+24, 5+25, 6+26]]
# assert(matrixAdd(L, M) == N)
# With this in mind, write the function matrixAdd(L, M) that takes two rectangular 2d lists (that we will consider 
# to be matrices) that you 
# may assume only contain numbers, and returns a new 2d list that is the result of adding the two matrices. Return 
# None if the two matrices 
# cannot be added because they are of different dimensions.

# def matrixadd(L, M):
		
# 	N=[]
# 	for i in range(len(L)):
# 			p=[]
# 			for j in range(len(L[0])):
# 					# N[i][j]=L[i][j]+M[i][j]
# 					p.append(0)
# 			N.append(p)

# 	if(len(L)!=len(M) or len(L[0])!=len(M[0])):
#   		#print("a")
#   		return None
# 	# elif(len(L[0])!=len(M[0]) or len(M[0])!=len(M[1])):
#   # 		#print("b")
#   # 		return None
# 	else:
# 		for i in L:
# 			for j in M:
# 				if(len(i)!=len(j)):
# 					return None		
# 				else:
#   					for i in range(len(L)):
#   							for j in range(len(L[0])):
#   									N[i][j]=L[i][j]+M[i][j]
# 				return N

				
# 		# print("c")
# 		# result = [[L[i][j] + M[i][j]  for j in range(len(L[0]))] for i in range(len(L))]
# 		#return N
# print(matrixadd([[1,  2,  3],[4,  5,  6]], [[21, 22, 23], [24, 25, 26]]))

def matrixadd(L, M):
	row1=len(L)
	col1=len(L[0])
	row2=len(M)
	col2=len(M[0])
	r=[]
	for i in range(row1):
		c=[]
		for j in range(col1):
			c.append(0)
		r.append(c)
	if(row1!=row2 or col1!=col2):
		return None
	else:
		for i in L:
			for j in M:
				if(len(i)!=len(j)):
					return None
		
		for i in range(row1):
			for j in range(col1):
				r[i][j]=L[i][j]+M[i][j]
		return r

