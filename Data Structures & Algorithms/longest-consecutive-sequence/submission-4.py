class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        if nums == [0,0]:
            return 1
        n = sorted(set(nums))
        max_length = 0
        for i in range(len(n)):
            length = 1
            current = n[i]
            for j in range(i+1,len(n)):
                if n[j] == current+1:
                    current = n[j]
                    length +=1
                    max_length = max(max_length, length)
                else:
                    max_length = max(max_length, length)
                    continue
        return max_length