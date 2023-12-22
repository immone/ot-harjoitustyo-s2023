from pathlib import Path
import json
from config import EXERCISES_FILE_PATH  # pylint: disable=import-error
from entities.parser import Parser
from entities.exercise import DefinitionExercise, TheoremExercise, ProblemExercise


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
        out = []
        exercises = filter(
            lambda exercise: exercise.difficulty == difficulty, exercises)
        for e in exercises:
            out.append(e)
        return out

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
        """ Lukee tehtävät tietokannasta Exercise-olioiksi.
        """

        ex_out = []
        self._ensure_file_exists()
        parser = Parser()
        parser.parse(EXERCISES_FILE_PATH)
        exercises = parser.get_ex()
        for ex in exercises:
            ex = ex[0]
            try:
                options = ex['options']
                question = ex['question']
                correct = ex['correct']
                structure = ex['structure']

                content = []
                content.append(question)
                for opt in options:
                    content.append(opt)
                content.append(correct)
                content.append(structure)

                description = ex['description']
                difficulty = ex['difficulty']
                hint = ex['hint']
                id_ex = ex['id']
                if type == 'definition':
                    new = DefinitionExercise(description,
                                             content,
                                             difficulty,
                                             hint,
                                             id_ex)
                elif type == 'problem':
                    new = ProblemExercise(description,
                                          content,
                                          difficulty,
                                          hint,
                                          id_ex)
                else:
                    new = TheoremExercise(description,
                                          content,
                                          difficulty,
                                          hint,
                                          id_ex)
                ex_out.append(new)
            except TypeError:
                print("Faulty exercise in DB.")

        return ex_out

    def _write(self, exercises):
        """ Kirjoittaa tietokantaan.

        Todo: Korjaa vastaamaan nykyistä .json-formaattia.
        """
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
