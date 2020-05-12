import logging
import os
import shutil

logging.basicConfig(level=logging.INFO)


class Folder:
    def __init__(self):
        self.path_to_input_folder = ""
        self.path_to_incorrect_input_folder = ""

    def create_folders(self):
        home = os.path.expanduser('~')
        self.path_to_input_folder = os.path.join(home, 'Documents', 'books', 'input')
        self.path_to_incorrect_input_folder = os.path.join(home, 'Documents', 'books', 'incorrect_input')

        try:
            if not os.path.isdir(os.path.join(home, 'Documents', 'books')):
                os.mkdir(os.path.join(home, 'Documents', 'books'))
            if not os.path.isdir(self.path_to_input_folder):
                os.mkdir(os.path.join(home, 'Documents', 'books', 'input'))
                logging.info("Input folder was created by path {}".format(self.path_to_input_folder))
            if not os.path.isdir(self.path_to_incorrect_input_folder):
                os.mkdir(self.path_to_incorrect_input_folder)
        except OSError as error:
            logging.error("Creation of the directory failed. {}".format(str(error)))

    def clean_input_folder(self):
        for file in os.listdir(self.path_to_input_folder):
            if not file.endswith(".fb2"):
                logging.info("File {} was moved to {}".format(os.path.join(self.path_to_input_folder,
                                                                           file), self.path_to_incorrect_input_folder))
                try:
                    shutil.move(os.path.join(self.path_to_input_folder, file), self.path_to_incorrect_input_folder)
                except:
                    logging.error(
                        "File {} already exists in directory {}".format(file, self.path_to_incorrect_input_folder))

    def find_all_fb2_books(self, path):
        list_of_files = []
        for file in os.listdir(path):
            if file.endswith(".fb2"):
                logging.info("Processing of file {} in progress...".format(os.path.join(path, file)))
                list_of_files.append(file)

        return list_of_files
