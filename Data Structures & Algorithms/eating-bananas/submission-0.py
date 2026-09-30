class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def valid(mid):
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            return hours <= h

        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2

            if valid(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result