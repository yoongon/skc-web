import json
from unittest import TestCase
from runner import *


class Test(TestCase):
    def test_lambda_handler(self):
        # todo mocking !
        pass
    def test_get_handler(self):
        actual = get_handler(None, None)
        expected = {'description': 'Implements adder', 'sample_input': [[1, 2], [3, 4]]}
        assert expected == actual

    def test_post_handler(self):
        code = 'class Solution:\n    def hello(self, a, b):\n        c = a + b\n        return c\n'
        # todo
        inputs = [[1, 2], [3, 4]]
        event = {'body': json.dumps({'code': code, 'inputs': inputs}), 'httpMethod': 'POST'}

        actual = post_handler(event, None)
        expected = [{"input": [1, 2], "user_output": 3, "solution_output": 3}, {"input": [3, 4], "user_output": 7, "solution_output": 7}]
        assert expected == actual
