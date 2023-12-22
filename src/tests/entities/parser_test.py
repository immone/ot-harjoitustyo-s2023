import unittest
from src.entities.parser import Parser


class TestParser(unittest.TestCase):

    def setUp(self):
        self.mockUser = Parser()

    def test_init_ex(self):
        self.assertEqual(self.mockUser.get_ex(), [])

    def test_init_id(self):
        self.assertEqual(self.mockUser.get_ids(), [])

    def test_update_ids(self):
        self.mockUser.parse("src/tests/entities/test_data.json")
        self.assertEqual(self.mockUser.get_ids(), ["123"])

    def test_update_data(self):
        self.mockUser.parse("src/tests/entities/test_data.json")
        self.assertEqual(self.mockUser.get_ex(), [[{
            "data": "What is included in the definition of a group?",
            "second": "otherstuff",
            "third": 123
        }]]
        )

    def test_update_data_length(self):
        self.assertEqual(self.mockUser.exercise_count(), 0)
        self.mockUser.parse("src/tests/entities/test_data.json")
        self.assertEqual(self.mockUser.exercise_count(), 1)
