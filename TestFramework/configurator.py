class Configurator:
    def __init__(self, test_type):
        with open('config.json') as file:
            self.config = eval(file.read())
        self.config = self.config[test_type]
        self.type = test_type

    def get_database_url(self):
        return self.config['database']

    def get_test_data_folder(self):
        return self.config['test_data_folder']
