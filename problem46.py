"""
Given a string, find the longest palindromic contiguous substring. 
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". 
The longest palindromic substring of "bananas" is "anana".


"""
def longest_palindrome(s):
    list1 = []
    longest = ''
    for i in range(len(s)):
        for j in range(1, len(s)+1):
            substring = s[i:j]
            if (substring[::-1] == substring) and len(substring) > len(longest):
                longest = substring
                list1.append(longest)
    
    return  list1 , longest


sub ="aabcdcb" 
print(longest_palindrome(sub))