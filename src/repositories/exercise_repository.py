from pathlib import Path
import json
from config import EXERCISES_FILE_PATH # pylint: disable=import-error
from entities.parser import Parser
from entities.exercise import DefinitionExercise

# Todo: Make own repositories for each # subclass of exercises pylint: disable=fixme


class ExerciseRepository:
    """Tehtäviin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, file_path):
        """Luokan konstruktori.

        Args:
            file_path: Polku tiedostoon, johon tehtävät tallennetaan.
        """

        self._file_path = file_path

    def find_all(self):
        """Palauttaa kaikki tehtävät.

        Returns:
            Palauttaa listan Exercise-olioita.
        """

        return self._read()

    def find_all_by_difficulty(self, difficulty):
        """Palauttaa kaikki halutun vaikeustason tehtävät.

                Args:
                    Difficulty: Merkkijono, joka kuvaa vaikeutta
                Returns:
                    Palauttaa listan Exercise-olioita.
                """

        exercises = self.find_all()

        difficulty_exercises = filter(
            lambda exercise: exercise.user and exercise.difficulty == difficulty, exercises)

        return difficulty_exercises

    def find_by_username(self, username):
        """Palauttaa käyttäjän tehtävät.

        Args:
            username: Käyttäjän käyttäjätunnus, jonka tehtävät palautetaan.

        Returns:
            Palauttaa listan Exercise-olioita.
        """

        exercises = self.find_all()

        user_exercises = filter(
            lambda exercise: exercise.user and exercise.user.username == username, exercises)

        return list(user_exercises)

    def create(self, exercise):
        """Tallentaa tehtävän tietokantaan.

        Args:
            exercise: Tallennettava tehtävä Exercise-oliona.

        Returns:
            Tallennettu tehtävä Exercise-oliona.
        """

        exercises = self.find_all()

        exercises.append(exercise)

        self._write(exercises)

        return exercise

    def set_done(self, exercise_id, done=True):
        """Asettaa tehtävän tehdy-statuksen.

        Args:
            id: Tehtävän id, jonka tehty-status muutetaan.
            done:
                Vapaaehtoinen, oletusarvo True.
                Boolean-arvo, joka asetetaan tehtävän tehty-statukseksi.
        """

        exercises = self.find_all()

        for ex in exercises:
            if ex.id == exercise_id:
                ex.done = done
                break

        self._write(exercises)

    def delete(self, ex_id):
        """Poistaa tietyn tehtävän.

        Args:
            id: Poistettavan tehtävän id.
        """

        exercises = self.find_all()

        exercises_without_id = filter(
            lambda exercise: exercise.id != ex_id, exercises)

        self._write(exercises_without_id)

    def delete_all(self):
        """Poistaa kaikki tehtävät.
        """

        self._write([])

    def _ensure_file_exists(self):
        """ Varmistaa, että tehtävätiedosto on olemassa. """
        Path(self._file_path).touch()

    def _read(self):
        """ Lukee tehtävät tietokantaan.
        """

        ex_out = []

        self._ensure_file_exists()
        parser = Parser()
        parser.parse(EXERCISES_FILE_PATH)
        exercises = parser.get_ex()
        ids = parser.get_ids()
        for id in ids:
            try:
                ex = exercises[id]
                options = ex['options']
                question = ex['question']
                correct = ex['correct']
                new_exercise = DefinitionExercise(ex['type'],
                                                  ex['attempts'],
                                                  ex['difficulty'],
                                                  ex['hint'],
                                                  ex['id']
                                                  )
                new_exercise.set_question(question, options, correct)
            except TypeError:
                print("Faulty exercise on ID", id)

        return ex_out

    def _write(self, exercises):
        self._ensure_file_exists()

        data = {}
        for ex in exercises:
            data[ex.id] = {
                'type': ex.type,
                'attempts': ex.attempts,
                'difficulty': ex.difficulty,
                'hint': ex.hint,
            }
        with open(self._file_path, 'w', encoding='UTF-8') as f:
            json.dump(data, f, ensure_ascii=False)


ex_repository = ExerciseRepository(EXERCISES_FILE_PATH)
