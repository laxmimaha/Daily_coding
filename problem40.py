"""
Given an array of integers where every integer occurs three times except for one integer, 
which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

"""

from collections import Counter 
def no_of_occurrence(nums):
    # storing the frequencies using Counter
    count = Counter(nums)
    for i in count:
        if(count[i] == 1):
            return i
 
 
a = [6, 1, 3, 3, 3, 6, 6]
print("The element with single occurrence is ",int(no_of_occurrence(a)))
b = [13, 19, 13, 13]
print("The element with single occurrence is ",int(no_of_occurrence(b)))