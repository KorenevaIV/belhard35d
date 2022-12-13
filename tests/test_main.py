import unittest

from lessons.lesson15 import multiply
class MainTestCase(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(2,4), 8)