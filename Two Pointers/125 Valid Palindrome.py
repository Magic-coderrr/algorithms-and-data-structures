# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

def isPalindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:

        if not s[left].isalnum():
            left += 1
            
        elif not s[right].isalnum():
            right -= 1
            
        else:
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))