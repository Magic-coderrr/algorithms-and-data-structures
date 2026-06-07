# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index
#  k (1 <= k < nums.length) such that the resulting array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of
#  target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
def search( nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
            
        # The Left half is perfectly sorted
        if nums[left] <= nums[mid]:
            
            # Is the target bounded inside this left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Target is here.
            else:
                left = mid + 1   # Target is Not here. 
                
        # The Right half is perfectly sorted
        else:
            
            # Is the target bounded inside this right half?
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Target is here.
            else:
                right = mid - 1  # Target is Not here.
                
    # if no answer found we return -1
    return -1

nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums,target))