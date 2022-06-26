"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
"""

def balancedBrackets(string):
    open_brackets = "({["
    match_brackets = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in string:
        if char in open_brackets:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if stack[-1] == match_brackets[char]:
                stack.pop()
								
    if len(stack) == 0:
    	return True
    return False


string=input()
print(balancedBrackets(string))

     

