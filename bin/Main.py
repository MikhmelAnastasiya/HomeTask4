import bin.DBConnector as calc
import bin.model.Model as model
import bin.ParseXML as parser
import os


def main():

    p = parser.XMLParser('')
    p.find_path()
    p.clean_input_folder()

    for file in p.find_all_books():
        if file.endswith(".fb2"):
            calc.DBConnector().add_book(model.Model(file))





if __name__ == "__main__":
    main()
