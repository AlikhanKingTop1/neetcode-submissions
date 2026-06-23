class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for i in range(len(strs)):
            sorted_key= "".join(sorted(strs[i]))
            if sorted_key not in hashMap:
                hashMap[sorted_key] = []
            hashMap[sorted_key].append(strs[i])
        return list(hashMap.values())