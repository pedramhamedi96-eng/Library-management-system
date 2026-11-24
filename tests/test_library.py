import unittest
from src.library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib = Library()

    def test_add_book(self):
        self.assertTrue(self.lib.add_book(1, "Python"))

    def test_add_member(self):
        self.assertTrue(self.lib.add_member(1, "Ali"))

    def test_borrow(self):
        self.lib.add_book(1, "Python")
        self.assertEqual(self.lib.borrow(1), "Python")

    def test_search(self):
        self.lib.add_book(1, "Python")
        self.assertEqual(self.lib.search("Python"), ["Python"])

    def test_return(self):
        self.lib.return_book(1, "Python")
        self.assertEqual(self.lib.search("Python"), ["Python"])
