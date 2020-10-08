"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
string = "LLAMA"

result = ""
def to_lower_case(string):
    if 65 <= ord(c) and ord(c) <= 90:
        lowercase = ord(c) + 32
        c = chr(lowercase)
        result += c
    return result
print(to_lower_case("LowerCase"))
# newstring = ""
# def to_lower_case(string):
#     # Your code here 
#     # lowercase = string.lower()
#     for i in string:
#         i = ord(i) + 32
#         newstring += chr(i)
#     return newstring
# to_lower_case(string)