import unittest
from src.entities.user import User


class TestExercise(unittest.TestCase):

    def setUp(self):
        self.mockUser = User("User", "secretPass", "Beginner")

    def test_update_skill(self):
        self.mockUser.update_skill("Advanced")
        self.assertEqual(self.mockUser.skill, "Advanced")

    def test_initial_points(self):
        self.assertEqual(self.mockUser.get_points(), 0)

    def test_increase_points(self):
        self.mockUser.increase_points()
        self.assertEqual(self.mockUser.get_points(), 1)
