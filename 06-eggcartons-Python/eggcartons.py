# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	if(0<eggs<12):
  		return 1
	elif(eggs%12==0):
		a=eggs//10
		return a
	else:
		a=eggs//10
		return a+1
  			
	# your code goes here
	#return 1
