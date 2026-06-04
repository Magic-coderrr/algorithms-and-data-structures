# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.
# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
def checkInclusion(s1, s2):
    window_size = len(s1)
    if window_size > len(s2):
        return False
        
    count_s1 = {}
    window_count = {}
    
    for i in range(window_size):

        char1 = s1[i]
        count_s1[char1] = count_s1.get(char1, 0) + 1
        
        char2 = s2[i]
        window_count[char2] = window_count.get(char2, 0) + 1
        
    if count_s1 == window_count:
        return True
        
    for i in range(window_size, len(s2)):
        new_char = s2[i]
        old_char = s2[i - window_size]
        
        window_count[new_char] = window_count.get(new_char, 0) + 1
        
        window_count[old_char] -= 1
        
        if window_count[old_char] == 0:
            del window_count[old_char]
            
        if count_s1 == window_count:
            return True
            
    return False

s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))