# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def fun_recursion_onlyevendigits(l): 
	if(len(l)==0):
		return 0
	i=0
	sum=0
	a=only_evendigits(l,i,sum)
	return a

def only_evendigits(l,i,sum):
	if(i<len(l)):
			i+=1
			j=0
			b=only_even(l[i],str(l[i]),j)

def only_even(p,q,j):
	if(j<len(q)):
		j+=1
		if(p%10==0):
  		
			p=p//10
			return only_even(p,q,j)
		elif((p//10)%2==0):
  			total=total*
				p=p//10
				return only_even(p,q,j)
	else:
		return 