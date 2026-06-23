class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        st = set(nums)
        res = []
        for i in range(1,len(nums)):
            if i in st:
                continue
            else:
                res.append(i)
        if len(nums) not in st:
            res.append(len(nums))
        return res