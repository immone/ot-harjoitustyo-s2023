import unittest
from src.repositories.exercise_repository import ExerciseRepository
from src.entities.parser import Parser
from src.entities.exercise import DefinitionExercise


class TestExerciseRepository(unittest.TestCase):

    def setUp(self):
        self.ex_repo = ExerciseRepository(
            "src/tests/repositories/test_json.json")

    def test_find_all(self):
        out = self.ex_repo.find_all()
        self.assertEqual(out[0].description, "Group definition")

    def test_set_find_all_by_difficulty(self):
        h = self.ex_repo.find_all_by_difficulty("hard")
        e = self.ex_repo.find_all_by_difficulty("easy")
        self.assertEqual(h, [])
        self.assertEqual(e[0].description, "Group definition")
