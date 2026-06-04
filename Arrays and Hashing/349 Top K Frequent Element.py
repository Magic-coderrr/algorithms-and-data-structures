# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

def topKFreq(nums,k):
    feqCount_Map={}
    for i in nums:
        if i not in feqCount_Map:
            feqCount_Map[i]=1
        else:
            feqCount_Map[i]+=1
   
   # Creating an array of empty lists of size (len(nums) + 1) to perform bucket sort
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in feqCount_Map.items():
    # putting respective freq ones in their respective buckets
        buckets[freq].append(num)

    res = []
    # This starts from the end of the buckets array we do this as most freq ones will be at the end
    for bucket in reversed(buckets):
        # A bucket might have multiple numbers in it, or it might be empty
        for num in bucket:
            res.append(num)
            if len(res)==k:
                return res



nums = [1,1,1,2,2,3]
k = 2
print(topKFreq(nums,k))