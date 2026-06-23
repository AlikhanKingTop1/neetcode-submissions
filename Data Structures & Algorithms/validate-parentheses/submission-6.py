class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashM = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in hashM:
                if stack and stack[-1] == hashM[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
