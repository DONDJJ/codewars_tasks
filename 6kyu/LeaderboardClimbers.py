import unittest

'''
Example:
['John',
 'Brian',
 'Jim',
 'Dave',
 'Fred']

Then you will be given a list of strings for example:
['Dave +1', 'Fred +4', 'Brian -1']

# Dave up 1             # Fred up 4             # Brian down 1
['John',                ['Fred',                ['Fred',
 'Brian',               'John',                  'John',
 'Dave',      =>        'Brian',       =>        'Dave',
 'Jim',                 'Dave',                  'Brian',
 'Fred']                'Jim']                   'Jim']
 
'''


def leaderboard_sort(leaderboard, changes):
    for i in changes:
        char_position = i.find('+') if i.find('+') != -1 else i.find('-')  # выяснить знак
        change = int(i[char_position:])  # выяснить на сколько изменилась позиция
        name = i[0:char_position - 1]  # выяснить имя
        name_pos_leaderboard = leaderboard.index(name)
        leaderboard.remove(name)
        leaderboard.insert(name_pos_leaderboard - change, name)

    return leaderboard


class LettersSearchTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(leaderboard_sort(['John', 'Brian', 'Jim', 'Dave', 'Fred'], ['Dave +1', 'Fred +4', 'Brian -1']),
                         ['Fred', 'John', 'Dave', 'Brian', 'Jim'])

    def test_2(self):
        self.assertEqual(leaderboard_sort(['Bob', 'Larry', 'Kevin', 'Jack', 'Max'], ['Max +3', 'Kevin -1', 'Kevin +3']),
                         ['Bob', 'Kevin', 'Max', 'Larry', 'Jack'])


if __name__ == '__main__':
    unittest.main()
