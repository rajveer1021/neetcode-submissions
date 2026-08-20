class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        need = Counter(t)
        required = len(need)

        window = {}
        left = 0
        have = 0
        res , res_len = [-1,-1], float("inf")

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c]==need[c]:
                have += 1

            while have == required:
                if right - left +1 < res_len:
                    res = left, right
                    res_len = right - left + 1

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                
                left += 1
        left, right = res
        return s[left: right+1] if res_len != float("inf") else ""
        