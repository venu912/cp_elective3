# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2




def fun_nth_additive_prime(n):
	found = 0
	guess = 0
	while (found <= n):
			guess += 1
			if (isprime(guess) and additive_prime(guess)):
					found += 1
	return guess

def additive_prime(n):
	sum=0
	while(n):
			m=n%10
			sum=sum+m
			n=n//10
	if(isprime(sum)):
			return sum

def isprime(x):
		if(x<2):
				return False
		for i in range(2,x):
				if(x%i==0):
						return False
		return True

#(0,2),(1,3),(5,23),(7,41),(20,157),(25,197)
# print(fun_nth_additive_prime(67))
# print(fun_nth_additive_prime(0))
# print(fun_nth_additive_prime(1))
# print(fun_nth_additive_prime(25))
# print(fun_nth_additive_prime(4))
# print(fun_nth_additive_prime(5))


	