class Solution:
    def isPalindrome(self, word: str):
        length = len(word)
        for i in range(length//2):
            if word[i] != word[length - i - 1]:
                return False
        return True

    def firstPalindrome(self, words: [str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""