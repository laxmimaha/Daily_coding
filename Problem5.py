"""
cons(a,b) constructs a pair , and car(pair) and cdr(pair)
returns first element and last element of the pair . For example , 
car(cons(3,4)) returns 3,
and cdr(cons(3,4)) returns 4
"""
# defining the inner functions is the solution for this problem
def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair
def car(pair):
    def first_ele(a,b):
        return a
    return pair(first_ele)
def cdr(pair):
    def second_ele(a,b):
        return b
    return pair(second_ele)
print(car(cons(3,4)))
print(cdr(cons(3,4)))
