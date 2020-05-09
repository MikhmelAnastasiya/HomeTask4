import bin.ParseXML as parser
import logging
import re


class TextInformation:

    def __init__(self):
        self.root = parser.XMLParser('').parse_book()

    def book_title(self):
        title = self.root.find(".//*[@info-type='src-book-title']").text
        logging.info('Book  with title ' + title + ' was found')

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
