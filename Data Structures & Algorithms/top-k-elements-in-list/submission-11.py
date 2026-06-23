class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}
        for num in nums:
            if num not in hMap:
                hMap[num] = 1
            else:
                hMap[num] += 1
        
        freq = [[] for _ in range(len(nums)+1)]

        for key, value in hMap.items():
            freq[value].append(key)
        
        ans = []
        
        for arr in reversed(freq):
            if len(arr) > 0:
                ans += arr
            if len(ans) == k:
                return ans
        
