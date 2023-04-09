"""
    Reverse the order of the String
    Find the hidden message by reversing a string using a stack
"""

import stack_class

string = "gninraeL nIdekniL htiw tol a nraeL"

reversed_string = ""
s = stack_class.Stack()

for char in string:
    s.push(char)

while not s.is_empty():
    reversed_string += s.pop()



print(reversed_string)
