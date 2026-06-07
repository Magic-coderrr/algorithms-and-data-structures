# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).
# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

def findMedianSortedArrays( nums1, nums2):
    A, B = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
    m, n = len(A), len(B)
    half_len = (m + n + 1) // 2

    left = 0
    right = m
    while left <= right:
        # Calculate partition indices
        i = left + (right - left) // 2
        j = half_len - i
        
        # Grab the 4 edge values 
        A_left = A[i - 1] if i > 0 else float('-inf')
        A_right = A[i] if i < m else float('inf')
        
        B_left = B[j - 1] if j > 0 else float('-inf')
        B_right = B[j] if j < n else float('inf')

        # Checking if the cut is valid
        if A_left <= B_right and B_left <= A_right:
            #  The total combined length is Odd
                if (m + n) % 2 != 0:
                    return float(max(A_left, B_left))
                    
                # The total combined length is Even
                else:
                    left_max = max(A_left, B_left)
                    right_min = min(A_right, B_right)
                    return (left_max + right_min) / 2.0
            
        elif A_left > B_right:
            right = i - 1
            
        else:
            left = i + 1

nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1,nums2))