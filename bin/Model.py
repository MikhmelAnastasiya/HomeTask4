import bin.ParseXML as parser
import logging

logging.basicConfig(level=logging.INFO)


class Model:
    def __init__(self):
        self.name = ''
        self.count = 0

    # def find_elements(self):
    #     root = parser.XMLParser('').parse_book()
    #
    #     elem = root.find(".//*[@info-type='src-book-title']").text
    #     self.name = elem
    #
    #     p = root.findall('.//{http://www.gribuser.ru/xml/fictionbook/2.0}p')
    #     print(len(p))
    #
    #     print(elem)
