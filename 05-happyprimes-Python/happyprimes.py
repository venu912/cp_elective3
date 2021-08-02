# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def ishappyprimenumber(n):
    if(ishappynumber(n)):
        if(isprime(n)):
            return True
        else:
            return False
    else:
        return False


def ishappynumber(n):
        if(n==1):
                return True
        elif(n<1):
                return False
        a=sum_of_digits(n)
        if(a==1):
                return a
        elif(a<10):
                return False

def sum_of_digits(n):
	sum=0
	while(1):
		m=n%10
		sum=sum+m*m
		n=n//10
		if(n==0):
			if(sum<10):
				return sum
			n=sum
			sum=0

def isprime(n):
    for i in range(2,n):
         if(n%i==0):
             #print(i)
             return False
    return True
print(isprime(833))
#print(ishappyprimenumber(833))