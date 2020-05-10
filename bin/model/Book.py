from bin.handler.BookInformationSearcher import BookInformationSearcher
import logging


class Book:
    def __init__(self, path, file):
        try:
            info = BookInformationSearcher(path, file)
            self.book_name = info.book_title()
            self.number_of_paragraphs = info.count_paragraphs()
            self.number_of_words = info.count_words()
            self.number_of_letters = info.count_letters()
            self.words_with_capital_letters = info.count_words_with_capital_letters()
            self.words_in_lowercase = info.count_words_in_lowercase()

        except:
            logging.exception('Cannot initialize Object model.')

    def get_model(self):
        return [self.book_name,
                self.number_of_paragraphs,
                self.number_of_words,
                self.number_of_letters,
                self.words_with_capital_letters,
                self.words_in_lowercase]
