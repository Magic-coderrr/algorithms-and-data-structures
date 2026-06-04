# you are given an integer array height of length n. There are n vertical lines drawn such that 
# the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains 
# the most water.

# Return the maximum amount of water a container can store.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left=0
    right=len(height)-1
    max_area=0
    while left<right:
        # Calculating area for the current window 
        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height
        
        # Updating our main record
        max_area = max(max_area, area)
        
        # Now deciding which pointer to move based on heights of wall
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area



height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))