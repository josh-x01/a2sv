class Solution:
    def printVertically(self, s: str) -> List[str]:
        words_list = s.split()
        result_list = []
        max_len = max(len(word) for word in words_list)
        for i in range(max_len):
            new_word = []
            for word in words_list:
                if i < len(word):
                    new_word.append(word[i])
                else:
                    new_word.append(" ")
            result_list.append("".join(new_word).rstrip())
        return result_list
                    