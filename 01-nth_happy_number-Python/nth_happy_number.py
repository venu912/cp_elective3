# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)


def nth_happy_number(n):
	found = 0
	guess = 0
	while (found < n):
			guess += 1
			if (ishappynumber(guess)):
					found += 1
	return guess

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
