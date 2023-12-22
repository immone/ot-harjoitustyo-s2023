import unittest
from src.entities.game import Game
from src.entities.user import User
from src.entities.exercise import TheoremExercise


class TestGame(unittest.TestCase):

    def setUp(self):
        self.mockUser = User("User", "secretPass", "easy")
        self.game = Game(('definition', 'group'), self.mockUser)

    def test_initial_user(self):
        self.assertEqual(self.game.player(), self.mockUser)

    def test_game_not_over(self):
        self.assertEqual(self.game.is_over(), False)

    def test_game_not_over2(self):
        self.game.problems = ['1', '2', '3']
        self.game.answered = 2
        self.assertEqual(self.game.is_over(), False)

    def test_game_over(self):
        self.game.problems = ['1', '2']
        self.game.answered = 2
        self.assertEqual(self.game.is_over(), True)

    def test_fetch_games(self):
        list = ['1', '2']
        self.game.problems = list
        self.assertEqual(self.game.exercises(), list)

    def test_set_done_method(self):
        theoremChoice = TheoremExercise("Theorem exercise",
                                        ['Which one is a?',
                                         'a',
                                         'b',
                                         'c',
                                         0,
                                         'group'],
                                        'easy',
                                        ex_id=123)

        self.game.problems = [theoremChoice]
        self.game.set_done(123)
        self.assertEqual(theoremChoice.is_done(), True)
