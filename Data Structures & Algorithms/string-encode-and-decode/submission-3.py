class Solution:
    def encode(self, strs: list[str]) -> str:
        parts = []

        for s in strs:
            parts.append(f"{len(s)}#{s}")

        return "".join(parts)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            j += 1

            res.append(s[j:j + length])
            i = j + length

        return res