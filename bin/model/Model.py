import bin.TextInformation as info
import logging


class Model:
    def __init__(self, file):
        try:
            inf = info.TextInformation(file)
            self.book_name = inf.book_title()
            self.number_of_paragraphs = inf.count_paragraphs()
            self.number_of_words = inf.count_words()
            self.number_of_letters = inf.count_letters()
            self.words_with_capital_letters = inf.count_words_with_capital_letters()
            self.words_in_lowercase = inf.count_words_in_lowercase()

        except IOError as e:
            logging.exception('Cannot initialize Object model.')

    def get_model(self):
        return [self.book_name,
                self.number_of_paragraphs,
                self.number_of_words,
                self.number_of_letters,
                self.words_with_capital_letters,
                self.words_in_lowercase]
