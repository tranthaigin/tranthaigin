import datetime as dt
import unittest
from build_streak import statistics

class WeeklyStreakTests(unittest.TestCase):
    def test_empty_history(self):
        self.assertEqual(statistics({}, dt.date(2026,10,31)), {'total':0,'current':[],'longest':[]})

    def test_sunday_boundary_and_unfinished_week(self):
        days = {'2026-10-17':2,'2026-10-18':3}
        stats = statistics(days, dt.date(2026,10,26))
        self.assertEqual(stats['total'], 5)
        self.assertEqual(stats['current'], ['2026-10-11','2026-10-18'])
        self.assertEqual(stats['longest'], stats['current'])
        self.assertEqual(statistics(days, dt.date(2026,11,1))['current'], [])

    def test_year_boundary_gap_and_future(self):
        days = {'2025-12-27':1,'2026-01-01':2,'2026-01-12':4,'2027-01-01':99}
        stats = statistics(days, dt.date(2026,1,13))
        self.assertEqual(stats['total'], 7)
        self.assertEqual(len(stats['longest']), 2)
        self.assertEqual(stats['current'], ['2026-01-11'])

if __name__ == '__main__': unittest.main()
