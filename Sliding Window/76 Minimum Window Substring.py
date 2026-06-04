# Given two strings s and t of lengths m and n respectively, return the minimum window substring 
# of s such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

def minWindow(s, t):
    # Frequency maps for the target string and our current sliding window
    target_map = {}
    window_map = {}

    for char in t:
        target_map[char] = target_map.get(char, 0) + 1
        
    # 'need' is the total number of unique characters required
    # 'have' tracks how many of those characters currently meet the required frequency
    have = 0
    need = len(target_map)
    
    min_length = float('inf')
    left = 0
    best_left, best_right = -1, -1
    
    for right in range(len(s)):
        char = s[right]
        window_map[char] = window_map.get(char, 0) + 1
        
        # If the current character fulfills its required frequency, update 'have'
        if char in target_map and window_map[char] == target_map[char]:
            have += 1
            
        # Once the window is fully valid, attempt to shrink it from the left
        while have == need:
            current_length = right - left + 1
            
            # Record the new minimum window boundaries
            if current_length < min_length:
                min_length = current_length
                best_left = left
                best_right = right
                
            # Drop the leftmost character and update state
            left_char = s[left]
            window_map[left_char] -= 1

            # If dropping this character breaks the window's validity, update 'have'
            if left_char in target_map and window_map[left_char] < target_map[left_char]:
                have -= 1
                
            left += 1

    return s[best_left : best_right + 1] if min_length != float('inf') else ""

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s,t))