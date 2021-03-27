import unittest
import cap_test

# inherits
class Testcap(unittest.TestCase):

    def test_word(self):
        text = 'ashish is'
        result = cap_test.cap_test(text)
        self.assertEqual(result,'Ashish Is')

if __name__ == '__main__':
    unittest.main()

