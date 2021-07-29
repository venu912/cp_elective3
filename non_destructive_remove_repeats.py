# nondestructiveRemoveRepeats(L)
# Write the function nondestructiveRemoveRepeats(L), which takes a list L and nondestructively returns a new list in which any repeating elements in L are removed.
# Specify the time complexity based on the solution that you have given.

# Here are the sample test cases.
# For example:
# assert(nondestructiveRemoveRepeats([1, 3, 5, 3, 3, 2, 1, 7, 5]) == [1, 3, 5, 2, 7])
# assert(nondestructiveRemoveRepeats([1, 5, 3, 3, 2, 1, 7, 5]) == [1, 5, 3, 2, 7])
# assert(nondestructiveRemoveRepeats([1, 2, 3, 5, 3, 3, 2, 1, 7, 5]) == [1, 2, 3, 5, 7])

def nondestructiveRemoveRepeats(L):
    empty=[]
    empty.append(L[0])
    for i in range(len(L)):
        c=0
        j=i
        if(i>0):
            while(j):
                if(L[i]!=L[j-1]):
                    j-=1
                else:
                    c+=1
                    break
            if(c==0):
                empty.append(L[i])
    return empty


assert(nondestructiveRemoveRepeats([1, 3, 5, 3, 3, 2, 1, 7, 5]) == [1, 3, 5, 2, 7])
assert(nondestructiveRemoveRepeats([1, 5, 3, 3, 2, 1, 7, 5]) == [1, 5, 3, 2, 7])
assert(nondestructiveRemoveRepeats([1, 2, 3, 5, 3, 3, 2, 1, 7, 5]) == [1, 2, 3, 5, 7])
print ("All test cases passed....")