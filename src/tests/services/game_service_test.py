import unittest
from src.services.game_service import GameService
from src.entities.exercise import TheoremExercise

from src.entities.user import User


class TestGameService(unittest.TestCase):

    def setUp(self):
        self.game_service = GameService()
        self.user = User("nick", "pw", "easy")
        self.game = self.game_service.create_game(
            "theorem", "group", self.user)

    def test_create_game_user(self):
        curr = self.game_service.get_current_game()
        self.assertEqual(curr.user, self.user)

    def test_create_game_init_difficulty(self):
        curr = self.game_service.get_current_game()
        self.assertEqual(curr.user.skill, "easy")

    def test_increase_points(self):
        self.game_service.increase_points()
        self.assertEqual(self.game.correct, 1)

    def test_answered(self):
        self.assertEqual(self.game_service.answered(), 0)

    def test_correct(self):
        self.assertEqual(self.game_service.correct(), 0)

    def test_get_exercises_method(self):
        self.game.problems = ["one", "two"]
        self.assertEqual(self.game_service.get_exercises(), ["one", "two"])

    def test_get_undone_exercises(self):
        ex = TheoremExercise("Theorem exercise",
                             ['Which one is a?',
                              'a',
                              'b',
                              'c',
                              0,
                              'group'],
                             'easy')
        self.game.problems = [ex]
        self.assertEqual(self.game_service.get_undone_exercises(), [ex])
        ex.end_exercise()
        print(ex.is_done())

    def test_set_ex_done(self):
        ex = TheoremExercise("Theorem exercise",
                             ['Which one is a?',
                              'a',
                              'b',
                              'c',
                              0,
                              'group'],
                             'easy',
                             ex_id=222)
        self.game.problems = [ex]
        self.game_service.set_exercise_done(222)
        self.assertEqual(ex.is_done(), True)
