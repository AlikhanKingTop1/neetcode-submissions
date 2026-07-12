class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        cur_min = float("inf")
        while left <= right:
            mid = left + (right - left) // 2
            cur_min = min(cur_min,nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid - 1
            else:
                break
        return cur_min