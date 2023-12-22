import unittest
from src.entities.question_generator import QuestionGenerator


class TestQuestionGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = QuestionGenerator("theorem", "easy", "group")

    def test_init_diff(self):
        self.assertEqual(self.generator.difficulty, "easy")

    def test_init_type(self):
        self.assertEqual(self.generator.type, "theorem")

    def test_init_structure(self):
        self.assertEqual(self.generator.structure, "group")
