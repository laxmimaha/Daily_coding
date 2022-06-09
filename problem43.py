class Stack:
    
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
        
    def push(self, data):
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()
        
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1
        return self.arr[self.next_index]
    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
    
    def _handle_stack_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range( 2* len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element
    #def get_max(self,data):
a = Stack()
print(a.arr)
a.push(40)
a.push(3)
a.push(29)
a.push(21)
a.push(23)
a.push(25)
a.push(26)
print(a.arr)
print(a.pop())
print(a.pop())
print("maximum elementin stack:", max(a.arr))

