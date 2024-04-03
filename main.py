from collections import Counter

def findWords(inputString, dictionary):
    def is_valid_word(word, input_count):
        return all(word.count(char) <= input_count.get(char, 0) for char in word)

    input_count = Counter(inputString)
    return [word for word in dictionary if is_valid_word(word, input_count)]

# Test cases
print(findWords("ate", ["ate", "eat", "tea", "dog", "do", "god", "goo", "go", "good"]))
print(findWords("oogd", ["ate", "eat", "tea", "dog", "do", "god", "goo", "go", "good"]))
print(findWords("a", ["a", "b", "c"])) 
print(findWords("", ["abc", "def", "ghi"])) 
print(findWords("abab", ["ab", "ba", "abb", "bba", "abc"])) 
