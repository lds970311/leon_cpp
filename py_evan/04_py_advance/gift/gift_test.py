# coding:utf-8
# time: 2023/5/12
# author: evan

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
