# def palindrome(n):
#   m=n
#   sum=0
#   while(n>0):
#     a=n%10
    
#     sum=(sum*10)+a
#     print(sum)
#     n=n//10
#   if(m==sum):
#     return True
#   else:
#     return False



# print(palindrome(121))

def matrixadd(L,M):
  N=[]
  for i in range(len(L)):
    for j in range(len(L[0])):
      a=L[i][j]+M[i][j]
      N.append(a)

  return N

print(matrixadd([[1,2,3],],[[4,5,6]]))