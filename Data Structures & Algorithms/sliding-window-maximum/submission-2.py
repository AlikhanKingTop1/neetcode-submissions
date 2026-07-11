class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res =[]
        l,r = 0,0
        dq = deque()
        while r < len(nums):
            #Monotonic decreasing dq
            while dq and nums[r] > dq[-1]:
                dq.pop()
            dq.append(nums[r])
            if (r-l+1) == k:
                res.append(dq[0])
                if dq[0] == nums[l]:
                    dq.popleft()
                l += 1
            r +=1
        return res