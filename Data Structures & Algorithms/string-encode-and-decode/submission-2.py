class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> list[str]:
        decoded = []
        i = 0

        while i < len(s):
            # Find the '#'
            j = i
            while s[j] != "#":
                j += 1

            # Length of the next word
            length = int(s[i:j])

            # Move to the start of the word
            j += 1

            # Extract the word
            word = s[j:j + length]
            decoded.append(word)

            # Move to the next encoded string
            i = j + length

        return decoded
