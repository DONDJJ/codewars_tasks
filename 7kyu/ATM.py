import unittest

'''
There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.

You are given money in nominal value of n with 1<=n<=1500.

Try to find minimal number of notes that must be used to repay in dollars, or output -1 if it is impossible.
'''


def solve(n):
    money = (10, 20, 50, 100, 200, 500)

    if n % 10 != 0:
        return -1
    number_of_notes = 0

    for i in money[::-1]:
        while n >= i:
            n -= i
            number_of_notes += 1
    return number_of_notes


class ATMTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solve(770), 4)

    def test_2(self):
        self.assertEqual(solve(550), 2)

    def test_3(self):
        self.assertEqual(solve(10), 1)

    def test_4(self):
        self.assertEqual(solve(1250), 4)

    def test_impossible_1(self):
        self.assertEqual(solve(125), -1)

    def test_impossible_2(self):
        self.assertEqual(solve(666), -1)

    def test_impossible_3(self):
        self.assertEqual(solve(42), -1)

    def test_impossible_4(self):
        self.assertEqual(solve(1), -1)


if __name__ == "__main__":
    unittest.main()
