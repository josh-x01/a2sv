class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        last_row = "zxcvbnm"
        def word_row(row, word):
            for letter in word.lower():
                if letter not in row:
                    return False
            return True
        valid_words = []
        for word in words:
            if word_row(first_row, word) or word_row(second_row, word) or word_row(last_row, word):
                valid_words.append(word)
        return valid_words
