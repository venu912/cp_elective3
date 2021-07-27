# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
		n=n%(len(s))
		if(len(s)==0 or n==0):
				return s
		elif(n>0):
			s1=s[n:]+s[:n]
			return s1
		elif(n<0):
			s1=s[n:]+s[:n]
			return s1
		
  			
print(fun_rotatestrings('abcd',-5))