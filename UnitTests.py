import unittest
import StringProcessor as sp

class TestStringProcessor(unittest.TestCase):

    def setUp(self):
        pass

    def test_TotalWords_1(self):
        self.assertEqual( sp.TotalWords("hello there my friend"), 4)

    def test_PhraseLength_1(self):
        self.assertEqual( sp.PhraseLength("hello there my friend"), 21)

    def test_DistinctWords_1(self):
        self.assertEqual( sp.DistinctWordCount("hello there my friend"), 4)

    def test_DistinctWords_2(self):
        self.assertEqual( sp.DistinctWordCount("hello hello there my friend"), 4)

    def test_DistinctWords_3(self):
        self.assertEqual( sp.DistinctWordCount("hello! hello there my friend"), 4)

    def test_DistinctWords_4(self):
        self.assertEqual( sp.DistinctWordCount("Hello hello there my friend"), 4)


if __name__ == '__main__':
    unittest.main()
