# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


# import math

# def fun_nth_kaprekarnumber(n):
#         found = 0
#         guess = 0
#         while (found <= n):
#                 guess += 1
#                 if (kaprekarnumber(guess)):
#                         found += 1
#         return guess

def kaprekarnumber(n):
    a=n*n
    y=a
    count1=0
    while(a):
        count1+=1
        a=a//10
    count2=count1
    z=1
    b=count2//2
    while(b):
        z=z*10
        b-=1
    if(count1%2!=0):
        z+=1
    c=y//z
    d=y%z
    e=c+d
    return e

print(kaprekarnumber(45))
print(kaprekarnumber(55))
print(kaprekarnumber(99))
print(kaprekarnumber(2223))
print(kaprekarnumber(9))
print(kaprekarnumber(1))



