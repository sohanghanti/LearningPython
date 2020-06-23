import unittest
from TestCaseExecution_unittest import myFunctions


class Tests(unittest.TestCase):
    def test_case_01(self):
        text = 'python the great language'
        result = myFunctions.change_to_captial(text)
        self.assertEqual(result, 'Python the great language')


if __name__ == '__main__':
    unittest.main()


