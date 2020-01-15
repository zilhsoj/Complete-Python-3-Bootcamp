import unittest
import cap_me

# inherit unittest class
class TextCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap_me.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_more_words(self):
        text = 'monty python'
        result = cap_me.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()
