class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashCount = {}
        for i in range(len(nums)):
            hashCount[nums[i]] = i
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashCount and i != hashCount[difference]:
                return [i,hashCount[difference]]