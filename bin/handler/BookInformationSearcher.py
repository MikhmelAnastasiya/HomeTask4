import logging
import re
from bin.parser.XMLParser import XMLParser


class BookInformationSearcher:

    def __init__(self, path, file):
        parser = XMLParser(path, file)
        self.root = parser.parse_book()

    def book_title(self):
        title = self.root.find(".//*[@info-type='src-book-title']").text
        logging.info('Book with title ' + title + ' was found')

        return title

    def count_paragraphs(self):
        paragraphs = self.root.findall('.//{http://www.gribuser.ru/xml/fictionbook/2.0}p')
        count = len(paragraphs)
        logging.info('Number of paragraphs was counted: ' + str(count))

        return count

    def count_words(self):
        count = 0

        for paragraph in self.root.findall('.//{http://www.gribuser.ru/xml/fictionbook/2.0}p'):
            words_in_paragraph = re.findall(r'\w+', ''.join(paragraph.itertext()))  # ??? регулярное выражение
            count += len(words_in_paragraph)

        logging.info('Number of words was counted: ' + str(count))

        return count

    def count_letters(self):
        count = 0

        for paragraph in self.root.findall('.//{http://www.gribuser.ru/xml/fictionbook/2.0}p'):
            words_in_paragraph = re.findall(r'[a-zA-Z]|[а-яА-Я]', ''.join(paragraph.itertext()))
            count += len(words_in_paragraph)

        logging.info('Number of letters was counted: ' + str(count))

        return count

    def count_words_with_capital_letters(self):
        count = 0

        for paragraph in self.root.findall('.//{http://www.gribuser.ru/xml/fictionbook/2.0}p'):
            words_with_capital_letters = re.findall(r'\b[A-Z]\w+\b|\b[А-Я]\w+\b', ''.join(paragraph.itertext()))
            count += len(words_with_capital_letters)

        logging.info('Number of words with capital letters was counted: ' + str(count))

        return count

    def count_words_in_lowercase(self):
        count = 0

        for paragraph in self.root.findall('.//{http://www.gribuser.ru/xml/fictionbook/2.0}p'):
            words_in_lowercase = re.findall(r'\b[a-z]+\b|\b[а-я]+\b', ''.join(paragraph.itertext()))
            count += len(words_in_lowercase)

        logging.info('Number of words in lowercase was counted: ' + str(count))

        return count

    def frequency_of_word(self):
        list_of_words = []

        paragraphs = self.root.findall('.//{http://www.gribuser.ru/xml/fictionbook/2.0}p')

        full_string = ""

        for paragraph in paragraphs:
            string = ''.join(paragraph.itertext())
            full_string = full_string + " " + string

        full_string = re.sub(r'[^\w]', " ", full_string)

        split_string_in_lowercase = full_string.lower().split()
        unique_split_string_in_lowercase = set(split_string_in_lowercase)

        string_with_uppercase = re.findall(r'\b[A-Z]\w*\b|\b[А-Я]\w*\b', full_string)
        split_upper_string_in_lowercase = ' '.join(string_with_uppercase).lower().split()
        unique_split_upper_string_in_lowercase = set(split_upper_string_in_lowercase)

        for word in unique_split_string_in_lowercase:
            count_word = 0
            count_appercase = 0

            count_word = split_string_in_lowercase.count(word)

            for w in unique_split_upper_string_in_lowercase:
                if w == word:
                    count_appercase = split_upper_string_in_lowercase.count(w)

            list_of_words.append((word, count_word, count_appercase))

        return list_of_words
