"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]


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
