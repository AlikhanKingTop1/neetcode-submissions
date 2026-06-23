class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                max_w = max(max_w, (j - i) * min(heights[i], heights[j]))
        return max_w