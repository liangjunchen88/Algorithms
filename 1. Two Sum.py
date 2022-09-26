class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        res = {}
        for i in range(len(nums)):
            if nums[i] in res:
                return [res[nums[i]], i]
            res[target - nums[i]] = i

