
class Solution:
    def encode(self, strs: list[str]) -> str:
        encodedstring = ""
        for i in strs:
            encodedstring = encodedstring + "´" + i
        return encodedstring

    def decode(self, s: str) -> list[str]:
        decode = s.strip(" ")
        decode = s.split("´")
        return decode[1:]
