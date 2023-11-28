from pathlib import Path
import json
from enties.parser import Parser
from entities.exercise import DefinitionExercise
from repositories.user_repository import user_repository
from config import EXERCISES_FILE_PATH

## Todo: Make own repositories for each
## subclass of exercises

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
            Palauttaa listan Todo-olioita.
        """

        return self._read()

    def find_all_by_difficulty(self, difficulty):
        """Palauttaa kaikki halutun vaikeustason tehtävät.

                Args:
                    Difficulty: Merkkijono, joka kuvaa vaikeutta
                Returns:
                    Palauttaa listan Todo-olioita.
                """

        exercises = self.find_all()

        difficulty_exercises = filter(
            lambda exercise: exercise.user and exercise.difficulty == difficulty)

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

    def set_done(self, id, done=True):
        """Asettaa tehtävän tehdy-statuksen.

        Args:
            id: Tehtävän id, jonka tehty-status muutetaan.
            done:
                Vapaaehtoinen, oletusarvo True.
                Boolean-arvo, joka asetetaan tehtävän tehty-statukseksi.
        """

        exercises = self.find_all()

        for ex in exercises:
            if ex.id == id:
                ex.done = done
                break

        self._write(exercises)

    def delete(self, id):
        """Poistaa tietyn tehtävän.

        Args:
            id: Poistettavan tehtävän id.
        """

        exercises = self.find_all()

        exercises_without_id = filter(lambda exercise: exercise.id != id, exercises)

        self._write(exercises_without_id)

    def delete_all(self):
        """Poistaa kaikki tehtävät.
        """

        self._write([])

    def _ensure_file_exists(self):
        """ Varmistaa, että tehtävätiedosto on olemassa. """
        Path(self._file_path).touch()

    def _read(self):
        ex_out = []

        self._ensure_file_exists()
        parser = Parser()
        exercises = parser.get_ex(EXERCISES_FILE_PATH)
        for ex in exercises:
            ex_out.append(DefinitionExercise(ex['type'],
                                                ex['attempts'],
                                                ex['difficulty'],
                                                ex['hint'],
                                                ex['id']
                                            )
                          )
        return ex_out

    def _write(self, exercises):
        self._ensure_file_exists()

        data = {}
        for ex in exercises:
            data[ex.id] = {
                'type' : ex.type,
                'attempts' : ex.attempts,
                'difficulty' : ex.difficulty,
                'hint' : ex.hint,
            }
        with open(self._file_path, 'w') as f:
            json.dump(data, f, ensure_ascii=False)


ex_repository = ExerciseRepository(EXERCISES_FILE_PATH)