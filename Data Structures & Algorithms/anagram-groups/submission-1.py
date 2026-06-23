class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for n in strs:
            count = [0] * 26
            for c in n:
                count[ord(c) - ord("a")] += 1
            if tuple(count) not in hashmap:
                hashmap[tuple(count)] = []
            hashmap[tuple(count)].append(n)

        return list(hashmap.values())      
        