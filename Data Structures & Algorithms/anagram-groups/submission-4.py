class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for i,s in enumerate(strs):
            count= [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashMap[tuple(count)].append(s)

        return list(hashMap.values())