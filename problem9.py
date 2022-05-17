"""
Given  a list of integers, write a function that returns the largest
sum of non- adjacent numbers.Numbers can be 0 0r negative 
For example,
[2,4,6,2,5] should return 13,since we pick 2,6,5.
[5,1,1,5] should return 10, since we pick 5 and 5.

"""
import math


def maxlength(arr):
    if(len(arr) == 0):
        return 0
    if(len(arr) == 1):
        return arr[0]
    first = 0
    second = 0
    for i in range(len(arr)):
        n_sum = max(arr[i] + second, first)
        second = first
        first = n_sum
    return first
list1 = [2,4,6,2,5]
print(maxlength(list1))
list2 = [5,1,1,5]
print(maxlength(list2))