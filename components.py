import emoji

from dictionary import docs


class TextChecker:
    text: str

    def __init__(self, text: str):
        self.text = text

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
