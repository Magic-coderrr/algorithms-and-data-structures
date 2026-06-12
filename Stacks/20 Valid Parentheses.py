# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

def isValid(s):
    # if length is odd its not possible that pairs are correct
    if len(s) % 2 != 0:
        return False
        
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        # Is the character a Closing bracket? 
        if char in bracket_map:
            # Safely grab the top of the stack. If stack is empty, grab a dummy '#'
            top_element = stack.pop() if stack else '#'
            
            # Checking if the popped bracket matches the one from our dictionary
            if top_element != bracket_map[char]:
                return False
        
        # Otherwise, it's an Opening bracket. Push it to the stack.
        else:
            stack.append(char)
            
    # If the stack is empty at the end, it's valid!
    return len(stack) == 0

s = "()"
print(isValid(s))
