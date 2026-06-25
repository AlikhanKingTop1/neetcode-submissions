class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        cnt = defaultdict(int)
        l = 0
        for r in range(len(s)):
            cnt[s[r]] +=1
            most_freq = max(cnt.values())
            if (r-l+1) - most_freq > k:
                cnt[s[l]] -= 1
                l +=1
            res= max(res, r-l+1)
        return res