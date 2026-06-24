class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen = set()
        for r,r_char in enumerate(s):
            while r_char in seen:
                seen.remove(s[l])
                l +=1
            seen.add(r_char)
            res = max(res, r - l +1)
        return res