import unittest

'''
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:
a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.
For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.
'''
vowels = ['a', 'e', 'i', 'o', 'u']


def encode(st):
    st_list = list(st)

    for i, j in zip(st_list, range(len(st_list))):
        if i.lower() in vowels:
            st_list[j] = str(vowels.index(i) + 1)

    return ''.join(st_list)


def decode(st):
    st_list = list(st)

    for i, j in zip(st_list, range(len(st_list))):
        try:
            x = int(i)
        except ValueError:
            continue
        else:
            st_list[j] = vowels[int(i) - 1]

    return ''.join(st_list)


class VowelCodeTest(unittest.TestCase):
    def test_encode_1(self):
        self.assertEqual(encode('hello'), 'h2ll4')

    def test_encode_2(self):
        self.assertEqual(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?')

    def test_decode_1(self):
        self.assertEqual(decode(encode('This is an encoding test.')), 'This is an encoding test.')

    def test_decode_2(self):
        self.assertEqual(decode('h2ll4'), 'hello')


if __name__ == "__main__":
    unittest.main()
