class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = sorted(s1)
        for i in range(len(s2)):
            for j in range(i + len(s1), i + len(s1) + 1):
                if sorted(s2[i:j]) == s:
                    return True
        return False