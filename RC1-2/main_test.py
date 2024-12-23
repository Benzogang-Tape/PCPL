import main
from operator import itemgetter
import unittest


class TestMainMethods(unittest.TestCase):
    def test_first_task(self):
        test_data = [
            ('c', 'Ludovico Einaudi', 'Leningrad Philharmonic'),
            ("f", 'Ivan Dremin', 'Leningrad Philharmonic'),
            ('b', 'Ludwig van Beethoven', 'Benzogang Orchestra'),
            ('d', 'Edward Grieg', 'Leningrad Philharmonic'),
            ('e', 'Aram Khachaturian', 'Budapest Festival Orchestra'),
            ('a', 'Antonio Vivaldi ', 'Budapest Festival Orchestra')
        ]
        result = main.first_task(test_data)
        expected = sorted(test_data, key=itemgetter(0))
        self.assertEqual(expected, result)

    def test_second_task(self):
        test_data = [
            ('Fly', 'Ludovico Einaudi', 'Leningrad Philharmonic'),
            ("I'm swimming in the river", 'Ivan Dremin', 'Leningrad Philharmonic'),
            ('Moonlight Sonata', 'Ludwig van Beethoven', 'Benzogang Orchestra'),
            ('Morning', 'Edward Grieg', 'Leningrad Philharmonic'),
            ('Saber Dance', 'Aram Khachaturian', 'Budapest Festival Orchestra'),
            ('Summer Storm', 'Antonio Vivaldi ', 'Budapest Festival Orchestra')
        ]
        result = main.second_task(test_data)
        expected = [('Leningrad Philharmonic', 3), ('Budapest Festival Orchestra', 2), ('Benzogang Orchestra', 1)]
        self.assertEqual(expected, result)

    def test_third_task(self):
        test_data = [
            ('Fly', 'Ludovico Einaudi', 'Leningrad Philharmonic'),
            ("I'm swimming in the river", 'Ivan Dremin', 'Leningrad Philharmonic'),
            ("I'm crazy", 'Ivan Dremin', 'Unknown Orchestra'),
            ('Moonlight Sonata', 'Ludwig van Beethoven', 'Benzogang Orchestra'),
            ('Morning', 'Edward Grieg', 'Leningrad Philharmonic'),
            ('Saber Dance', 'Aram Khachaturian', 'Budapest Festival Orchestra'),
            ('Summer Storm', 'Antonio Vivaldi ', 'Budapest Festival Orchestra')
        ]
        result = main.third_task(test_data, 'n')
        expected = [
            ("I'm swimming in the river", 'Leningrad Philharmonic'),
            ("I'm crazy", 'Unknown Orchestra'),
            ('Moonlight Sonata', 'Benzogang Orchestra'),
            ('Saber Dance', 'Budapest Festival Orchestra')
        ]
        self.assertEqual(expected, result)