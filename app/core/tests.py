from core import calc
from django.test import SimpleTestCase


class CalcTests(SimpleTestCase):
    def test_add(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_sub(self):
        res = calc.sub(7, 6)

        self.assertEqual(res, 1)