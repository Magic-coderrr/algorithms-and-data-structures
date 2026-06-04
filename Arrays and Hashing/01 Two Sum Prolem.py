def twoSum(nums, target):
    # Dictionary to store {number: index}
    prev_map = {} 

    for i, n in enumerate(nums):
        complement = target - n
        
        # Checking if we've seen the complement before
        if complement in prev_map:
            return [prev_map[complement], i]
            
        # If not, add the current number and its index to the map
        prev_map[n] = i

    return [] # In case no solution is found we return empty list which indicates no solution found

nums = [2, 11, 7, 15]
print(twoSum(nums,target=9)) #prints indices if solution found