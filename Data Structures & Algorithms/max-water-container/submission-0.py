class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        max_area = 0
        while L < R:
            width = R - L
            height = min(heights[L], heights[R])
            current_area = width * height
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
            max_area = max(max_area, current_area)
        return max_area
            
        