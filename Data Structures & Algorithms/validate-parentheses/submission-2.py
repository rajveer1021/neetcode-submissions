class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")": "(", "]": "[", "}": "{"}
        stack = []

        for i in s:
            if i in pair:
                if not stack or pair[i] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0