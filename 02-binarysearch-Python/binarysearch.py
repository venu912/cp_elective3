"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    low=0
    high=len(input_array)
    #middle=(low+high-1)//2
    exist_count=input_array.count(value)
    if(exist_count>0):
        a=search(input_array,value,low,high)
        return a
    else:
        return -1

def search(input_array,value,low,high):
    middle=(low+high)//2
    if(input_array[middle]==value):
        return middle
    elif(input_array[middle]>value):
        return search(input_array,value,low,middle-1)
    elif(input_array[middle]<value):
        return search(input_array,value,middle+1,high)
    

#print(binary_search([1,3,9,11,15,19,29],15))
#print(binary_search([1,3,9,11,15,19,29],25))

