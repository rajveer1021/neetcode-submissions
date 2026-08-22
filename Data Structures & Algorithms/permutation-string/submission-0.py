class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        need = Counter(s1)
        required = len(s1)

        left = 0
        window = {}

        for right in range(len(s2)):
            c = s2[right]
            window[c] = window.get(c, 0) + 1

            while right - left + 1 > required:
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1
                
            if window == need:
                return True

        return False