import xml.etree.ElementTree as ET
import logging
import os
import shutil

logging.basicConfig(level=logging.INFO)


class XMLParser:
    def __init__(self, file):
        self.file=file
        self.path_to_input_folder = ""
        self.path_to_incorrect_input_folder = ""

    def parse_book(self):
        try:
            tree = ET.parse(self.path_to_input_folder + "\\" + self.file)
            root = tree.getroot()
            logging.info('File ' + self.path_to_input_folder + ' was parsed')

            return root

        except IOError as e:
            logging.exception('Cannot find file: ' + self.path_to_input_folder)

    def find_path(self):
        home = os.path.expanduser('~')

        try:
            if not os.path.isdir(home + '\\Documents\\books'):
                os.mkdir(home + '\\Documents\\books')
            if not os.path.isdir(home + '\\Documents\\books\\input'):
                os.mkdir(home + '\\Documents\\books\\input')
            if not os.path.isdir(home + '\\Documents\\books\\incorrect_input'):
                os.mkdir(home + '\\Documents\\books\\incorrect_input')
        except OSError:
            logging.error("Creation of the directory failed")

        self.path_to_input_folder = home + '\\Documents\\books\\input'
        self.path_to_incorrect_input_folder = home + '\\Documents\\books\\incorrect_input'

    def clean_input_folder(self):
        for file in os.listdir(self.path_to_input_folder):
            if not file.endswith(".fb2"):
                logging.info("File " + os.path.join(self.path_to_input_folder, file) + " was moved to " + self.path_to_incorrect_input_folder)
                try:
                    shutil.move(self.path_to_input_folder + "\\" + file, self.path_to_incorrect_input_folder)
                except:
                    logging.error("File " + file + " already exists in directory " + self.path_to_incorrect_input_folder)

    def find_all_books(self):
        list_of_files = []
        for file in os.listdir(self.path_to_input_folder):
            if file.endswith(".fb2"):
                logging.info("File " + os.path.join(self.path_to_input_folder, file) + " in progress...")
                list_of_files.append(file)

        return list_of_files


