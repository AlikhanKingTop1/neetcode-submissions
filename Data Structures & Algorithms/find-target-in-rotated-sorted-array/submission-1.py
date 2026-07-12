class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            if nums[l] <= nums[mid]:
                if target > mid_val or target < nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if target < mid_val or target > nums[r]:
                    r = mid-1
                else:
                    l = mid +1
        
        return -1