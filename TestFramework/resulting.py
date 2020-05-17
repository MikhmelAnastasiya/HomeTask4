class Result:
    def __init__(self, test_type):
        if test_type == "health_check":
            self.result_file = open('results/health_check.log', 'w')
        elif test_type == "smoke":
            self.result_file = open('results/smoke.log', 'w')

    def start_test(self, test_type):
        self.result_file.write('\n\n{} test was started\n'.format(test_type))

    def finish_test(self):
        self.result_file.close()

    def start_case(self, test_name):
        self.result_file.write("\n\nTest case '{}'".format(test_name))

    def add_pass(self, query, actual_result):
        self.result_file.write("\nPASS. Result is '{0}' as expected"
                               "\n\tQuery: {1}".format(actual_result, query))

    def add_fail(self, query, actual_result, expected_result):
        self.result_file.write("\nFAIL. Result is '{0}', but expected '{1}'"
                               "\n\tQuery: {2}".format(actual_result, expected_result, query))
