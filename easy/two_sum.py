"""
思路：根据dict中，key的索引性能。
首先，将数组的val和index，转化成dict的key和value
其次，遍历数组，targe - num是否是dict中的key。
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        obj = {}
        for i, num in enumerate(nums):
            obj[num] = i
            
        for i ,num in enumerate(nums):
            if target - num in obj:
                r = obj[target - num]
                if i != r:
                    return [i, r]
            
        
nums = [2, 7, 11, 15]
target = 9

s = Solution()
res = s.twoSum(nums=nums, target=target)
print("The result is: ", res)
