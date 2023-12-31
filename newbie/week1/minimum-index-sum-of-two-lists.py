class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_words = {}
        for index, word in enumerate(list1):
            if word in list2:
                common_words[word] = index + list2.index(word)
        min_index = min(common_words[word] for word in common_words)
        result = []
        for word, count in common_words.items():
            if count == min_index:
                result.append(word)
        return result
