class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt = defaultdict(int)
        for c in t:
            t_cnt[c] +=1
        t_uniq = len(t_cnt)
        s_cnt = defaultdict(int)
        s_uniq = 0  
        res = None
        res_len = float("inf")
        l = 0
        for r in range(len(s)):
            new_char = s[r]
            s_cnt[new_char] +=1
            if new_char in t_cnt and s_cnt[new_char] == t_cnt[new_char]:
                s_uniq +=1
            while s_uniq == t_uniq:
                cur_len = r-l+1
                if cur_len < res_len:
                    res = (l,r)
                    res_len = cur_len
                del_char = s[l]
                s_cnt[del_char] -=1
                if del_char in t_cnt and s_cnt[del_char] < t_cnt[del_char]:
                    s_uniq -=1
                l +=1
        if res_len == float("inf"):
            return ""
        l,r = res
        return s[l:r+1]
