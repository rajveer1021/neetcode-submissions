class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        window = {}
        result = 0
        max_f = 0

        for R in range(0, len(s)):
            window[s[R]] = 1 + window.get(s[R], 0)
            max_f = max(max_f, window[s[R]])

            while (R-L+1) - max_f > k:
                window[s[L]] -= 1
                L += 1
            result = max(result, R-L+1)
        return result



        