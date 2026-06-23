class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntH = {}
        arr= []
        for n in nums:
            cntH[n]=1 + cntH.get(n,0)
        for val,cnt in cntH.items():
            arr.append([cnt,val])
        arr.sort()
        return arr.pop()[-1]