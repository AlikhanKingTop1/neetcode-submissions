class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = sorted(nums)
        for i in range(1,len(a)):
            if a[i] == a[i-1]:
                return True;
        return False;
        

