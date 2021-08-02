# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22


def fun_nth_smithnumber(n):
    return 1

def smithnumber(n):
    empty=[]
    return isprime(n,empty,sum=0)

# def smithnumber(n,p=2):
#     sum=0
#     if(isprime(p) and div(n,p,sum)):
#         if(isprime(m)):
#             True

def isprime(p,empty,i=2,sum=0):
    for i in range(2,p):
        if(p%i==0):
            empty.append(i)
            sum+=i
            return isprime(p//i,empty,i=2,sum)
        else:
            continue
    empty.append(p)
    #sum+=p
    return empty,sum

print(smithnumber(378))

# def div(n,p,sum):
#     m=n
#     if(n%p==0):
#         sum+=p
#         m=n//2
#         return sum,m
#     else:
#         return smithnumber(n,p+1)