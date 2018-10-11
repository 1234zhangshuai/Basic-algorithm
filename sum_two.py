
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


nums = [2, 7, 11, 15]
target = 9
a = Solution()
two_sum = a.twoSum(nums, target)
print(two_sum)