import json


class Parser:
    """ Luokka, joka lukee tehtävät .json-tiedostosta.
        Attributes:
            self.exercises:
                Lista, johon .json-tiedoston tehtävät luetaan
            exercise_count:
                Kokonaislukuarvo, joka kuvaa luettujen tehtävien määrää
    """

    def __init__(self):
        self._exercises = []
        self._ids = []
        self.exercise_count = len(self._exercises)

    def get_ex(self):
        """ Palauttaa tehtävät dict-tyyppisenä. """
        return self._exercises

    def get_ids(self):
        """ Palauttaa tehtävien id:t listana '"""
        return self._ids

    def parse(self, exercise_file):
        """ Lukee tehtävät listaksi, joka koostuu dict-tyyppisistä tehtävistä.

            Args:
                execise_file:
                    Merkkijonoarvo, joka on luettavan tiedoston nimi.

        """
        with open(exercise_file, encoding='UTF-8') as f:
            data = json.load(f)
        for ex in data:
            self._exercises.append(data[ex])
            self._ids.append(ex)
