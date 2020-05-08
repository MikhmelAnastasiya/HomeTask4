import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO)
# ET.register_namespace(prefix, uri)

class XMLParser:
    def __init__(self, path):
        # self.path = path
        self.path = "C:/Users/Anastasiya_Mikhmel/Documents/DQE Training/Module 4/Example.fb2"

    def parse_book(self):
        try:
            tree = ET.parse(self.path)
            root = tree.getroot()
            logging.info('File ' + self.path + ' was parsed')

            return root

        except IOError as e:
            logging.exception('Cannot find file: ' + self.path)




