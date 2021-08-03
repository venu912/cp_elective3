# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(l):
    for i in range(len(l)):
        s=set(l[i])
        if(len(l[i])==len(s)):
            if(s==set(l[0])):
                continue
            else:
                return False
        else:
            return False
    for j in range(len(l)):
        a=[]
        for i in range(len(l)):
            a.append(l[i][j])
        s=set(a)
        if(len(a)==len(s)):
            if()
    return True

print(isLatinSquare([[1,2,3],[2,3,1],[3,1,2]]))    
    
