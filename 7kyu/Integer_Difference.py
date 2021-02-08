import unittest

'''
Write a function that accepts two arguments: an array/list of integers and another integer (n).
Determine the number of times where two integers in the array have a difference of n
[1, 1, 5, 6, 9, 16, 27], n=4  -->  3  # (1,5), (1,5), (5,9)
[1, 1, 3, 3], n=2             -->  4  # (1,3), (1,3), (1,3), (1,3)
'''


def int_diff(arr, n):
    pairs_number = 0
    for i in range(len(arr) - 1):
        r = [j for j in range(i + 1, len(arr))]
        for j in r:
            if abs(arr[j] - arr[i]) == n:
                pairs_number += 1
    return pairs_number


class IntDifTest(unittest.TestCase):
    def test_blank(self):
        result = int_diff([], 10)
        self.assertEqual(result, 0)

    def test_one_elem(self):
        result = int_diff([1], 2)
        self.assertEqual(result, 0)

    def test_two_elem(self):
        result = int_diff([1, 2], 1)
        self.assertEqual(result, 1)

    def test_1(self):
        result = int_diff([1, 1, 5, 6, 9, 16, 27], 4)
        self.assertEqual(result, 3)

    def test_2(self):
        result = int_diff([1, 1, 3, 3], 2)
        self.assertEqual(result, 4)

    def test_n_0_first(self):
        result = int_diff([1, 2, 3], 0)
        self.assertEqual(result, 0)

    def test_n_0_second(self):
        result = int_diff([1, 1, 1, 1], 0)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
