import unittest
import string

'''
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
'''


def alphabet_position(text):
    alphabet_list = list(string.ascii_uppercase)
    text_list = list(text.upper())

    new_list = [None for i in range(len(text_list))]
    for i in range(len(text_list)):
        if text_list[i] in alphabet_list:
            new_list[i] = alphabet_list.index(text_list[i]) + 1

    while None in new_list:
        new_list.remove(None)
    return ' '.join(str(i) for i in new_list)


class AlphPosTest(unittest.TestCase):
    def test_blank(self):
        self.assertEqual(alphabet_position(''), '')

    def test_one(self):
        self.assertEqual(alphabet_position('a'), '1')

    def test_standart(self):
        self.assertEqual(alphabet_position("The sunset sets at twelve o' clock."),
                         "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")


if __name__ == '__main__':
    unittest.main()
