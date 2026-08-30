class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)

        right_forward = [n] * n
        left_backward = [-1] * n

        stack = []

        # Find first smaller element on LEFT
        for i in range(n):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                left_backward[i] = stack[-1]

            stack.append(i)

        # reset stack
        stack = []

        # Find first smaller element on RIGHT
        for i in range(n - 1, -1, -1):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right_forward[i] = stack[-1]

            stack.append(i)

        area = 0

        for i in range(n):

            width = right_forward[i] - left_backward[i] - 1

            current_area = heights[i] * width

            area = max(area, current_area)

        return area