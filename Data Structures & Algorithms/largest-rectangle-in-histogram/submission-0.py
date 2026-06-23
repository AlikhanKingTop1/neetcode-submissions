class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # ( idx, height)

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                prev_idx,prev_h = stack.pop()
                max_area = max(max_area, prev_h * (idx - prev_idx))
                start = prev_idx
            stack.append((start,height))
        for idx,height in stack:
            max_area = max(max_area, height*(len(heights) - idx))

        return max_area