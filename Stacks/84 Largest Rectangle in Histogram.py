# Given an array of integers heights representing the histogram's bar height where the width 
# of each bar is 1, return the area of the largest rectangle in the histogram.
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

def largestRectangleArea(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    max_area = 0
    stack = []

    for i, h in enumerate(heights):
        start_index = i 
        
        # While the incoming bar is Shorter than the top of the stack
        while stack and h < stack[-1][1]:
            # Popping it and unpacking the tuple
            popped_index, popped_height = stack.pop()
            
            # Calculate the area
            area = popped_height * (i - popped_index)
            max_area = max(max_area, area)
            
            # The new short bar stretches backward so we take its index
            start_index = popped_index
            
        # Push the new bar with its newly calculated start_index
        stack.append((start_index, h))

    # untrapped bars extending to the end
    for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

    return max_area