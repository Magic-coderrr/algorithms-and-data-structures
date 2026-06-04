# ou are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

def findMaxAverage(nums, k):

    max_sum = 0
    for i in range(k):
        max_sum += nums[i] 
        
    old_sum = max_sum
    left = 0  
    
    for i in range(k, len(nums)):
        new_sum = old_sum - nums[left] + nums[i]
        left += 1

        if new_sum > max_sum:
            max_sum = new_sum
            
        old_sum = new_sum

    return max_sum / float(k)

nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))