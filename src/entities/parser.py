import json


class Parser:
    """ Luokka, joka lukee tehtävät .json-tiedostosta.
        Attributes:
            _exercises:
                Lista, johon .json-tiedoston tehtävät luetaan
            _ids:
                Lista, johon tehtävien id:t luetaan.
    """

    def __init__(self):
        self._exercises = []
        self._ids = []

    def get_ex(self):
        """ Palauttaa tehtävät dict-tyyppisenä. """
        return self._exercises

    def get_ids(self):
        """ Palauttaa tehtävien id:t listana. """
        return self._ids

    def exercise_count(self):
        """ Palauttaa tehtävien lukumäärän."""
        return len(self._exercises)

    def parse(self, exercise_file):
        """ Lukee tehtävät ja niiden id:t ja lisää ne attribuuttien listoihin.

            Args:
                execise_file:
                    Merkkijonoarvo, joka on luettavan tiedoston nimi.

        """
        with open(exercise_file, encoding='UTF-8') as f:
            data = json.load(f)
        for ex in data:
            self._exercises.append(data[ex])
            self._ids.append(ex)
