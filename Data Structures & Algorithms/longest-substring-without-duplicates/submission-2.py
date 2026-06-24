class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = set()
        for i in range(len(s)):
            new_sub = 0
            for j in range(i,len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    new_sub +=1
                else:
                    seen.clear()
                    break
            max_len = max(max_len, new_sub)
        return max_len