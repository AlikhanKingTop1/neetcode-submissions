class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}
        for num in nums:
            if num not in hMap:
                hMap[num] = 1
            else:
                hMap[num] +=1

        freq = [[] for i in range(len(nums) + 1)]
        for num, cnt in hMap.items():
            freq[cnt].append(num)

        res = []
        for arr in reversed(freq):
            if len(arr) >= 0:
                res += arr
            if len(res) == k:
                return res