import xml.etree.ElementTree as ET
import logging
import os

logging.basicConfig(level=logging.INFO)


class XMLParser:
    def __init__(self, path, file):
        self.file = file
        self.path = path

    def parse_book(self):
        try:
            tree = ET.parse(os.path.join(self.path, self.file))
            root = tree.getroot()
            logging.info("File {} was parsed".format(os.path.join(self.path, self.file)))

            return root

        except IOError as e:
            logging.exception("Cannot find file: {}".format(self.path))
