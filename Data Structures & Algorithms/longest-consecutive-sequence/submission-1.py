class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for i in nums:
            current = 0
            if i - 1 not in numbers:
                while i in numbers:
                    current += 1
                    i = i+1
            longest = max(longest, current)
        return longest