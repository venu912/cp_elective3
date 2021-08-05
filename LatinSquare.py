# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(a):
    # Your code goes here...
    N = len(a)
    rows = []
    for i in range(N):
        rows.append(set([]))
    cols = []
    for i in range(N):
        cols.append(set([]))
    invalid = 0
    for i in range(N):
        for j in range(N):
            rows[i].add(a[i][j])
            cols[j].add(a[i][j])
  
            if (a[i][j] > N or a[i][j] <= 0) :
                invalid += 1
    numrows = 0
    numcols = 0
  
    for i in range(N):
        if (len(rows[i]) != N) :
            numrows+=1
        if (len(cols[i]) != N) :
            numcols+=1
    if (numcols == 0 or numrows == 0 and invalid == 0) :
        return "Yes"
    else:
        return "No"


assert(isLatinSquare([[1,2],[3,1]])=="Yes")
print("All Passed")

#print(isLatinSquare([[1,2,3],[2,3,1],[3,1,2]]))    
    
