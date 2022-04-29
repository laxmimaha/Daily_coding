"""
Given a list of numbers and a number k, return whether any two numbers from
the list add up to k.

For example,
  [10,15,3,7] and k of 17,
  return true since 10+7 is 17

"""


def sum_ele(list1,key):
    sor = sorted(list1)
    for i in range(len(sor)):
        for j in range(1,len(sor)):
            var = sor[i] + sor[j]
            if(var == key):
                print(sor[i],sor[j])
                
            j = j + 1
n = int(input("Enter the size of list : "))
print("\n")
numList = list(map(int, input("Enter the list numbers separated by space ").strip().split()))[:n]
print("User List: ", numList)
k = int(input("target Element after adding two elements in list:"))
print(sum_ele(numList,k))

        

