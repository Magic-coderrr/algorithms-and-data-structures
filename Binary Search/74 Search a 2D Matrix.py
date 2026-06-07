# # You are given an m x n integer matrix matrix with the following two properties:

# # Each row is sorted in non-decreasing order.
# # The first integer of each row is greater than the last integer of the previous row.
# # Given an integer target, return true if target is in matrix or false otherwise.

# # You must write a solution in O(log(m * n)) time complexity.

# # Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# # Output: true

def searchMatrix(matrix, target):

    left=0
    Rows=len(matrix)
    Cols=len(matrix[0])
    right= (Rows * Cols) - 1

    while left<=right:
        
        mid=left + (right - left) // 2
        # convert the 1D mid index back into 2D grid coordinates
        r = mid // Cols
        c = mid % Cols
        mid_val = matrix[r][c]

        if mid_val == target: 
            return True
        elif mid_val < target:
             left=mid+1
        elif mid_val > target: 
             right =mid-1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(matrix,target))
