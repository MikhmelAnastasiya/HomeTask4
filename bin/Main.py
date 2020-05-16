import sys
import os

sys.path.insert(0, os.path.abspath('..'))
from sys import argv
from bin.parser.Folder import Folder
from bin.model.DBConnector import DBConnector
from bin.model.Book import Book
import logging


def main():
    folder = Folder(argv[1])
    folder.create_folders()
    folder.clean_input_folder()

    if len(folder.find_all_fb2_books(folder.path_to_input_folder)) != 0:
        for file in folder.find_all_fb2_books(folder.path_to_input_folder):
            if file.endswith(".fb2"):
                try:
                    DBConnector().add_book(Book(folder.path_to_input_folder, file))
                except:
                    logging.error("Cannot parse {} file".format(os.path.join(folder.path_to_input_folder, file)))
    else:
        logging.info("No .fb2 files in folder " + folder.path_to_input_folder)


if __name__ == "__main__":
    main()
