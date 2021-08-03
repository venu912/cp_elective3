# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def recursion_powersof3ton(n):
	empty=[]
	if(n<1):
			return None
	else:
			return powerof3ton(n,empty)

def powerof3ton(n,empty,i=0,total=0):
	total=(3**i)
	if(total<=n):
			empty.append(total)
	i=i+1
	if(total>=n):
  		return empty
	return powerof3ton(n,empty,i,total)

		
print(recursion_powersof3ton(10.5))

