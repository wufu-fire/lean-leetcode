"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

思路：根据dict中，key的索引性能。
首先，在遍历数组的过程中，将数组的key和index转化为dict的key和value
其次：index1 必须小于 index2，则对象的添加操作要慢一步，所以返回结果的时候，先返回obj的value。
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        obj = {}
        for i, num in enumerate(numbers):
            if obj.get(target - num) is not None:
                return [int(obj.get(target - num)) + 1, i+1]
            obj[num] = i

nums = [2, 7, 11, 15]
target = 9

s = Solution()
res = s.twoSum(nums, target)
print("The result is: ", res)
