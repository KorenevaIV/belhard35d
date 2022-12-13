# import unittest
#
from lessons.lesson15 import multiply
# class MainTestCase(unittest.TestCase):
#
#     def test_multiply(self):
#         self.assertEqual(multiply(2,4), 8)

import  pytest


@pytest.mark.parametrize(
    'a, b, c',
    (
            (4, 2, 7),
            (2, 3, 6),
            (8, 7, 21),
            (-12,4,-48),
            ('a', 3, 'aaa')
    )
)
def test_multiply(a, b, c):
    assert  multiply(a, b) == c
