import unittest

'''
Colour here:        G G        B G        R G        B R
Becomes colour:      G          R          B          G

Another example:
R R G B R G B B
 R B R G B R B
  G G B R G G
   G R G B G
    B B R R
     B G R
      R B
       G

The answer: 'G'
'''


def triangle(row):
    cur_row = row

    while len(cur_row) > 1:
        new_row = ""
        for i in range(len(cur_row) - 1):
            new_row += define_next_color({cur_row[i], cur_row[i + 1]})
        cur_row = new_row

    return cur_row


def define_next_color(color_set):
    if color_set == {'G', 'G'}:
        return 'G'
    elif color_set == {'B', 'B'}:
        return 'B'
    elif color_set == {'R', 'R'}:
        return 'R'
    elif color_set == {'G', 'B'}:
        return 'R'
    elif color_set == {'G', 'R'}:
        return 'B'
    elif color_set == {'B', 'R'}:
        return 'G'


class ColouredTrianglesTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(triangle('GB'), 'R')

    def test_2(self):
        self.assertEqual(triangle('RRR'), 'R')

    def test_3(self):
        self.assertEqual(triangle('RGBG'), 'B')

    def test_4(self):
        self.assertEqual(triangle('RBRGBRB'), 'G')

    def test_5(self):
        self.assertEqual(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')

    def test_6(self):
        self.assertEqual(triangle('B'), 'B')

    def test_6(self):
        self.assertEqual(triangle(''), '')


if __name__ == '__main__':
    unittest.main()
