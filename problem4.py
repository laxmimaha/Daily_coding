"""
 Problem 4:

 Given an array of integers, find the first missing positive integer in linear time and constant space .
 in other words, find the lowest positive integer that does not exit in the array. the array can contain 
 duplictaes and negative numbers as well.

 For example, the input
 [3,4,1,-1] should give 2.
 the input [1,3,4] should give 3.
"""
def positiveMissingNo(list1):
 #defining a function for finding least integer in list which is not found
    n = len(list1)
#loop for neglacting the zero and negative integers
    for i in range(n) :
        if (list1[i] <= 0 or list1[i] > n):
            i = i+1
        value = list1[i]

        while (list1[value - 1] != value):
            temp = list1[value - 1]
            list1[value - 1] = value
            value = temp

            if (value <= 0 or value > n):
                break
    
    for i in range(n):
       
        if (list1[i] != i + 1) :
            return i + 1
    return n + 1
 

list1= [ 1, 3, 7, 6, 8, 4, -10, 15 ]

missing = positiveMissingNo(list1)
print( "The smallest positive", missing)
