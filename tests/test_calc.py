# -*- coding: UTF-8 -*-

import unittest
import sample.calc


class TestCase(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(sample.calc.plus(1, 2), 3)
        self.assertEqual(sample.calc.plus(0, 0), 0)
        self.assertEqual(sample.calc.plus(-1, -2), -3)
        self.assertEqual(sample.calc.plus(2, 1), 3)

    def test_minus(self):
        self.assertEqual(sample.calc.minus(1, 2), -1)
        self.assertEqual(sample.calc.minus(0, 0), 0)
        self.assertEqual(sample.calc.minus(-1, -2), 1)
        self.assertEqual(sample.calc.minus(2, 1), 1)
