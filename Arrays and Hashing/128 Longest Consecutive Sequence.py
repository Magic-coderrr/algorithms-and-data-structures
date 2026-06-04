# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

def LCS(nums):
    # 1. Creating the Hash Set
    num_set = set(nums)
    longest_streak = 0
    
    # 2. Looping through the numbers
    for num in num_set:
        
        # 3.We Only start counting if it is the beginning of a sequence
        if (num - 1) not in num_set:
            current_num = num
            current_streak = 1
            
            # 4. Counting upwards as high as the sequence goes
            while (current_num + 1) in num_set:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
            
    return longest_streak

nums = [100, 4, 200, 1, 3, 2]
print(LCS(nums)) 