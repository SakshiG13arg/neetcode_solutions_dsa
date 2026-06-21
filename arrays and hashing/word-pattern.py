class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        charToWord = {}
        wordToChar = {}
        for c, w in zip(pattern, words):
            if w in wordToChar and wordToChar[w] != c:
                return False
            if c in charToWord and charToWord[c] != w:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True
