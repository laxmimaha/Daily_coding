"""Problem 2 :
     Given an array of integers, return a new array such that each element at index i of the new array is the product of all
     the numbers in the original array except the one at i.
     For example,
     if our input was [1,2,3,4,5], the 
     expected output would be 
     [120,60,40,30,24]


[1,2,3,4,5]
[120,60,40,30,24]
[2*3*4*5]
[1*3*4*5]
[1*2*4*5]
[1*2*3*5]
[1*2*3*4]
[120,60,40,30,24]

"""
def prod(list1):
    list2 = []
    p = 1
    
    for i in range(len(list1)):
        for j in range(len(list1)):
            if(i == j):
                j = j+ 1
            else:
                
                p = list1[j] * p
        list2.append(p)
        p = 1
    return list2
n = int(input("enter the element size:"))
list1 = []
for i in range(n):
    ele = int(input())
    list1.append(ele)
print(list1)
print(prod(list1))
            

          
        