"""
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:
set(key, value): sets key to value. 
If there are already n items in the cache and we are adding a new item,
 then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
"""

class DLL_Node:   
    def __init__(self,key,value):       
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
# Created cache class 
class LRU_Cache(object):
    #intializing cache with capacity
    def __init__(self,capacity):       
        self.my_cache = {}        # intialize cache as empty
        self.capacity = capacity
        self.head = DLL_Node(None,None)
        self.tail = DLL_Node(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
    # function defines adding values into linked list
    def append(self,node):
        previous_tail=self.tail.prev
        self.tail.prev=node
        node.next = self.tail
        previous_tail.next=node
        node.prev= previous_tail
    #fuction defines to delete values in the linked list
    def pop(self,node):
        prenode=node.prev
        postnode=node.next
        prenode.next=postnode
        postnode.prev=prenode
    
    def get(self, key):

        # Retrieve item from provided key. Return -1 if nonexistent.
        
        if key in self.my_cache:
            node=self.my_cache[key]
            self.append(node)
            return node.value
        else:
            return -1
        
    def set(self, key, value):
        if self.capacity <= 0:
            return "invalid capacity cache"
        #create a key and value node in double linked list
        node = DLL_Node(key,value)
        #check if the key is already override the value and make it as most recent used.
        if key in self.my_cache:              
            node = self.my_cache[key]
            self.append(node)
            self.my_cache[key]= node
            return 
        #check if capacity exceed cache capacity  
        if len(self.my_cache) == self.capacity:  
            firstnode = self.head.next
            self.pop(firstnode)                  
            del self.my_cache[firstnode.key]
        #append node to last node
        else:
            self.append(node)
            self.my_cache[key]=node
            pass
#TEST CASES :
print("test_case1")        
our_cache = LRU_Cache(5)    
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(3))       # return 3
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3))      # returns 3 

print("Test Case 2:")
our_cache= LRU_Cache(0)
our_cache.set(2,2)           #returns invalid capacity cache
print(our_cache.get(2))

print("Test Case 3:")
our_cache = LRU_Cache(3)      
our_cache.set(1,9)            #returns nothing as the value and key are not same 


print("Test Case 4")
our_cache = LRU_Cache(4)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2      
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(2))  

print("Test Case 5")
our_cache = LRU_Cache(1)       #return Nothing
our_cache.set(None, None); 

print("Test Case 6")
our_cache = LRU_Cache(-1)       #return Nothing
our_cache.set(5, 5); 
print(our_cache.get(5))       #returns -1
