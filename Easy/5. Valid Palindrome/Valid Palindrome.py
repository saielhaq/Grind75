class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        for char in s.lower():
            if char.isalnum():
                clean += char
        s = clean[::-1]
        if s == clean:
            return True
        else:
            return False