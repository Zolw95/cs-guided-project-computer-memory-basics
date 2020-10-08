"""
In order to solve this challenge you will need to [review the rules of Roman
Numerals](https://www.mathsisfun.com/roman-numerals.html).

Given a Roman Numeral (as a string), convert it to an integer. Your input is
guaranteed to be a Roman Numeral value from 1 to 3999.

Example 1:

Input: "IV"
Output: 4

Example 2:

Input: "XII"
Output: 12

Example 3:

Input: "MCMLXXXIV"
Output: 1984
"""
roman_numerals = [
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1),]
def roman_to_integer(roman):
    # Your code here
    index = 0
    result = 0
    while index < len(roman):
        for n, value in roman_numerals:
            print("N", n)
            print("value", value)
            print("romannumerals", roman_numerals)
            if roman.startswith(n, index):
                result += value
                index += len(n)
                break
    # print(result)
roman_to_integer("MCMLXXXIV")



