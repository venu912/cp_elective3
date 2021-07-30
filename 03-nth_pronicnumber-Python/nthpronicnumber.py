# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	found = 0
	guess = 0
	while (found < n):
			guess += 1
			if (pronic_number(guess)):
					found += 1
	return guess

def pronic_number(n):
	for i in range(1,n):
		if(i*(i+1)==n):
				return True
		elif(i>=(n//2)+1):
  			return False
		

print(nthpronicnumber(25))
