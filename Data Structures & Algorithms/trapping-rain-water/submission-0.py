class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)

        max_prefix = 0
        max_suffix = 0
        max_water = 0

        for i in range(len(height)):
            max_prefix = max(max_prefix, height[i])
            prefix[i] = max_prefix

        for i in range(len(height) - 1, -1, -1):
            max_suffix = max(max_suffix, height[i])
            suffix[i] = max_suffix

        for i in range(len(height)):
            water = min(prefix[i], suffix[i]) - height[i]
            max_water += water

        return max_water