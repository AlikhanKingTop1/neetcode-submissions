class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)-k+1):
            max_el = nums[i]
            for j in range(i,i+k):
                max_el = max(max_el,nums[j])
            res.append(max_el)
        return res