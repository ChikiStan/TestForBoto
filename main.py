from components import TextChecker


def check_message(text: TextChecker):
    return (
        text.is_only_number
        and text.is_eng_symbol
        and text.is_many_repeat
        and text.is_nonsense_russian
        and text.is_this_word_exist
    ) or text.is_has_only_emoji


if __name__ == "__main__":
    message = input()
    text = TextChecker(message)
    print(check_message(text))
