class Solution:
    def countSubstrings(self, s: str) -> int:
        def get_pal(s, left, right):
            cnt = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt+=1
                left -= 1
                right +=1
            return cnt

        res = 0
        for i in range(len(s)):
            op1, op2 = get_pal(s,i,i), get_pal(s,i, i+1)
            res += op1 + op2
            
        return res