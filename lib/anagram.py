# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matching_words = []
        
        for word in word_list:
            if sorted(self.word) == sorted(word):
                matching_words.append(word)

        return matching_words