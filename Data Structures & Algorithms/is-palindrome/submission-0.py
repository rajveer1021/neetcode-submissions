class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        return cleaned == cleaned[::-1]