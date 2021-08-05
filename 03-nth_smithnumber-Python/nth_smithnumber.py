# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22


# def fun_nth_smithnumber(n):
#         found = 0
#         guess = 0
#         while (found <= n):
#                 guess += 1
#                 if (smithnumber(guess)):
#                         found += 1
#         return guess

# def smithnumber(n):
#     empty=[]
#     a,b=isprime(n,empty,sum=0)
#     c=count_digits(n)
#     if(a!=[]):
#         if(b==c):
#             return True
#         else:
#             return False
#     else:
#         return False
    

# def isprime(p,empty,sum=0,i=2):
#     for i in range(2,p):
#         if(p%i==0):
#                 empty.append(i)
#                 sum+=i
#                 return isprime(p//i,empty,sum,i=2)
#         else:
#             continue
#     #empty.append(p)
#     sum+=(p)
#     #print(sum)
#     sum=count_digits(sum)
#     #print(empty,sum)
#     return empty,sum

# def count_digits(n,count=0):
#     #count=0
#     while(n):
#         m=n%10
#         count+=m
#         n=n//10
#     print(count)
#     if(count>9):
#         return count_digits(count)
#     return count


# def smithnumber(n):
#     empty=[]
#     for i in range(2,n):
#         if(isprime(i) and (n%i==0)):
#             empty.append(i)
            

# def isprime(n):
#     for i in range(2,n):
#         if(i%2==0):
#             return False
#     return True

# print(smithnumber(105))
#print(fun_nth_smithnumber(17))





def isprime(n):
    if n==1:
        return False
    if n==2:
        return True    
    for i in range(2, (n//2)+1):
        if(n%i==0):
            return False
    else:
        return True
       
def smith(n):
    if(isprime(n)!=True):
        k = n
        factorslist = []
        factorssum=0
        digitsum = 0
        if n==1:
            return False
        for i in range(2,(n//2) + 1):
            if(isprime(i)==True) and (n%i==0):
                factorslist.append(i)
         
        for an in str(n):
            digitsum+=int(an)
       
        li=[]
        for i in factorslist:
            while (k%i==0 and k!=0):
                li.append(i)    
                factorssum+=i
                k=k//i
      
        repeatsuminfactors = 0        
        for j in li:
            if(j>9):
                for d in str(j):
                    repeatsuminfactors+=int(d)
            else:
               repeatsuminfactors+=j
        
        if(digitsum==repeatsuminfactors):
            return True
        else:
            return False
def fun_nth_smithnumber(n):
    count=0
    position=1
    result = 0
    while(n+1!=count):
        if(smith(position)==True):
            count+=1
            result = position
        position+=1
    return result

