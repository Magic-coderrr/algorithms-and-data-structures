# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array 
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

def trap(height):

    if not height:
        return 0
    
    left=0
    right=len(height)-1
    max_left,max_right=height[left],height[right]
    total_water=0
    
    while left < right:
        # The Left side is the  bottleneck
        if max_left <= max_right:
            left+=1
            max_left=max(height[left],max_left)
            total_water+=max_left - height[left]

        # The Right side is the  bottleneck
        else:
            right-=1
            max_right=max(height[right],max_right)
            total_water+=max_right-height[right]

    return total_water