class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntH = {}
        for n in nums:
            cntH[n] = 1+cntH.get(n,0)
        ans =0
        best =0
        for val,cnt in cntH.items():
            if cnt > best:
                best = cnt
                ans = val
        return ans