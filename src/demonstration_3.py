"""
Given a list of integers `lst`, any integer with a frequency that is equal to its value is considered a **lucky integer**.

Write a function that returns the lucky integer from the array. If the array contains multiple lucky integers, return the largest one. If there are no lucky integers return -1.

**Example 1**:

Input: arr = [2,3,3,3,4]
Output: 3

**Example 2**:

Input: arr = [1,2,2,3,3,3,4,4,4,4]
Output: 4

**Example 3**:

Input: arr = [1,1,2,2,2]
Output: -1
"""
def find_lucky(lst):
    # Your code here
    # If the number shows more than once, consider it lucky
    # if there are multiple lucky numbers return the last one
    # if there are no lucky numbers return -1
    counter = 0
    num = lst[0] 
      
    for i in lst: 
        luckynumber = lst.count(i) 
        if(luckynumber> counter): 
            counter = luckynumber
            num = i 
  
    return num 

print(find_lucky([1,2,2,3,3,3,4,4,4,4]))

def find_lucky(lst):
    lucky = []
    string = ''.join(map(str, lst))
    for char in string:
        if int(char) == string.count(char):
            lucky.append(char)
    if not lucky:
        return -1
    return max(lucky)
print(find_lucky(lst))

# Overall runtime (with count in loop)
# constant + n log n (for the sort) + n * n --> O(n^2)
# 1 + n log n + n^2
# runtime with count outside of loop:
# 1 + n log n + n --> n log n
# space complexity: 0(n)

output = -1 # constant
# Sort the list from the largest to smallest


# count the number of times each element appears in the list
counts = {}

for number in lst: # O(n)
    if number not in counts:
        counts[number] = 0
    counts[number] += 1

set_list = set(lst)

for number in set_list # How many times does the loop run?
    count = counts[number] # O(1)
    if number == count: # O(1)
        output = number # O(1)
    return output