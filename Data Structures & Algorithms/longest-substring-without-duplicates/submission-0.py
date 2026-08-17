class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        result = 0
        L = 0

        for R in range(0, len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            result = max(result, R-L+1)
        return result

        