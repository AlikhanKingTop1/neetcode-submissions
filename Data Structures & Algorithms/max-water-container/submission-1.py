class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        max_w = 0
        while l < r:
            max_w = max(max_w, (r-l)*min(heights[l],heights[r]))
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_w