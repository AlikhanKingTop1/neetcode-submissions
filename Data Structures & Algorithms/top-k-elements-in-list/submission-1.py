class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashCount = {}
        for n in nums:
            hashCount[n] = 1 + hashCount.get(n,0)
        sort_keys = sorted(hashCount, key = hashCount.get, reverse = True)
        a = []
        for i in range(k):
            a.append(sort_keys[i])
        return a