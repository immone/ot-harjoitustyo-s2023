import unittest
from src.entities.exercise import TheoremExercise


class TestTheoremExercise(unittest.TestCase):

    def setUp(self):
        self.theoremChoice = TheoremExercise("Theorem exercise",
                                             ['Which one is a?',
                                              'a',
                                              'b',
                                              'c',
                                              0,
                                              'group'],
                                             'easy')

    def test_multiple_choice_initialization(self):
        self.assertEqual(self.theoremChoice.is_done(), False)

    def test_multiple_choice_guesses_positive(self):
        self.theoremChoice.check_answer(0)
        self.assertEqual(self.theoremChoice.solved, True)

    def test_multiple_choice_guesses_negative(self):
        self.theoremChoice.check_answer(2)
        self.theoremChoice.check_answer(1)
        self.assertEqual(self.theoremChoice.solved, False)

    def test_multiple_choice_solved(self):
        self.theoremChoice.done = True
        self.assertEqual(self.theoremChoice.is_done(), True)

    def test_multiple_choice_reduce_attempt(self):
        self.assertEqual(self.theoremChoice.is_done(), False)
        self.theoremChoice.decrease_attempts()
        self.assertEqual(self.theoremChoice.is_done(), True)

    def test_multiple_choice_raises_error_negative(self):
        with self.assertRaises(ValueError):
            self.theoremChoice.check_answer(-1)

    def test_multiple_choice_raises_error_above_bound(self):
        with self.assertRaises(ValueError):
            self.theoremChoice.check_answer(5)
