# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2




def fun_nth_additive_prime(n):
		found=1
		guess=1
		count=0
		while(found):
			if(additive_prime(guess)):

				if(n==count):
					found=0
					return guess

				guess=guess+1
				count+=1
			else:
				guess=guess+1

def additive_prime(n):
		sum=0
		while(n):
				m=n%10
				sum=sum+m
				n=n//10
		if(isprime(sum)):
  			return sum

  	

def isprime(x):
		if(x==2):
				return True
		else:
				for i in range(2,x//2+1):
						if(x%i==0):
								return False
		return True

	