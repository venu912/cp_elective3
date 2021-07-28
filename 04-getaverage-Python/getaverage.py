# Write the function getAverage(values) that takes a string of 
# comma-separated non-negative integer values, and returns their 
# average as a float (even though the values themselves are integers). 
# Note that some values may not be non-negative integers, and these 
# should be ignored. If there are no integer values, return 0 (do not crash here).
# For example, getAverage('13,excused,14,absent') ignores the two 
# strings and averages 13 and 14 to return 13.5. Also, getAverage('a,b,c') returns 0.




def fun_getaverage(s):
		inp=s.split(",")
		print(len(inp))
		sum=0
		c=0
		avg=0
		for i in range(len(inp)):
			if(type(inp[i])!=int):
					continue
			else:
				sum+=inp[i]
				c+=1  
		if(c>0):
  			avg=sum/c
		return avg

print(fun_getaverage('13,excused,14,absent'))

