import logging
import os
import shutil


class Folder:
    def __init__(self, path):
        self.path_to_folder = path
        self.path_to_input_folder = os.path.join(path, 'input')
        self.path_to_incorrect_input_folder = os.path.join(path, 'incorrect_input')

    def create_folders(self):
        try:
            if not os.path.isdir(self.path_to_folder):
                os.mkdir(self.path_to_folder)
            if not os.path.isdir(self.path_to_input_folder):
                os.mkdir(self.path_to_input_folder)
                logging.info("Cannot find input folder")
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
