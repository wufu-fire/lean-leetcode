"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
思路： l1 + l2 + l3 = 0   =>   l1 + l2 = -l3
3数之和，转换为2数之和
"""
class Solution(object):
    def threeSum(self, nums):
      """
      :type nums: List[int]
      :rtype: List[List[int]]
      """
      nums.sort()
      res =[]
      i = 0
      for i in range(len(nums)):
        if i == 0 or nums[i]>nums[i-1]:
          l = i+1
          r = len(nums)-1
          while l < r:
            s = nums[i] + nums[l] +nums[r]
            if s ==0:
              res.append([nums[i],nums[l],nums[r]])
              l +=1
              r -=1
              while l < r and nums[l] == nums[l-1]:
                  l += 1
              while r > l and nums[r] == nums[r+1]:
                  r -= 1
            elif s>0:
              r -=1
            else :
              l +=1
      return res

nums = [-1, 0, 1, 2, -1, -4]
res = Solution()

print(res.threeSum(nums))


