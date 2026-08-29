class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for t in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[t]:
                i = stack.pop()
                result[i] = t-i
            stack.append(t)
        return result

        