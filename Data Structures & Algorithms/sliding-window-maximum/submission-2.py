class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        q = deque()
        res = []
        
        while r < len(nums):
            
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if q[0] < l:
                q.popleft()

            if r >= k-1:
                res.append(nums[q[0]])
                l += 1
            r+=1
        return res
