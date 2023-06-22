from statistics import mean

import emoji
import pymorphy3

from dictionary import docs


class TextChecker:
    def __init__(self, text: str):
        self.text = text

    @property
    def is_this_word_exist(self):
        analyzator = pymorphy3.MorphAnalyzer()
        words = self.text.split(" ")
        score_list = []
        for word in words:
            weight_word = analyzator.parse(word)
            score_list.append(weight_word[0].score)
        return mean(score_list) > 0.65

    @property
    def is_eng_symbol(self):
        return not (self.text.isascii())

    @property
    def is_has_only_emoji(self):
        return emoji.is_emoji(self.text)

    @property
    def is_only_number(self):
        return not (self.text.isdigit())

    @property
    def is_many_repeat(self):
        words = self.text.split(" ")
        for i in range(len(words) - 1):
            if words[i] == words[i + 1]:
                return False
        return True

    @property
    def is_nonsense_russian(self):
        for doc in docs:
            if doc in self.text:
                return False
        return True
