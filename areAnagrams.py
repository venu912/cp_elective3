# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

def areAnagrams(s1, s2):
    str1=s1.lower()
    str2=s2.lower()
    if(len(str1)!=len(str2)):
        return False
    else:
        for i in str1:
            if(i in str2):
                return(str1.count(i)==str2.count(i))
        return False

assert(areAnagrams('Aba','BAA')==True)
assert(areAnagrams('AbAAa','BAaaA')==True)
assert(areAnagrams('AbCaa','BAAac')==True)
assert(areAnagrams('AbBa','BAA')==False)
assert(areAnagrams('AbAAABa','AAbbBAA')==False)
print("All test cases passed")