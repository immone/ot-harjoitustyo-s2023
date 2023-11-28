import unittest
from src.entities.exercise import Exercise, MultipleChoice, TheoremExercise


class TestExercise(unittest.TestCase):

    def setUp(self):
        self.theoremChoice = TheoremExercise("Theorem exercise", 1, 3)

    def test_multiple_choice_initialization(self):
        self.assertEqual(self.theoremChoice.is_done(), False)

    def test_multiple_choice_guesses_positive(self):
        self.theoremChoice.set_question(
            "Question", ["Right", "Wrong", "Wrong"], 1)
        self.theoremChoice.check_answer(1)
        self.assertEqual(self.theoremChoice.solved, True)

    def test_multiple_choice_guesses_negative(self):
        self.theoremChoice.set_question(
            "Question", ["Right", "Wrong", "Wrong"], 1)
        self.theoremChoice.check_answer(2)
        self.assertEqual(self.theoremChoice.solved, False)
