# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
		found = -1
		guess = 0
		while (found < n):
				guess += 1
				if (property309(guess)):
						found += 1
		return guess
  	
def property309(n):
	a=n*n*n*n*n
	#print(a)
	b=str(a)
	c='0123456789'
	for i in c:
		if(i in b):
			continue
		else:
			return False
	return True

#print(property309(121))
print(nthwithproperty309(309))