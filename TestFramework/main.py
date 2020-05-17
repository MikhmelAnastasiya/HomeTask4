import sys
import os

sys.path.insert(0, os.path.abspath('..'))
from sys import argv
from TestFramework.configurator import Configurator
from TestFramework.connector import Connector
from TestFramework.resulting import Result
from TestFramework.test_processor import TestProcessor


def run():
    test_type = argv[1]

    config = Configurator(test_type)

    database_url = config.get_database_url()

    connector = Connector(database_url)

    logger = Result(test_type)

    test_processor = TestProcessor(config, connector, logger)
    test_processor.process()

    logger.finish_test()


if __name__ == '__main__':
    run()
