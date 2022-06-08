
"""
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. 
If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. 
All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', 
you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A',
 you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
"""

def itinerary(llist, start):
     
    itinerary_list = []
    itinerary_list.append(start)
    #looping the complete list
    while len(llist) >= 1:
        destination = None
        directions = {}
        #looping each element in the list
        for item in llist:
            
            if item[0] == start:
                directions[item[0]] = item[1]

        if len(directions) >= 1:
            destination = min(directions.values())
            remove_tuple = (start, destination)
            llist.remove(remove_tuple)
            itinerary_list.append(destination)
            start = destination
        else:
            return None
            

    return itinerary_list

#given  list of stations start and destination and a starting point
print(itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 
    'YUL'))

print(itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 
    'COM'))

print(itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 
    'A'))
print(itinerary([('A', 'B'), ('B', 'C'),('C', 'A')], 
    'B'))

