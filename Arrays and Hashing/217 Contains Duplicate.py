def containsDuplicate(nums):
    seen = set()
    
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
        
    return False

nums=[1,2,3,1]
print(containsDuplicate(nums)) #returns true if it contains duplicate and false if not