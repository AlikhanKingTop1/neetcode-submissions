class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashCount = {}
        for i in range(len(nums)):
            hashCount[nums[i]] = 1 + hashCount.get(nums[i], 0)
        sorted_keys = sorted(hashCount, key=hashCount.get, reverse=True)
        a = []
        for i in range(k):
            a.append(sorted_keys[i])
        return a

