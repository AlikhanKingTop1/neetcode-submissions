class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashCount = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashCount:
                return [hashCount[difference], i]
            hashCount[nums[i]] = i