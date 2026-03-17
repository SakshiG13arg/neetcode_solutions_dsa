class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified = ""
        for c in s:
            if c.isalnum():
                modified += c.lower()
        reversed_str = modified[::-1]
        return modified == reversed_str
        l, r = 0, reversed_str - 1
        while l < len(modified) and r >= 0:
            if modified[l] != reversed_str[r]:
                return False
            l += 1
            r -= 1
        return True
