import unittest
import StringProcessor as sp

class TestStringProcessor(unittest.TestCase):

    def setUp(self):
        pass

    def test_TotalWords_1(self):
        self.assertEqual( sp.TotalWords("hello there my friend"), 4)

    def test_PhraseLength(self):
        self.assertEqual( sp.PhraseLength("hello there my friend"), 21)

if __name__ == '__main__':
    unittest.main()
