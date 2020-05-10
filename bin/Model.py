import bin.TextInformation as info
import logging


class Model:
    def __init__(self):
        try:
            self.book_name = info.TextInformation().book_title()
            self.number_of_paragraphs = info.TextInformation().count_paragraphs()
            self.number_of_words = info.TextInformation().count_words()
            self.number_of_letters = info.TextInformation().count_letters()
            self.words_with_capital_letters = info.TextInformation().count_words_with_capital_letters()
            self.words_in_lowercase = info.TextInformation().count_words_in_lowercase()
            logging.info('Object Model was initialized.')

        except IOError as e:
            logging.exception('Cannot initialize Object Model.')

    def get_model(self):
        return [self.book_name, self.number_of_paragraphs, self.number_of_words, self.number_of_letters, self.words_with_capital_letters, self.words_in_lowercase]
