class Anagram:
    def __init__ (self, word):
        self.word = word

    def match(self, words):
        result = []
        sorted_word = sorted(self.word.lower())
        
        for candidate in words:
            if self.word.lower() != candidate.lower() and sorted_word == sorted(candidate.lower()):
                result.append(candidate)


        return result


