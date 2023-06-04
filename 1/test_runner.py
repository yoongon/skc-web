from unittest import TestCase
from runner import lambda_handler


class Test(TestCase):
    def test_lambda_handler(self):
        code = 'class Solution:\n    def hello(self, a, b):\n        c = a + b\n        return c\n'
        event = {'body': {'code': code}}

        actual = lambda_handler(event, None)
        expected = {'statusCode': 200, 'body': '[{"input": [1, 2], "user_output": 3, "solution_output": 3}, {"input": [3, 4], "user_output": 7, "solution_output": 7}]'}
        assert expected == actual

