import unittest
import Task2Program

class Test_request (unittest.TestCase):
    def test_status_code(self):
        url = 'https://www.python.org/'
        actual = Task2Program.main(url)
        expected = 200
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()