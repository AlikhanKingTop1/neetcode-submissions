class Solution:
    def rob(self, nums: List[int]) -> int:
        def robb(nums): 
            rob1 = 0
            rob2 = 0

            for num in nums:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        if (len(nums) == 1) : return nums[0]
        return max(robb(nums[:-1]), robb(nums[1:]))