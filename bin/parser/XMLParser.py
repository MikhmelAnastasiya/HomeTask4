import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO)


class XMLParser:
    def __init__(self, path, file):
        self.file = file
        self.path = path

    def parse_book(self):
        try:
            tree = ET.parse(self.path + "\\" + self.file)
            root = tree.getroot()
            logging.info('File ' + self.path + "\\" + self.file + ' was parsed')

            return root

        except IOError as e:
            logging.exception('Cannot find file: ' + self.path)
