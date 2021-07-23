# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



#import math

def fun_nearestkaprekarnumber(n):
    if(kaprekarnumber(n)):
        return n
    else:
        a=n
        for i in range(1,n):
            if(i%2!=0):
                a=a-i
                if(kaprekarnumber(a)):
                    return a
            else:
                a=a+i
                if(kaprekarnumber(a)):
                    return a 
                
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
        z=z*10    
    c=y//z
    d=y%z
    e=c+d
    if(n==e):
        return e
    else:
        c=str(c)
        d=str(d)
        while(len(c)):
            if(c[-1]=='0'):
                c=c[0:-1]
            else:
                break
        while(len(d)):
            if(d[-1]=='0'):
                d=d[0:-1]
            else:
                break
        if(len(c)==0 or len(d)==0):
            return False
        sum=int(c)+int(d)
        if(sum==n):
            return True
    return False

print(fun_nearestkaprekarnumber(3861))
print(fun_nearestkaprekarnumber(4878))
print(kaprekarnumber(4879))
print(kaprekarnumber(3861))