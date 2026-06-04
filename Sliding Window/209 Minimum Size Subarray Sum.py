# Given an array of positive integers nums and a positive integer target, return the minimal length 
# of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

def minSubArrayLen(target, nums):
    min_length = float('inf')
    left = 0
    current_sum = 0 
    
    for i in range(len(nums)):

        current_sum += nums[i]        
        while current_sum >= target:
            min_length = min(min_length, i - left + 1)
            left += 1
            current_sum -= nums[left - 1]
            
    if min_length == float('inf'):
        return 0
    else:
        return min_length

target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))