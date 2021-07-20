# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	# Your code goes here
	j=0
	b=0
	n=len(a)-1
	c=0
	for i in range(len(a)):
		b+=a[i][j]
		j+=1
		c+=a[i][n]
		n-=1
	
	if(b==c):
		for i in range(len(a)-1):
			if(sum(a[i])==sum(a[i+1])):
					continue
			else:
					return False
	
		j=0
		p=0
		q=0
		r=0
		for i in range(len(a)):
			p+=a[i][j]
			q+=a[i][j+1]
			r+=a[i][j+2]
		if(p==q==r):
				return True
		else:
				return False

	else:
		return False
	
# print(ismostlymagicsquare([[2, 7, 6], [9, 5, 1], [4, 3, 8]]))
# print(ismostlymagicsquare([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))