import unittest
from var_1_task_2 import armstrong_num
from var_1_task_1 import leap_year
from var_1_task_3 import is_fibbo


class MyTestCase(unittest.TestCase):
    def test_values(self):
        self.assertEqual(armstrong_num(), 7)
        self.assertEqual(leap_year(2016), True)
        self.assertEqual(leap_year(2015), False)
        self.assertEqual(is_fibbo(2, 3, 5, 8, 13), True)
        self.assertEqual(is_fibbo(2, 3, 5, 8, 12), False)

    def test_types(self):
        self.assertRaises(TypeError, leap_year, 'test')
        self.assertRaises(TypeError, leap_year, 2.46557)
        self.assertRaises(TypeError, leap_year, 4456-4645j)
        self.assertRaises(TypeError, leap_year, True)
        self.assertRaises(TypeError, leap_year, (1, 3, 5))
        self.assertRaises(TypeError, leap_year, [1, 4, 6])


if __name__ == '__main__':
    unittest.main()
