class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        dq = deque()
        result = []

        for right in range(len(nums)):

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

            # Remove elements that are outside the window
            if dq[0] < right - k + 1:
                dq.popleft()

            # Window is ready
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result