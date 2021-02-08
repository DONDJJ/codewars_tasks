import unittest
import string

'''
Create a function which accepts one arbitrary string as an argument, and return a string of length 26.
The objective is to set each of the 26 characters of the output string to either '1' or '0' based on the fact 
whether the Nth letter of the alphabet is present in the input (independent of its case).
So if an 'a' or an 'A' appears anywhere in the input string (any number of times), 
set the first character of the output string to '1', otherwise to '0'. 
if 'b' or 'B' appears in the string, set the second character to '1', and so on for the rest of the alphabet.
'''


def change(st):
    alphabet = list(string.ascii_uppercase)
    st = st.upper()

    for i in range(len(alphabet)):
        if alphabet[i] in st:
            alphabet[i] = 1
        else:
            alphabet[i] = 0

    return ''.join(str(v) for v in alphabet)


class LettersSearchTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(change("a **&  bZ"), "11000000000000000000000001")

    def test_2(self):
        self.assertEqual(change('Abc e  $$  z'), "11101000000000000000000001")

    def test_3(self):
        self.assertEqual(change("!!a$%&RgTT"), "10000010000000000101000000")

    def test_4(self):
        self.assertEqual(change(""), "00000000000000000000000000")

    def test_5(self):
        self.assertEqual(change("abcdefghijklmnopqrstuvwxyz"), "11111111111111111111111111")

    def test_6(self):
        self.assertEqual(change("aaaaaaaaaaa"), "10000000000000000000000000")

    def test_7(self):
        self.assertEqual(change("&%&%/$%$%$%$%GYtf67fg34678hgfdyd"), "00010111000000000001000010")


if __name__ == '__main__':
    unittest.main()
