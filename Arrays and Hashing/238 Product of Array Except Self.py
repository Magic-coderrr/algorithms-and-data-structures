# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
    
         # We Pre-fill arrays with 1s so we don't multiply by 0 and the whole array will become 0
        left_product_array = [1] * length
        right_product_array = [1] * length
        main_array = [1] * length
        
        # 1. Building Left Array each element is the product of everything to its left
        for i in range(1, length):
                left_product_array[i] = left_product_array[i - 1] * nums[i - 1]
                
        # 2. Building Right Array each element is the product of everything to its right
        for i in range(length - 2, -1, -1):
                right_product_array[i] = right_product_array[i + 1] * nums[i + 1]
                
        # 3. Multiplying them together for the final answer as we already have calulated the right and left side product already
        for i in range(length):
                main_array[i] = left_product_array[i] * right_product_array[i]
                
        return main_array
        

nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
