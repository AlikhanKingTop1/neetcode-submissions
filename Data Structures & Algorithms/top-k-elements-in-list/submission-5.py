class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        a = []
        res = []
        for n in nums:
            count[n] = 1 +count.get(n,1)
        
        for num,freq in count.items():
            a.append([freq,num])
        a = sorted(a)

        while len(res) < k:
            res.append(a.pop()[1])
        return res