"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
Find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

def time_period(n):
    time_count = [ 0 for i in range(1000)]
    for i in n:
        time_count[i[0]] += 1
        time_count[i[1]] += -1
    rooms =0
    temp = 0
    for i in time_count:
        temp +=i
        if(temp >rooms):
            rooms = temp
    return rooms
print(time_period([[30,75],[0,50],[60,150]]))
print(time_period([]))